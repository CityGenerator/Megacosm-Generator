#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import the stuffs!

"""`main` is the top level module for this application."""

from flask import Flask, render_template, request
from flask_assets import Environment, Bundle

from megacosm.generators.Business import Business
from megacosm.generators.City import City
from megacosm.generators.Continent import Continent
from megacosm.generators.Country import Country
from megacosm.generators.Deity import Deity
from megacosm.generators.Flag import Flag
from megacosm.generators.GeomorphDungeon import GeomorphDungeon
from megacosm.generators.Govt import Govt
from megacosm.generators.Leader import Leader
from megacosm.generators.MagicItem import MagicItem
from megacosm.generators.Moon import Moon
from megacosm.generators.NPC import NPC
from megacosm.generators.Organization import Organization
from megacosm.generators.Planet import Planet
from megacosm.generators.Region import Region
from megacosm.generators.RogueDungeon import RogueDungeon
from megacosm.generators.Sect import Sect
from megacosm.generators.Star import Star
from megacosm.generators.Street import Street
from megacosm.generators.Wanted import Wanted
from megacosm.generators.Weather import Weather
from megacosm.util.Seeds import set_seed
from megacosm.util import Filters
# from megacosm import oneliners
import datetime
import json
import re
import traceback


def create_app(config_location='config.BaseConfiguration'):
    myapp = Flask(__name__)
    myapp.config.from_object(config_location)
    return myapp


app = create_app()

#########################################################################
# Using JS and CSS bundlers to minify code.
assets = Environment(app)

js = Bundle(
    'js/threejs/seedrandom-2.3.10.min.js',
    #    'js/*.js',
    #    filters='jsmin',
    output='gen/jspacked.js'
)
assets.register('js_all', js)

css = Bundle('css/*.css',
             #    filters='yui_css',
             #    output='gen/csspacked.css'
             )
assets.register('css_all', css)

jsflag = Bundle(

    'js/flag/*.js',
    #    filters='jsmin',
    output='gen/flagpacked.js'
)
assets.register('js_flag', jsflag)

jscity = Bundle(

    'js/threejs/three*.js',
    'js/threejs/stats.min.js',
    'js/threejs/OrbitControls.js',
    'js/threejs/ImprovedNoise.js',
    'js/threejs/Detector.js',
    'js/city/*.js',
    # FIXME this can't be packed without breaking perlin noise... why??
    #    filters='jsmin',
    #    output='gen/citypacked.js'
)
assets.register('js_city', jscity)


#########################################################################

@app.route('/')
def indexpage():
    """This is the first page anyone sees."""

    return render_template('index.html')


#########################################################################

@app.route('/magicitem')
def generatemagicitem():
    """Generate a MagicItem"""

    features = feature_filter('magicitem')
    magicitem = MagicItem(app.config['REDIS'], features)

    kind = magicitem.kind
    return render_template('magicitem_' + kind + '.html', tempobj=magicitem)


@app.route('/magicitem_builder')
def magicitem_builder():
    """Build a Magic Item"""

    classname = 'magicitem'
    (plist, pstring, pset) = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/npc')
def generatenpc():
    """Generate an NPC"""

    features = feature_filter('npc')
    features['deity'] = Deity(app.config['REDIS'])
    tempobj = NPC(app.config['REDIS'], features)
    return render_template('npc.html', tempobj=tempobj)


@app.route('/npc_builder')
def npc_builder():
    """Build an NPC"""

    classname = 'npc'
    (plist, pstring, pset) = builder_form_data(classname)

    return render_template('npc_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/planet_builder')
def planet_builder():
    """Build a planet"""

    classname = 'planet'
    (plist, pstring, pset) = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


@app.route('/planet')
def generateplanet():
    """Generate a planet"""

    features = feature_filter('planet')
    planet = Planet(app.config['REDIS'], features)
    planet.add_continents()
    return render_template('planet.html', tempobj=planet)


#########################################################################

@app.route('/organization')
def generate_organization():
    """Generate a simple organization"""

    features = feature_filter('organization')
    tempobj = Organization(app.config['REDIS'], features)
    return render_template('organization.html', tempobj=tempobj)


@app.route('/organization_builder')
def organization_builder():
    """Generate the basic data about a organization"""

    classname = 'organization'
    (plist, pstring, pset) = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/business')
def generate_business():
    """Generate a business"""

    features = feature_filter('business')
    business = Business(app.config['REDIS'], features)
    return render_template('business.html', tempobj=business)


@app.route('/business_builder')
def business_builder():
    """Build a a business"""

    classname = 'business'
    (plist, pstring, pset) = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/street')
def generatestreet():
    """Generate a street"""

    features = feature_filter('street')
    tempobj = Street(app.config['REDIS'], features)
    return render_template('street.html', tempobj=tempobj)


@app.route('/street_builder')
def street_builder():
    """Build a a street"""

    classname = 'street'
    (plist, pstring, pset) = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/moon')
