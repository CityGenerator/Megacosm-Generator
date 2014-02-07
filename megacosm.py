"""`main` is the top level module for this application."""

# Import the stuffs!
from flask import Flask, send_file, render_template, request, url_for
from generators import WorldMap, Star, StarSystem
import random
import redis
import ConfigParser
import os
import sys


config = ConfigParser.RawConfigParser()
config.read( '../data/config.ini')

#url = config.get('redis', 'url')
#server=redis.from_url(url)


pool = redis.ConnectionPool(host=config.get('redis', 'host'), port=config.get('redis', 'port'), db=0, password=config.get('redis', 'password'),   )
server = redis.Redis(connection_pool=pool)    

# This thing here.. does stuff.
app = Flask(__name__)

@app.route('/')
def welcomepage():
    """This is the first page anyone sees."""
    worldId= request.args.get('worldId')
    if (worldId == None):
        worldId=random.randint(1,100000)

    starsystem=StarSystem.StarSystem(server,worldId)

    worldname=WorldMap.generate_name(worldId,server)
    return render_template('map.html', worldId=worldId, worldname=worldname)

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

@app.route('/worldbumpmap.png')
def worldbumpmap():
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
    myImage=WorldMap.bump_map(mapdata)

    return send_file(myImage, mimetype='image/png', cache_timeout=100)

@app.route('/worldspecularmap.png')
def worldspecularmap():
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
    myImage=WorldMap.specular_map(mapdata)

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




