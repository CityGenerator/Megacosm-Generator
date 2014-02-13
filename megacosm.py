"""`main` is the top level module for this application."""

# Import the stuffs!
from flask import Flask, send_file, render_template, request, url_for
from generators import WorldMap, Star, StarSystem
import random
import redis
import ConfigParser
import pprint
import json
import os
import sys

MAPWIDTH=500
MAPHEIGHT=300

config = ConfigParser.RawConfigParser()
config.read( 'data/config.ini')

url = config.get('redis', 'url')
server=redis.from_url(url)

#pool = redis.ConnectionPool(host=config.get('redis', 'host'), port=config.get('redis', 'port'), db=0, password=config.get('redis', 'password'),   )
#server = redis.Redis(connection_pool=pool)    

# This thing here.. does stuff.
app = Flask(__name__)

@app.route('/')
def indexpage():
    """This is the first page anyone sees."""
    seed= request.args.get('seed')
    if (seed == None):
        seed=random.randint(1,100000)
    random.seed(int(seed))
    starsystem=StarSystem.StarSystem(server,{'seed':seed})

    return render_template('index.html',starsystem=starsystem) 


@app.route('/worldmap')
def worldmap():
    """A view into the solar system."""
    seed= request.args.get('seed')
    if (seed == None):
        seed=random.randint(1,100000)
    random.seed(int(seed))
    starsystem=StarSystem.StarSystem(server,{'seed':seed})

    return render_template('map.html', starsystem=starsystem )

@app.route('/worldmap.png')
def worldmappng():
    """Generate a worldmap and return it."""
    seed= request.args.get('seed')
    if (seed == None):
        seed=random.randint(1,100000)
    random.seed(int(seed))
    zoom=1.0
    xoffset=0
    yoffset=0
    # Generate the map data
    mapdata=WorldMap.generate_map(seed,MAPWIDTH,MAPHEIGHT,xoffset,yoffset,zoom)

    # Colorize the data and return a png.
    myImage=WorldMap.colorize_map(mapdata)

    return send_file(myImage, mimetype='image/png', cache_timeout=100)

@app.route('/worldbumpmap.png')
def worldbumpmap():
    """Generate a worldmap and return it."""
    seed= int(request.args.get('seed'))
    if (seed == None):
        seed=random.randint(1,100000)
    zoom=1.0
    xoffset=0
    yoffset=0
    # Generate the map data
    mapdata=WorldMap.generate_map(seed,MAPWIDTH,MAPHEIGHT,xoffset,yoffset,zoom)

    # Colorize the data and return a png.
    myImage=WorldMap.bump_map(mapdata)

    return send_file(myImage, mimetype='image/png', cache_timeout=100)

@app.route('/worldspecularmap.png')
def worldspecularmap():
    """Generate a worldmap and return it."""
    seed= int(request.args.get('seed'))
    if (seed == None):
        seed=random.randint(1,100000)
    zoom=1.0
    xoffset=0
    yoffset=0
    # Generate the map data
    mapdata=WorldMap.generate_map(seed,MAPWIDTH,MAPHEIGHT,xoffset,yoffset,zoom)

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




