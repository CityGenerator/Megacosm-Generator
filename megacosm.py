"""`main` is the top level module for this application."""

# Import the stuffs!
from flask import Flask, render_template, request
from generators import Artwork
from generators import Planet
from generators import NPC
from generators import MagicItem
from generators import Deity
from generators import Bond
from generators import Rumor
from generators import Cuisine
from generators import Continent
from generators import Country
from generators import Sect
from generators import Leader
from generators import Legend
from generators import Business
from generators import Star
from generators import Moon
from generators import Currency
from generators import Misfire
from generators import Region
from generators import Wanted
from generators import Weather
from generators import Govt
from generators import Resource
from generators import Event
from generators import JobPosting
from generators import Gem
from generators import MundaneItem
from generators import Motivation
from generators import RogueDungeon
from generators import GeomorphDungeon
from generators import Street
from generators import Flag
from util.Seeds import set_seed
from generators import Organization
from util import Filters
import logging
import logging.config
import redis
import ConfigParser
import datetime
import json
import re
import traceback

CONFIG = ConfigParser.RawConfigParser()
CONFIG.read('data/config.ini')

URL = CONFIG.get('redis', 'url')
server = redis.from_url(URL)

# This thing here.. does stuff.
app = Flask(__name__)

logfile= open(CONFIG.get('logging', 'path'))
logging.config.dictConfig(json.load(logfile))


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
    magicitem = MagicItem.MagicItem(server, features)

    kind = magicitem.kind
    return render_template('magicitem_'+kind+'.html', tempobj=magicitem)

@app.route('/magicitem_builder')
def magicitem_builder():
    """Build a Magic Item"""

    classname = 'magicitem'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################


@app.route('/npc')
def generatenpc():
    """Generate an NPC"""

    features = feature_filter('npc')
    features['deity'] = Deity.Deity(server)
    tempobj = NPC.NPC(server, features)
    return render_template('npc.html', tempobj=tempobj)

@app.route('/npc_builder')
def npc_builder():
    """Build an NPC"""
    classname = 'npc'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/bond')
