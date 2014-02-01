"""`main` is the top level module for this application."""

# Import the stuffs!
from flask import Flask, send_file, render_template, request, url_for
from generators import WorldMap

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
    zoom=1.0
    xoffset=0
    yoffset=0
    # Generate the map data
    mapdata=WorldMap.generate_map(worldId,width,height,xoffset,yoffset,zoom)

    # Colorize the data and return a png.
    myImage=WorldMap.colorize_map(mapdata)

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


if __name__ == '__main__':
    app.debug = True
    app.run()
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server...except we do to get it to run without app engine/