def generatemoon():
    """Generate a moon"""

    features = feature_filter('moon')
    moon = Moon(app.config['REDIS'], features)
    return render_template('moon.html', tempobj=moon)


@app.route('/moon_builder')
def moon_builder():
    """Build a a moon"""

    classname = 'moon'
    (plist, pstring, pset) = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/star')
def generatestar():
    """Generate a star"""

    features = feature_filter('star')
    star = Star(app.config['REDIS'], features)
    return render_template('star.html', tempobj=star)


@app.route('/star_builder')
def star_builder():
    """Build a a star"""

    classname = 'star'
    (plist, pstring, pset) = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/continent')
def generatecontinent():
    """Generate a continent"""

    features = feature_filter('continent')
    continent = Continent(app.config['REDIS'], features)
    continent.add_countries()
    return render_template('continent.html', tempobj=continent)


@app.route('/continent_builder')
def continent_builder():
    """Build a a continent"""

    classname = 'continent'
    (plist, pstring, pset) = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/region')
def generateregion():
    """Generate a region"""

    features = feature_filter('region')
    region = Region(app.config['REDIS'], features)

    #    region.add_cities()
    #    region.add_locations()()

    return render_template('region.html', tempobj=region)


@app.route('/region_builder')
def region_builder():
    """Build a a region"""

    classname = 'region'
    (plist, pstring, pset) = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/sect')
def generatesect():
    """Generate a sect"""

    features = feature_filter('sect')
    sect = Sect(app.config['REDIS'], features)
    return render_template('sect.html', tempobj=sect)


@app.route('/sect_builder')
def sect_builder():
    """Build a a sect"""

    classname = 'sect'
    (plist, pstring, pset) = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/govt')
def generategovt():
    """Generate a govt"""

    features = feature_filter('govt')
    govt = Govt(app.config['REDIS'], features)
    return render_template('govt.html', tempobj=govt)


@app.route('/govt_builder')
def govt_builder():
    """Build a a govt"""

    classname = 'govt'
    (plist, pstring, pset) = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################


@app.route('/city')
def generate_city():
    """Generate a simple city"""
    features = feature_filter('city')
    tempobj = City(app.config['REDIS'], features)
    return render_template('city.html', tempobj=tempobj)


@app.route('/city_builder')
def city_builder():
    """Generate the basic data about a city"""
    classname = 'city'
    (paramlist, paramstring, paramset) = builder_form_data(classname)
    return render_template('generic_builder.html', paramlist=paramlist,
                           paramstring=paramstring, paramset=paramset, name=classname)


#########################################################################


@app.route('/weather')
def generate_weather():
    """Generate a weather"""

    features = feature_filter('weather')
    weather = Weather(app.config['REDIS'], features)
    return render_template('weather.html', tempobj=weather)


@app.route('/weather_builder')
def weather_builder():
    """Build a a weather"""

    classname = 'weather'
    (plist, pstring, pset) = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/wanted')
def generatewanted():
    """Generate a wanted"""

    features = feature_filter('wanted')
    wanted = Wanted(app.config['REDIS'], features)
    return render_template('wanted.html', tempobj=wanted)


@app.route('/wanted_builder')
def wanted_builder():
    """Build a a wanted"""

    classname = 'wanted'
    (plist, pstring, pset) = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/geomorphdungeon')
def generategeomorphdungeon():
    """Generate a geomorphdungeon"""

    features = feature_filter('geomorphdungeon')
    geomorphdungeon = GeomorphDungeon(app.config['REDIS'], features)
    return render_template('geomorphdungeon.html', tempobj=geomorphdungeon,
                           jsondata=geomorphdungeon.simplify_for_json())


@app.route('/geomorphdungeon_builder')
def geomorphdungeon_builder():
    """Build a a geomorphdungeon"""

    classname = 'geomorphdungeon'
    (plist, pstring, pset) = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/roguedungeon')
def generateroguedungeon():
    """Generate a dungeon"""

    features = feature_filter('roguedungeon')
    roguedungeon = RogueDungeon(app.config['REDIS'], features)
    return render_template('roguedungeon.html', tempobj=roguedungeon, jsondata=roguedungeon.simplify_for_json())


@app.route('/roguedungeon_builder')
def roguedungeon_builder():
    """Build a a dungeon"""

    classname = 'roguedungeon'
    (plist, pstring, pset) = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/country')
def generatecountry():
    """Generate a country"""

    features = feature_filter('country')
    country = Country(app.config['REDIS'], features)
    country.add_regions()
    return render_template('country.html', tempobj=country)


@app.route('/country_builder')
def country_builder():
    """Build a a country"""

    classname = 'country'
    (plist, pstring, pset) = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/deity')
def generatedeity():
    """Generate a deity"""

    features = feature_filter('deity')
    deity = Deity(app.config['REDIS'], features)
    return render_template('deity.html', tempobj=deity)


@app.route('/deity_builder')
def deity_builder():
    """Build a a deity"""

    classname = 'deity'
    (plist, pstring, pset) = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/leader')