def generatebond():
    """Generate a bond"""

    features = feature_filter('bond')
    titletext = 'The Ties that Bind Us..'
    features['npc'] = NPC.NPC(server)
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count']) > 1 and int(request.args['count']) <= 100:
        bonds = []
        for _ in xrange(int(request.args['count'])):
            bonds.append(Bond.Bond(server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=bonds, oneliner=bonds[0], titletext=titletext, generator='bond')
    else:
        bond = Bond.Bond(server, features)
        return render_template('oneliner.html', oneliner=bond, titletext=titletext, generator='bond')

@app.route('/bond_builder')
def bond_builder():
    """Build a bond"""

    statinfo = {}
    for stat in ['when', 'template']:
        statinfo[stat] = []
        for statstring in server.lrange('bond_'+stat, 0, -1):
            statinfo[stat].append(statstring)

    return render_template('bond_builder.html', statinfo=statinfo)

#########################################################################
@app.route('/planet_builder')
def planet_builder():
    """Build a planet"""
    classname = 'planet'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


@app.route('/planet')
def generateplanet():
    """Generate a planet"""
    features = feature_filter('planet')
    planet = Planet.Planet(server, features)
    planet.add_continents()
    return render_template('planet.html', tempobj=planet)


#########################################################################

@app.route('/resource')
def generateresource():
    """Generate a resource"""

    features = feature_filter('resource')
    titletext = 'At Your Disposal...'
    features['npc'] = NPC.NPC(server)
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count']) > 1 and int(request.args['count']) <= 100:
        resources = []
        for _ in xrange(int(request.args['count'])):
            resources.append(Resource.Resource(server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=resources, oneliner=resources[0], titletext=titletext, generator='resource')
    else:
        resource = Resource.Resource(server, features)
        return render_template('oneliner.html', oneliner=resource, titletext=titletext, generator='resource')



@app.route('/resource_builder')
def resource_builder():
    """Build a resource"""
    classname = 'resource'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################

@app.route('/artwork')
def generateartwork():
    """Generate a artwork"""
    features = feature_filter('artwork')
    titletext = 'A Work of Art...'
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count']) > 1 and int(request.args['count']) <= 100:
        artworks = []
        for _ in xrange(int(request.args['count'])):
            artworks.append(Artwork.Artwork(server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=artworks, oneliner=artworks[0], titletext=titletext, generator='artwork')
    else:
        artwork = Artwork.Artwork(server, features)
        return render_template('oneliner.html', oneliner=artwork, titletext=titletext, generator='artwork')



@app.route('/artwork_builder')
def artwork_builder():
    """Build a a artwork"""
    classname = 'artwork'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################

@app.route('/rumor')
def generaterumor():
    """Generate a rumor"""
    features = feature_filter('rumor')
    titletext = 'Did You Hear?'
    features['npc'] = NPC.NPC(server)
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count']) > 1 and int(request.args['count']) <= 100:
        rumors = []
        for _ in xrange(int(request.args['count'])):
            rumors.append(Rumor.Rumor(server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=rumors, oneliner=rumors[0], titletext=titletext, generator='rumor')
    else:
        rumor = Rumor.Rumor(server, features)
        return render_template('oneliner.html', oneliner=rumor, titletext=titletext, generator='rumor')



@app.route('/rumor_builder')
def rumor_builder():
    """Build a a rumor"""
    classname = 'rumor'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################

@app.route('/misfire')
def generatemisfire():
    """Generate a misfire"""

    features = feature_filter('misfire')
    titletext = 'My Spell Misfired!'
    features['npc'] = NPC.NPC(server)
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count']) > 1 and int(request.args['count']) <= 100:
        misfires = []
        for _ in xrange(int(request.args['count'])):
            misfires.append(Misfire.Misfire(server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=misfires, oneliner=misfires[0], titletext=titletext, generator='misfire')
    else:
        misfire = Misfire.Misfire(server, features)
        return render_template('oneliner.html', oneliner=misfire, titletext=titletext, generator='misfire')


@app.route('/misfire_builder')
def misfire_builder():
    """Build a a misfire"""
    classname = 'misfire'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################


@app.route('/currency')
def generatecurrency():
    """Generate a currency"""
    features = feature_filter('currency')
    titletext = 'Spare Some Change?'
    features['npc'] = NPC.NPC(server)
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count']) > 1 and int(request.args['count']) <= 100:
        currencys = []
        for _ in xrange(int(request.args['count'])):
            currencys.append(Currency.Currency(server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=currencys, oneliner=currencys[0], titletext=titletext, generator='currency')
    else:
        currency = Currency.Currency(server, features)
        return render_template('oneliner.html', oneliner=currency, titletext=titletext, generator='currency')



@app.route('/currency_builder')
def currency_builder():
    """Build a a currency"""
    classname = 'currency'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################

@app.route('/jobposting')
def generatejobposting():
    """Generate a jobposting"""

    features = feature_filter('jobposting')
    titletext = 'Help Wanted!'
    features['npc'] = NPC.NPC(server)
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count']) > 1 and int(request.args['count']) <= 100:
        jobpostings = []
        for _ in xrange(int(request.args['count'])):
            jobpostings.append(JobPosting.JobPosting(server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=jobpostings, oneliner=jobpostings[0], titletext=titletext, generator='jobposting')
    else:
        jobposting = JobPosting.JobPosting(server, features)
        return render_template('oneliner.html', oneliner=jobposting, titletext=titletext, generator='jobposting')



@app.route('/jobposting_builder')
def jobposting_builder():
    """Build a a jobposting"""
    classname = 'jobposting'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################


@app.route('/event')
def generateevent():
    """Generate a event"""

    features = feature_filter('event')
    titletext = 'Look over there...'
    features['npc'] = NPC.NPC(server)
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count']) > 1 and int(request.args['count']) <= 100:
        events = []
        for _ in xrange(int(request.args['count'])):
            events.append(Event.Event(server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=events, oneliner=events[0], titletext=titletext, generator='event')
    else:
        event = Event.Event(server, features)
        return render_template('oneliner.html', oneliner=event, titletext=titletext, generator='event')

@app.route('/event_builder')
def event_builder():
    """Build a a event"""
    classname = 'event'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################


@app.route('/motivation')
def generatemotivation():
    """Generate a motivation"""
    features = feature_filter('motivation')
    titletext = 'I\'m Motivated...'
    features['npc'] = NPC.NPC(server)
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count']) > 1 and int(request.args['count']) <= 100:
        motivations = []
        for _ in xrange(int(request.args['count'])):
            motivations.append(Motivation.Motivation(server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=motivations, oneliner=motivations[0], titletext=titletext, generator='motivation')
    else:
        motivation = Motivation.Motivation(server, features)
        return render_template('oneliner.html', oneliner=motivation, titletext=titletext, generator='motivation')

@app.route('/motivation_builder')
def motivation_builder():
    """Build a a motivation"""
    classname = 'motivation'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################


@app.route('/gem')
def generategem():
    """Generate a gem"""
    features = feature_filter('gem')
    titletext = 'OOOH, Shiny...'
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count']) > 1 and int(request.args['count']) <= 100:
        gems = []
        for _ in xrange(int(request.args['count'])):
            gems.append(Gem.Gem(server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=gems, oneliner=gems[0], titletext=titletext, generator='gem')
    else:
        gem = Gem.Gem(server, features)
        return render_template('oneliner.html', oneliner=gem, titletext=titletext, generator='gem')

@app.route('/gem_builder')
def gem_builder():
    """Build a a gem"""
    classname = 'gem'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################

@app.route('/mundaneitem')
def generatemundaneitem():
    """Generate a mundaneitem"""

    features = feature_filter('mundaneitem')
    titletext = 'Look what I found!'
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count']) > 1 and int(request.args['count']) <= 100:
        mundaneitems = []
        for _ in xrange(int(request.args['count'])):
            mundaneitems.append(MundaneItem.MundaneItem(server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=mundaneitems, oneliner=mundaneitems[0], titletext=titletext, generator='mundaneitem')
    else:
        mundaneitem = MundaneItem.MundaneItem(server, features)
        return render_template('oneliner.html', oneliner=mundaneitem, titletext=titletext, generator='mundaneitem')

@app.route('/mundaneitem_builder')
def mundaneitem_builder():
    """Build a a mundaneitem"""
    classname = 'mundaneitem'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################


@app.route('/legend')
def generatelegend():
    """Generate a legend"""
    features = feature_filter('legend')
    titletext = 'Let me tell you a story...'
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count']) > 1 and int(request.args['count']) <= 100:
        legends = []
        for _ in xrange(int(request.args['count'])):
            legends.append(Legend.Legend(server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=legends, oneliner=legends[0], titletext=titletext, generator='legend')
    else:
        legend = Legend.Legend(server, features)
        return render_template('oneliner.html', oneliner=legend, titletext=titletext, generator='legend')

@app.route('/legend_builder')
def legend_builder():
    """Build a a legend"""
    classname = 'legend'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################

@app.route('/organization')
def GenerateOrganization():
    """Generate a simple organization"""
    features = feature_filter('organization')
    tempobj = Organization.Organization(server, features)
    return render_template('organization.html', tempobj=tempobj)


@app.route('/organization_builder')
def Organization_Builder():
    """Generate the basic data about a organization"""
    classname = 'organization'
    plist, pstring, pset = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)
    
    
#########################################################################

@app.route('/business')
def generatebusiness():
    """Generate a business"""
    features = feature_filter('business')
    business = Business.Business(server, features)
    return render_template('business.html', tempobj=business)


@app.route('/business_builder')
def business_builder():
    """Build a a business"""

    classname = 'business'
    plist, pstring, pset = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################

@app.route('/street')
def generatestreet():
    """Generate a street"""
    features = feature_filter('street')
    tempobj = Street.Street(server, features)
    return render_template('street.html', tempobj=tempobj)


@app.route('/street_builder')
def street_builder():
    """Build a a street"""

    classname = 'street'
    plist, pstring, pset = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)



#########################################################################

@app.route('/moon')
def generatemoon():
    """Generate a moon"""
    features = feature_filter('moon')
    moon = Moon.Moon(server, features)
    return render_template('moon.html', tempobj=moon)


@app.route('/moon_builder')
def moon_builder():
    """Build a a moon"""
    classname = 'moon'
    plist, pstring, pset = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)



#########################################################################

@app.route('/star')
def generatestar():
    """Generate a star"""
    features = feature_filter('star')
    star = Star.Star(server, features)
    return render_template('star.html', tempobj=star)


@app.route('/star_builder')
def star_builder():
    """Build a a star"""
    classname = 'star'
    plist, pstring, pset = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)



#########################################################################

@app.route('/continent')
def generatecontinent():
    """Generate a continent"""
    features = feature_filter('continent')
    continent = Continent.Continent(server, features)
    continent.add_countries()
    return render_template('continent.html', tempobj=continent)


@app.route('/continent_builder')
def continent_builder():
    """Build a a continent"""
    classname = 'continent'
    plist, pstring, pset = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################

@app.route('/region')
def generateregion():
    """Generate a region"""
    features = feature_filter('region')
    region = Region.Region(server, features)
#    region.add_cities()
#    region.add_locations()()
    return render_template('region.html', tempobj=region)


@app.route('/region_builder')
def region_builder():
    """Build a a region"""
    classname = 'region'
    plist, pstring, pset = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################

@app.route('/sect')
def generatesect():
    """Generate a sect"""

    features = feature_filter('sect')
    sect = Sect.Sect(server, features)
    return render_template('sect.html', tempobj=sect)


@app.route('/sect_builder')
def sect_builder():
    """Build a a sect"""
    classname = 'sect'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/govt')
def generategovt():
    """Generate a govt"""
    features = feature_filter('govt')
    govt = Govt.Govt(server, features)
    return render_template('govt.html', tempobj=govt)


@app.route('/govt_builder')
def govt_builder():
    """Build a a govt"""
    classname = 'govt'
    plist, pstring, pset = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)



#########################################################################

@app.route('/weather')
def generateweather():
    """Generate a weather"""
    features = feature_filter('weather')
    weather = Weather.Weather(server, features)
    return render_template('weather.html', tempobj=weather)


@app.route('/weather_builder')
def weather_builder():
    """Build a a weather"""
    classname = 'weather'
    plist, pstring, pset = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)



#########################################################################

@app.route('/wanted')
def generatewanted():
    """Generate a wanted"""
    features = feature_filter('wanted')
    wanted = Wanted.Wanted(server, features)
    return render_template('wanted.html', tempobj=wanted)


@app.route('/wanted_builder')
def wanted_builder():
    """Build a a wanted"""
    classname = 'wanted'
    plist, pstring, pset = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)



#########################################################################

@app.route('/geomorphdungeon')
def generategeomorphdungeon():
    """Generate a geomorphdungeon"""
    features = feature_filter('geomorphdungeon')
    geomorphdungeon = GeomorphDungeon.GeomorphDungeon(server, features)
    return render_template('geomorphdungeon.html', tempobj=geomorphdungeon, jsondata=geomorphdungeon.convert_to_json())

@app.route('/geomorphdungeon_builder')
def geomorphdungeon_builder():
    """Build a a geomorphdungeon"""
    classname = 'geomorphdungeon'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################

@app.route('/roguedungeon')
def generateroguedungeon():
    """Generate a dungeon"""
    features = feature_filter('roguedungeon')
    roguedungeon = RogueDungeon.RogueDungeon(server, features)
    return render_template('roguedungeon.html', tempobj=roguedungeon, jsondata=roguedungeon.convert_to_json())


@app.route('/roguedungeon_builder')
def roguedungeon_builder():
    """Build a a dungeon"""
    classname = 'roguedungeon'
    plist, pstring, pset = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################


@app.route('/country')
def generatecountry():
    """Generate a country"""
    features = feature_filter('country')
    country = Country.Country(server, features)
    country.add_regions()
    return render_template('country.html', tempobj=country)


@app.route('/country_builder')
def country_builder():
    """Build a a country"""
    classname = 'country'
    plist, pstring, pset = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################

@app.route('/cuisine')
def generatecuisine():
    """Generate a cuisine"""
    features = feature_filter('cuisine')
    features['region'] = Region.Region(server)
    titletext = 'What\'s for Dinner?'
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count']) > 1 and int(request.args['count']) <= 100:
        cuisines = []
        for _ in xrange(int(request.args['count'])):
            cuisines.append(Cuisine.Cuisine(server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=cuisines, oneliner=cuisines[0], titletext=titletext, generator='cuisine')
    else:
        cuisine = Cuisine.Cuisine(server, features)
        return render_template('oneliner.html', oneliner=cuisine, titletext=titletext, generator='cuisine')


@app.route('/cuisine_builder')
def cuisine_builder():
    """Build a a cuisine"""
    classname = 'cuisine'
    plist, pstring, pset = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################

@app.route('/deity')
def generatedeity():
    """Generate a deity"""

    features = feature_filter('deity')
    deity = Deity.Deity(server, features)
    return render_template('deity.html', tempobj=deity)

@app.route('/deity_builder')
def deity_builder():
    """Build a a deity"""
    classname = 'deity'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################

@app.route('/leader')
def generateleader():
    """Generate a leader"""

    features = feature_filter('leader')
    leader = Leader.Leader(server, features)
    return render_template('leader.html', tempobj=leader)

@app.route('/leader_builder')
def leader_builder():
    """Build a a leader"""
    classname = 'leader'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################

@app.route('/flag')
def generateflag():
    """Generate a flag"""

    features = feature_filter('flag')
    flag = Flag.Flag(server, features)
    return render_template('flag.html', tempobj=flag, flagjson=flag.tojson())

@app.route('/flag_builder')
def flag_builder():
    """Build a a flag"""
    classname = 'flag'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)






#########################################################################
#########################################################################
#########################################################################





def feature_filter(generator):
    """Turn the request string into a feature set."""
    app.seed = set_seed(request.args.get('seed'))

    genregex = re.compile('^'+generator+'_[a-z_]+$')
    genrollregex = re.compile('^'+generator+'_[a-z_]+_(roll|chance)$')

    app.logger.info('Request Seed: %i', app.seed)
    features = {'seed':app.seed, }
    for param in request.args:
        if genrollregex.match(param) and isvalidscore(request.args[param]):
            features[param] = int(request.args[param])
        elif genregex.match(param) and str(request.args[param]).isdigit():
            fieldname = re.sub(generator+'_', '', param)
            features[fieldname] = server.lrange(param, int(request.args[param]), int(request.args[param]))[0]
    return features

def builder_form_data(generator):
    """Turn the fields of a generator into fodder for the generic_builder"""
    plist = {}
    pstring = {}
    pset = {}
    for key in server.keys(generator+'_*'):
        fieldname = key.replace(generator+'_', '')
        if server.type(key) == 'list':
            plist[fieldname] = server.lrange(key, 0, -1)
        elif server.type(key) == 'string':
            pstring[fieldname] = server.get(key)
        elif server.type(key) == 'zset':
            result = server.zrangebyscore(key, 1, 100)
            pset[fieldname] = []
            for field in result:
                try:
                    pset[fieldname].append(json.loads(field))
                except ValueError:
                    raise ValueError("failed to parse %s field %s" % (key, field))
    return plist, pstring, pset

def isvalidscore(value):
    """Verify if a string is a valid score."""
    if value.isdigit() and int(value) >= 0 and int(value) <= 100:
        return True
    else:
        return False

@app.errorhandler(404)
def page_not_found(error):
    """Return a custom 404 error."""
    print " ======================="
    print "Exception:", error
    time = str(datetime.datetime.now())
    return render_template("400.html", request=request, time=time), 404

@app.errorhandler(500)
def page_borked(error):
    """Return a custom 500 error. Only hit when debugging is off."""
    print " ======================="
    print "problem with ", request.url
    time = str(datetime.datetime.now())
    print "on seed", app.seed, "at", time
    print "Exception:", error.args[0]
    traceback.print_exc()

    return render_template("500.html", seed=app.seed, request=request, e=error, time=time), 500

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
    #FIXME is this correct? or is it count-based?
    return Filters.select_plural_adj(adj, subject)

if __name__ == '__main__':

    app.debug = True
    app.run()


