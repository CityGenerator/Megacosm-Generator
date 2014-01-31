"""`main` is the top level module for this application."""


# Import the stuffs!
from flask import Flask, send_file, render_template, request, url_for
from noise import snoise2, snoise3, snoise4
from StringIO import StringIO
import png
import random


# This thing here.. does stuff.
app = Flask(__name__)


@app.route('/')
def welcomepage():
    """This is the first page anyone sees."""
    worldId= request.args.get('worldId')
    if (worldId == None):
        worldId=random.randint(1,100000)
    return render_template('map.html', worldId=worldId)

@app.route('/worldmap.png')
def worldmap():
    """Generate a worldmap and return it."""
    worldId= request.args.get('worldId')
    random.seed(worldId)
    myMap=generate_map(worldId)

    # Create a temp file for writing the image
    img_io = StringIO()

    # Convert the matrix of pixels into a png, then write it to the temp file
    imagewriter = png.Writer(len(myMap[0])/3, len(myMap))
    imagewriter.write(img_io,myMap) 

    #ensure the image is properly flushed
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png', cache_timeout=100)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def page_borked(e):
    """Return a custom 500 error. Only hit when debugging is off."""
    message="You Broke it!"
    return message, 500

def generate_map(worldId):
    offset=random.randint(1,100000)
    s = []
    zoom=250.0
    waterline=145
    for x in xrange(500):
        row=[]
        for y in xrange (800):
            
            pixel=snoise2(x/zoom+offset , y/zoom+offset,  4, 0.4,2.0, 500/zoom*4, 800/zoom, 1 )
#            pixel=snoise3(x/zoom,y/zoom, offset,  4, 0.4, 2.0 )
#            pixel=snoise4(x/zoom,y/zoom, offset,offset ,  4, 0.4, 2.0 )
            # noise2(x, y,       octaves=1, persistence=0.5, lacunarity=2.0, repeatx=None, repeaty=None, base=0.0) return simplex noise value for specified 2D coordinate.
            # noise3(x, y, z,    octaves=1, persistence=0.5, lacunarity=2.0)
            # noise4(x, y, z, w, octaves=1, persistence=0.5, lacunarity=2.0)
            pixel=int((pixel+1)/2*255-1)

            if (pixel <waterline):
                row.append(max(pixel/2,0))
                row.append(max(pixel/2,0))
                row.append(255-max(pixel/4,0))
            else:
                pixel=(pixel-waterline)* 255/waterline
                row.append(54+pixel)
                row.append(54+pixel)
                row.append(pixel)
        s.append(row)
    return s


if __name__ == '__main__':
    app.debug = True
    app.run()
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server...except we do to get it to run without app engine/

