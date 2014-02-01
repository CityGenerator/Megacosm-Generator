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
    worldId= int(request.args.get('worldId'))
    if (worldId == None):
        worldId=random.randint(1,100000)
    width=800
    height=500
    zoom=100.0
    xoffset=0
    yoffset=0
    # Generate the map data
    mapdata=generate_map(worldId,width,height,xoffset,yoffset,zoom)

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

def generate_map(worldId=0,width=800,height=500,xoffset=0.0,yoffset=0.0,zoom=600.0):
    """ Return a simple matrix of simplex noise from 0-255."""
    mapdata = []
    waterline=145
    print worldId
    for x in xrange(height):
        row=[]
        for y in xrange (width):
            noisevalue=snoise2(x/zoom+worldId+xoffset, y/zoom+worldId+yoffset,  6, 0.52,2.0, height/zoom*5, width/zoom, 1 )
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

