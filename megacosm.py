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
import re

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
    return render_template('index.html') 


@app.route('/npc')
def GenerateNPC():
    """Generate an NPC"""
    seed=set_seed( request.args.get('seed') )

    npcfeatures={'seed':seed,}

    races=server.lrange('race',0,-1);
    professions=server.lrange('npc_profession',0,-1);
    attitudes=server.lrange('npc_attitude',0,-1);
    motivations=server.lrange('npc_motivation',0,-1);
    emotions=server.lrange('npc_emotion',0,-1);
    for param in request.args :
        if re.match('^npc_.*_roll$',param) and int(request.args[param])>=0 and int(request.args[param])<=100 :
            print "param is",param,"=",request.args[param]
            npcfeatures[param]=int(request.args[param])
        elif re.match('^npc_race$',param) and request.args[param] in races:
            npcfeatures['race']=request.args[param]
        elif re.match('^npc_profession$',param) and request.args[param] in professions:
            npcfeatures['profession']=request.args[param]
        elif re.match('^npc_attitude$',param) and request.args[param] in attitudes:
            npcfeatures['attitude']=request.args[param]
        elif re.match('^npc_motivation$',param) and request.args[param] in motivations:
            npcfeatures['motivation']=request.args[param]
        elif re.match('^npc_emotion$',param) and request.args[param] in emotions:
            npcfeatures['emotion']=request.args[param]

    npc=NPC.NPC(server,npcfeatures)
    return render_template('npc.html',npc=npc) 

@app.route('/npc_builder')
def NPC_Builder():
    """Generate an NPC"""

    stats=server.lrange('npcstats',0,-1)
    statinfo={}
    races=server.lrange('race',0,-1);
    professions=server.lrange('npc_profession',0,-1);
    attitudes=server.lrange('npc_attitude',0,-1);
    motivations=server.lrange('npc_motivation',0,-1);
    emotions=server.lrange('npc_emotion',0,-1);
    for stat in stats :
        statinfo[stat]=[]
        for statstring in server.zrange('npc_'+stat,0,-1):
            statinfo[stat].append(json.loads(statstring))
    
    return render_template('npc_builder.html',statinfo=statinfo, otherstats={'race':races,'profession':professions,'attitude':attitudes,'motivation':motivations,'emotion':emotions}) 

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




