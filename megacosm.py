"""`main` is the top level module for this application."""

# Import the stuffs!
from flask import Flask, send_file, render_template, request, url_for
from generators import Star, StarSystem, NPC
from util.MakeMap import *
from util.Seeds import *
import random
import redis
import ConfigParser
import pprint
import json
import os
import sys
import inflect

p = inflect.engine()

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
    seed=set_seed( request.args.get('seed') )

    starsystem=StarSystem.StarSystem(server,{'seed':seed})

    return render_template('index.html',starsystem=starsystem) 


@app.route('/npc')
def GenerateNPC():
    """Generate an NPC"""
    seed=set_seed( request.args.get('seed') )

    npc=NPC.NPC(server,{'seed':seed})

    return render_template('npc.html',npc=npc) 



@app.route('/continentmap')
def continentmap():
    """A view into the solar system."""
    seed=set_seed( request.args.get('seed') )

    starsystem=StarSystem.StarSystem(server,{'seed':seed})

    # Colorize the data and return a png.
    myImage=generate_image(starsystem.planet.continent[0].mapdata)


    return send_file(myImage, mimetype='image/png', cache_timeout=100)




@app.route('/worldmap')
def worldmap():
    """A view into the solar system."""
    seed=set_seed( request.args.get('seed') )

    starsystem=StarSystem.StarSystem(server,{'seed':seed})

    return render_template('map.html', starsystem=starsystem )

@app.route('/worldmap.png')
def worldmappng():
    """Generate a worldmap and return it."""
    seed=set_seed( request.args.get('seed') )

    # Generate the map data
    starsystem=StarSystem.StarSystem(server,{'seed':seed})

    # Colorize the data and return a png.
    myImage=generate_image(starsystem.planet.mapdata)

    return send_file(myImage, mimetype='image/png', cache_timeout=100)

@app.route('/worldbumpmap.png')
def worldbumpmap():
    """Generate a worldmap and return it."""
    seed=set_seed( request.args.get('seed') )

    # Generate the map data
    starsystem=StarSystem.StarSystem(server,{'seed':seed})

    # Colorize the data and return a png.
    myImage=generate_bump_image(starsystem.planet.mapdata)

    return send_file(myImage, mimetype='image/png', cache_timeout=100)

@app.route('/worldspecularmap.png')
def worldspecularmap():
    """Generate a worldmap and return it."""
    seed=set_seed( request.args.get('seed') )

    # Generate the map data
    starsystem=StarSystem.StarSystem(server,{'seed':seed})

    # Colorize the data and return a png.
    myImage=generate_specular_image(starsystem.planet.mapdata)

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

@app.template_filter('article')
def select_article(s):
    return p.an(s)

@app.template_filter('pluralize')
def select_pluralize(s):
    return p.plural(s)



if __name__ == '__main__':
    app.debug = True
    app.run()