def generateleader():
    """Generate a leader"""

    features = feature_filter('leader')
    leader = Leader(app.config['REDIS'], features)
    return render_template('leader.html', tempobj=leader)


@app.route('/leader_builder')
def leader_builder():
    """Build a a leader"""

    classname = 'leader'
    (plist, pstring, pset) = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/flag')
def generateflag():
    """Generate a flag"""

    features = feature_filter('flag')
    app.flag = Flag(app.config['REDIS'], features)
    return render_template('flag.html', tempobj=app.flag, flagjson=app.flag.tojson())


@app.route('/flag_builder')
def flag_builder():
    """Build a a flag"""

    classname = 'flag'
    (plist, pstring, pset) = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################
#########################################################################
#########################################################################


def feature_filter(generator):
    """Turn the request string into a feature set."""

    seed = set_seed(request.args.get('seed'))

    saveparamregex = re.compile('^[0-9A-Za-z_]+$')
    genregex = re.compile('^' + generator + '_[a-z_]+$')
    genrollregex = re.compile('^' + generator + '_[a-z_]+_(roll|chance)$')

    app.logger.debug('Request Seed: %i', seed)
    features = {'seed': seed}
    for param in request.args:
        # if npc_ethics has a valid score
        if genrollregex.match(param) and isvalidscore(request.args[param]):
            features[param] = int(request.args[param])
        # if npc_hair_roll is a digit
        elif genregex.match(param) and str(request.args[param]).isdigit():
            fieldname = re.sub(generator + '_', '', param)
            features[fieldname] = app.config['REDIS'].lrange(
                                                        param,
                                                        int(request.args[param]),
                                                        int(request.args[param]))[0]
        # if business_kind='temple'
        elif genregex.match(param) and saveparamregex.match(request.args[param]):
            # check to see if business_kind "temple" exists
            if app.config['REDIS'].keys(param):
                app.logger.debug("%s is a key", param)
                if request.args[param] in app.config['REDIS'].lrange(param, 0, -1):
                    app.logger.debug("%s was in %s", request.args[param], param)
                    # If it does, add it to features.
                    newparam = param[len(generator) + 1:]
                    features[newparam] = request.args[param]
                    app.logger.debug("%s %s", newparam, request.args[param])
    return features


def builder_form_data(generator):
    """Turn the fields of a generator into fodder for the generic_builder"""

    plist = {}
    pstring = {}
    pset = {}
    for key in app.config['REDIS'].keys(generator + '_*'):
        fieldname = key.replace(generator + '_', '')
        if app.config['REDIS'].type(key) == 'list':
            plist[fieldname] = app.config['REDIS'].lrange(key, 0, -1)
        elif app.config['REDIS'].type(key) == 'string':
            pstring[fieldname] = app.config['REDIS'].get(key)
        elif app.config['REDIS'].type(key) == 'zset':
            result = app.config['REDIS'].zrangebyscore(key, 1, 100)
            pset[fieldname] = []
            for field in result:
                try:
                    pset[fieldname].append(json.loads(field))
                except ValueError:
                    raise ValueError('failed to parse %s field %s' % (key, field))
    return plist, pstring, pset


def isvalidscore(value):
    """Verify if a string is a valid score."""

    if value.isdigit():
        if 0 <= int(value) <= 100:
            return True
        else:
            return False
    else:
        return False


@app.errorhandler(404)
def page_not_found(error):
    """Return a custom 404 error."""

    print(' =======================')
    print('Exception:', error)
    time = str(datetime.datetime.now())
    return render_template('400.html', request=request, time=time), 404


@app.errorhandler(500)
def page_borked(error):
    """Return a custom 500 error. Only hit when debugging is off."""

    print(' =======================')
    print('problem with ', request.url)
    time = str(datetime.datetime.now())
    print('Exception:', error)
    traceback.print_exc()

    return render_template('500.html', request=request, e=error, time=time), 500


@app.template_filter('uppercase')
def select_uppercase(word):
    """Switch the word to uppercase"""

    return Filters.select_uppercase(word)


@app.template_filter('article')
def select_article(noun):
    """Select the proper article for a noun."""

    return Filters.select_article(noun)


@app.template_filter('pluralize')
def select_pluralize(verb, count):
    """Select the proper verb for a count."""

    return Filters.select_pluralize(verb, count)


@app.template_filter('conjunction')
def select_conjunction(wordlist):
    """Join a list with commas and such."""

    return Filters.select_conjunction(wordlist)


@app.template_filter('plural_verb')
def select_plural_verb(verb, subject):
    """select the proper plural verb."""

    # FIXME is this a duplicate of select_pluralize???

    return Filters.select_plural_verb(verb, subject)


@app.template_filter('plural_adj')
def select_plural_adj(adj, subject):
    """Select the proper version of an adjective."""

    # FIXME is this correct? or is it count-based?

    return Filters.select_plural_adj(adj, subject)


if __name__ == '__main__':
    app.run()
