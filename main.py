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

    # Generate the map data
    mapdata=generate_map(worldId)

    # Colorize the data and return a png.
    myImage=colorize_map(mapdata)

    return send_file(myImage, mimetype='image/png', cache_timeout=100)

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
    """ Return a simple matrix of simplex noise from 0-255."""
    offset=random.randint(1,100000)
    mapdata = []
    zoom=140.0
    waterline=145
    for x in xrange(500):
        row=[]
        for y in xrange (800):
            noisevalue=snoise2(x/zoom , y/zoom,  10, 0.5,2.0, 500/zoom*5, 800/zoom, 1 )
            pixel=int((noisevalue+1)/2*255-1)
            row.append(pixel)
        mapdata.append(row)
    return mapdata

def colorize_map(mapdata):
    """ Convert the black and white pixel data to actual map-looking colors."""
    image=[]
    waterline=145
    for row in mapdata:
        imagerow=[]
        for y in row:
            pixel=y;
            color=(pixel,pixel,pixel) # land
            if (pixel < waterline-50):
                color=(0,0,205) # Deepest
            elif (pixel <waterline-15):
                color=(10,10,255) # Deep
            elif (pixel <waterline):
                color=(55,55,255) # Shallow
            #Note that this is actually tripling the width of the array for RGB values.
            imagerow.extend(color)
        image.append(imagerow)
    # Create a temp file for writing the image
    img_io = StringIO()

    # Convert the matrix of pixels into a png, then write it to the temp file
    imagewriter = png.Writer(len(image[0])/3, len(image))
    imagewriter.write(img_io,image) 

    #ensure the image is properly flushed
    img_io.seek(0)

    return img_io


if __name__ == '__main__':
    app.debug = True
    app.run()
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server...except we do to get it to run without app engine/

