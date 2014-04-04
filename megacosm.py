"""`main` is the top level module for this application."""

# Import the stuffs!
from flask import Flask, send_file, render_template, request, url_for
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
from util.Seeds import *
from util import Filters
import random
import redis
import ConfigParser
import pprint
import json
import os
import sys
import inflect
import re
from pprint import pprint

p = inflect.engine()

config = ConfigParser.RawConfigParser()
config.read( 'data/config.ini')

url = config.get('redis', 'url')
server=redis.from_url(url)

# This thing here.. does stuff.
app = Flask(__name__)

#########################################################################

@app.route('/')
def indexpage():
    """This is the first page anyone sees."""
    return render_template('index.html') 

#########################################################################

@app.route('/magicitem')
def GenerateMagicItem():
    """Generate a MagicItem"""

    features=feature_filter('magicitem')
    magicitem=MagicItem.MagicItem(server,features)

    kind= magicitem.kind
    return render_template('magicitem_'+kind+'.html',tempobj=magicitem) 

@app.route('/magicitem_builder')
def MagicItem_Builder():
    """Generate an NPC"""
    
    classname='magicitem'
    paramlist,paramstring,paramset=builder_form_data(classname)

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
#########################################################################


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
        if re.match('^npc_[a-z_]+_roll$',param) and int(request.args[param])>=0 and int(request.args[param])<=100 :
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

    npcfeatures['deity']=Deity.Deity(server)
    npc=NPC.NPC(server,npcfeatures)
    return render_template('npc.html',tempobj=npc) 

@app.route('/npc_builder')
def NPC_Builder():
    """Generate an NPC"""

    stats=server.lrange('stat_npc',0,-1)
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

#########################################################################

@app.route('/bond')
def GenerateBond():
    """Generate a simple bond"""
    seed=set_seed( request.args.get('seed') )


    bondfeatures={'seed':seed,}

    for param in request.args :
        if re.match('^bond_[a-z_]+_roll$',param) and int(request.args[param])>=0 and int(request.args[param])<=100 :
            bondfeatures[param]=int(request.args[param])
        elif re.match('^bond_template_id$',param)  and int(request.args[param])>=0 and int(request.args[param]) < server.llen('bond_template'):
            bondfeatures['template']=server.lrange('bond_template', int(request.args[param]), int(request.args[param]) )[0]
        elif re.match('^bond_when_id$',param)  and int(request.args[param])>=0 and int(request.args[param]) < server.llen('bond_when'):
            bondfeatures['when']=server.lrange('bond_when', int(request.args[param]), int(request.args[param]) )[0]
        elif re.match('^bond_[a-zA-Z]*$',param)  and re.match('^[a-zA-Z\']+$', request.args[param]):
            fieldname=param.split('_',2)[1]
            bondfeatures[fieldname]=request.args[param]

    bond=Bond.Bond(server,bondfeatures)

    return render_template('oneliner.html', oneliner=bond,titletext='The Ties that Bind Us... ', generator='bond' )

@app.route('/bond_builder')
def Bond_Builder():
    """Generate the basic data about a bond"""

    statinfo={}
    for stat in ['when', 'template']:
        statinfo[stat]=[]
        for statstring in server.lrange('bond_'+stat,0,-1):
            statinfo[stat].append(statstring)
    
    return render_template('bond_builder.html',statinfo=statinfo) 

#########################################################################
@app.route('/planet_builder')
def Planet_Builder():
    """Generate the basic data about a planet"""
    classname='planet'
    paramlist,paramstring,paramset=builder_form_data(classname)

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)


@app.route('/planet')
def GeneratePlanet():
    """Generate the basic data about a planet"""
    features=feature_filter('planet')
    planet=Planet.Planet(server,features)
    planet.add_continents()
    return render_template('planet.html', tempobj=planet )


#########################################################################

@app.route('/resource')
def GenerateResource():
    """Generate a simple resource"""

    features=feature_filter('resource')
    titletext='At Your Disposal...'
    features['npc']=NPC.NPC(server)
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count'])>1 and int(request.args['count'])<=100:
        resources=[]
        for item in xrange(int(request.args['count'])):
            resources.append(Resource.Resource(server,features))
            features['seed']=set_seed( )
        return render_template('oneliner.html', oneliners=resources, oneliner=resources[0] ,titletext=titletext, generator='resource' )
    else:
        resource=Resource.Resource(server,features)
        return render_template('oneliner.html', oneliner=resource ,titletext=titletext, generator='resource' )



@app.route('/resource_builder')
def Resource_Builder():
    """Generate the basic data about a resource"""
    classname='resource'
    paramlist,paramstring,paramset=builder_form_data(classname)

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
#########################################################################

@app.route('/rumor')
def GenerateRumor():
    """Generate a simple rumor"""
    features=feature_filter('rumor')
    titletext='Did You Hear?'
    features['npc']=NPC.NPC(server)
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count'])>1 and int(request.args['count'])<=100:
        rumors=[]
        for item in xrange(int(request.args['count'])):
            rumors.append(Rumor.Rumor(server,features))
            features['seed']=set_seed( )
        return render_template('oneliner.html', oneliners=rumors, oneliner=rumors[0] ,titletext=titletext, generator='rumor' )
    else:
        rumor=Rumor.Rumor(server,features)
        return render_template('oneliner.html', oneliner=rumor ,titletext=titletext, generator='rumor' )



@app.route('/rumor_builder')
def Rumor_Builder():
    """Generate the basic data about a rumor"""
    classname='rumor'
    paramlist,paramstring,paramset=builder_form_data(classname)

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
#########################################################################

@app.route('/misfire')
def GenerateMisfire():
    """Generate a simple misfire"""

    features=feature_filter('misfire')
    titletext='My Spell Misfired!'
    features['npc']=NPC.NPC(server)
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count'])>1 and int(request.args['count'])<=100:
        misfires=[]
        for item in xrange(int(request.args['count'])):
            misfires.append(Misfire.Misfire(server,features))
            features['seed']=set_seed( )
        return render_template('oneliner.html', oneliners=misfires, oneliner=misfires[0] ,titletext=titletext, generator='misfire' )
    else:
        misfire=Misfire.Misfire(server,features)
        return render_template('oneliner.html', oneliner=misfire ,titletext=titletext, generator='misfire' )


@app.route('/misfire_builder')
def Misfire_Builder():
    """Generate the basic data about a misfire"""
    classname='misfire'
    paramlist,paramstring,paramset=builder_form_data(classname)

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
#########################################################################


@app.route('/currency')
def GenerateCurrency():
    """Generate a simple currency"""
    features=feature_filter('currency')
    titletext='Space Some Change?'
    features['npc']=NPC.NPC(server)
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count'])>1 and int(request.args['count'])<=100:
        currencys=[]
        for item in xrange(int(request.args['count'])):
            currencys.append(Currency.Currency(server,features))
            features['seed']=set_seed( )
        return render_template('oneliner.html', oneliners=currencys, oneliner=currencys[0] ,titletext=titletext, generator='currency' )
    else:
        currency=Currency.Currency(server,features)
        return render_template('oneliner.html', oneliner=currency ,titletext=titletext, generator='currency' )



@app.route('/currency_builder')
def Currency_Builder():
    """Generate the basic data about a currency"""
    classname='currency'
    paramlist,paramstring,paramset=builder_form_data(classname)

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
#########################################################################

@app.route('/jobposting')
def GenerateJobPosting():
    """Generate a simple jobposting"""

    features=feature_filter('jobposting')
    titletext='Help Wanted!'
    features['npc']=NPC.NPC(server)
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count'])>1 and int(request.args['count'])<=100:
        jobpostings=[]
        for item in xrange(int(request.args['count'])):
            jobpostings.append(JobPosting.JobPosting(server,features))
            features['seed']=set_seed( )
        return render_template('oneliner.html', oneliners=jobpostings, oneliner=jobpostings[0] ,titletext=titletext, generator='jobposting' )
    else:
        jobposting=JobPosting.JobPosting(server,features)
        return render_template('oneliner.html', oneliner=jobposting ,titletext=titletext, generator='jobposting' )



@app.route('/jobposting_builder')
def JobPosting_Builder():
    """Generate the basic data about a jobposting"""
    classname='jobposting'
    paramlist,paramstring,paramset=builder_form_data(classname)

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
    
#########################################################################


@app.route('/event')
def GenerateEvent():
    """Generate a simple event"""

    features=feature_filter('event')
    titletext='Look over there...'
    features['npc']=NPC.NPC(server)
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count'])>1 and int(request.args['count'])<=100:
        events=[]
        for item in xrange(int(request.args['count'])):
            events.append(Event.Event(server,features))
            features['seed']=set_seed( )
        return render_template('oneliner.html', oneliners=events, oneliner=events[0] ,titletext=titletext, generator='event' )
    else:
        event=Event.Event(server,features)
        return render_template('oneliner.html', oneliner=event ,titletext=titletext, generator='event' )

@app.route('/event_builder')
def Event_Builder():
    """Generate the basic data about a event"""
    classname='event'
    paramlist,paramstring,paramset=builder_form_data(classname)

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
    
#########################################################################


@app.route('/motivation')
def GenerateMotivation():
    """Generate a simple motivation"""
    features=feature_filter('motivation')
    titletext='I\'m Motivated...'
    features['npc']=NPC.NPC(server)
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count'])>1 and int(request.args['count'])<=100:
        motivations=[]
        for item in xrange(int(request.args['count'])):
            motivations.append(Motivation.Motivation(server,features))
            features['seed']=set_seed( )
        return render_template('oneliner.html', oneliners=motivations, oneliner=motivations[0] ,titletext=titletext, generator='motivation' )
    else:
        motivation=Motivation.Motivation(server,features)
        return render_template('oneliner.html', oneliner=motivation ,titletext=titletext, generator='motivation' )

@app.route('/motivation_builder')
def Motivation_Builder():
    """Generate the basic data about a motivation"""
    classname='motivation'
    paramlist,paramstring,paramset=builder_form_data(classname)

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
#########################################################################


@app.route('/gem')
def GenerateGem():
    """Generate a simple gem"""
    features=feature_filter('gem')
    titletext='OOOH, Shiny...'
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count'])>1 and int(request.args['count'])<=100:
        gems=[]
        for item in xrange(int(request.args['count'])):
            gems.append(Gem.Gem(server,features))
            features['seed']=set_seed( )
        return render_template('oneliner.html', oneliners=gems, oneliner=gems[0] ,titletext=titletext, generator='gem' )
    else:
        gem=Gem.Gem(server,features)
        return render_template('oneliner.html', oneliner=gem ,titletext=titletext, generator='gem' )

@app.route('/gem_builder')
def Gem_Builder():
    """Generate the basic data about a gem"""
    classname='gem'
    paramlist,paramstring,paramset=builder_form_data(classname)

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
#########################################################################

@app.route('/mundaneitem')
def GenerateMundaneItem():
    """Generate a simple mundaneitem"""

    features=feature_filter('mundaneitem')
    titletext='Look what I found!'
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count'])>1 and int(request.args['count'])<=100:
        mundaneitems=[]
        for item in xrange(int(request.args['count'])):
            mundaneitems.append(MundaneItem.MundaneItem(server,features))
            features['seed']=set_seed( )
        return render_template('oneliner.html', oneliners=mundaneitems, oneliner=mundaneitems[0] ,titletext=titletext, generator='mundaneitem' )
    else:
        mundaneitem=MundaneItem.MundaneItem(server,features)
        return render_template('oneliner.html', oneliner=mundaneitem ,titletext=titletext, generator='mundaneitem' )

@app.route('/mundaneitem_builder')
def MundaneItem_Builder():
    """Generate the basic data about a mundaneitem"""
    classname='mundaneitem'
    paramlist,paramstring,paramset=builder_form_data(classname)

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
#########################################################################


@app.route('/legend')
def GenerateLegend():
    """Generate a simple legend"""
    features=feature_filter('legend')
    titletext='Let me tell you a story...'
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count'])>1 and int(request.args['count'])<=100:
        legends=[]
        for item in xrange(int(request.args['count'])):
            legends.append(Legend.Legend(server,features))
            features['seed']=set_seed( )
        return render_template('oneliner.html', oneliners=legends, oneliner=legends[0] ,titletext=titletext, generator='legend' )
    else:
        legend=Legend.Legend(server,features)
        return render_template('oneliner.html', oneliner=legend ,titletext=titletext, generator='legend' )

@app.route('/legend_builder')
def Legend_Builder():
    """Generate the basic data about a legend"""
    classname='legend'
    paramlist,paramstring,paramset=builder_form_data(classname)

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
#########################################################################

@app.route('/business')
def GenerateBusiness():
    """Generate a simple business"""
    features=feature_filter('business')
    business=Business.Business(server,features)
    return render_template('business.html', tempobj=business )


@app.route('/business_builder')
def Business_Builder():
    """Generate the basic data about a business"""

    classname='business'
    paramlist,paramstring,paramset=builder_form_data(classname)
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
#########################################################################

@app.route('/street')
def GenerateStreet():
    """Generate a simple street"""
    features=feature_filter('street')
    tempobj=Street.Street(server,features)
    return render_template('street.html', tempobj=tempobj )


@app.route('/street_builder')
def Street_Builder():
    """Generate the basic data about a street"""

    classname='street'
    paramlist,paramstring,paramset=builder_form_data(classname)
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
    
    
#########################################################################

@app.route('/moon')
def GenerateMoon():
    """Generate a simple moon"""
    features=feature_filter('moon')
    moon=Moon.Moon(server,features)
    return render_template('moon.html', tempobj=moon )


@app.route('/moon_builder')
def Moon_Builder():
    """Generate the basic data about a moon"""
    classname='moon'
    paramlist,paramstring,paramset=builder_form_data(classname)
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
    
    
#########################################################################

@app.route('/star')
def GenerateStar():
    """Generate a simple star"""
    features=feature_filter('star')
    star=Star.Star(server,features)
    return render_template('star.html', tempobj=star )


@app.route('/star_builder')
def Star_Builder():
    """Generate the basic data about a star"""
    classname='star'
    paramlist,paramstring,paramset=builder_form_data(classname)
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
    
    
#########################################################################

@app.route('/continent')
def GenerateContinent():
    """Generate a simple continent"""
    features=feature_filter('continent')
    continent=Continent.Continent(server,features)
    continent.add_countries()
    return render_template('continent.html', tempobj=continent )


@app.route('/continent_builder')
def Continent_Builder():
    """Generate the basic data about a continent"""
    classname='continent'
    paramlist,paramstring,paramset=builder_form_data(classname)
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
#########################################################################

@app.route('/region')
def GenerateRegion():
    """Generate a simple region"""
    features=feature_filter('region')
    region=Region.Region(server,features)
#    region.add_cities()
#    region.add_locations()()
    return render_template('region.html', tempobj=region )


@app.route('/region_builder')
def Region_Builder():
    """Generate the basic data about a region"""
    classname='region'
    paramlist,paramstring,paramset=builder_form_data(classname)
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
#########################################################################

@app.route('/sect')
def GenerateSect():
    """Generate a simple sect"""

    features=feature_filter('sect')
    sect=Sect.Sect(server,features)
    return render_template('sect.html', tempobj=sect )


@app.route('/sect_builder')
def Sect_Builder():
    """Generate the basic data about a sect"""
    classname='sect'
    paramlist,paramstring,paramset=builder_form_data(classname)
    result= server.zrange('portfolio_domain',0,-1)

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)

    
#########################################################################

@app.route('/govt')
def GenerateGovt():
    """Generate a simple govt"""
    features=feature_filter('govt')
    govt=Govt.Govt(server,features)
    return render_template('govt.html', tempobj=govt )


@app.route('/govt_builder')
def Govt_Builder():
    """Generate the basic data about a govt"""
    classname='govt'
    paramlist,paramstring,paramset=builder_form_data(classname)
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)


    
#########################################################################

@app.route('/weather')
def GenerateWeather():
    """Generate a simple weather"""
    features=feature_filter('weather')
    weather=Weather.Weather(server,features)
    return render_template('weather.html', tempobj=weather )


@app.route('/weather_builder')
def Weather_Builder():
    """Generate the basic data about a weather"""
    classname='weather'
    paramlist,paramstring,paramset=builder_form_data(classname)
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)


    
#########################################################################

@app.route('/wanted')
def GenerateWanted():
    """Generate a simple wanted"""
    features=feature_filter('wanted')
    wanted=Wanted.Wanted(server,features)
    return render_template('wanted.html', tempobj=wanted )


@app.route('/wanted_builder')
def Wanted_Builder():
    """Generate the basic data about a wanted"""
    classname='wanted'
    paramlist,paramstring,paramset=builder_form_data(classname)
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)



#########################################################################

@app.route('/geomorphdungeon')
def GenerateGeomorphDungeon():
    """Generate a simple geomorphdungeon"""
    features=feature_filter('geomorphdungeon')
    geomorphdungeon=GeomorphDungeon.GeomorphDungeon(server,features)
    return render_template('geomorphdungeon.html', tempobj=geomorphdungeon,jsondata=geomorphdungeon.convert_to_json() )

@app.route('/geomorphdungeon_builder')
def GeomorphDungeon_Builder():
    """Generate the basic data about a geomorphdungeon"""
    classname='geomorphdungeon'
    paramlist,paramstring,paramset=builder_form_data(classname)

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
#########################################################################

@app.route('/roguedungeon')
def GenerateRogueDungeon():
    """Generate a simple dungeon"""
    features=feature_filter('roguedungeon')
    roguedungeon=RogueDungeon.RogueDungeon(server,features)
    return render_template('roguedungeon.html', tempobj=roguedungeon,jsondata=roguedungeon.convert_to_json() )


@app.route('/roguedungeon_builder')
def RogueDungeon_Builder():
    """Generate the basic data about a dungeon"""
    classname='roguedungeon'
    paramlist,paramstring,paramset=builder_form_data(classname)
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)


#########################################################################


@app.route('/country')
def GenerateCountry():
    """Generate a simple country"""
    features=feature_filter('country')
    country=Country.Country(server,features)
    country.add_regions()
    return render_template('country.html', tempobj=country )


@app.route('/country_builder')
def Country_Builder():
    """Generate the basic data about a country"""
    classname='country'
    paramlist,paramstring,paramset=builder_form_data(classname)
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)


#########################################################################

@app.route('/cuisine')
def GenerateCuisine():
    """Generate a simple cuisine"""
    features=feature_filter('cuisine')
    features['region']=Region.Region(server)
    titletext='What\'s for Dinner?'
    if 'count' in request.args and request.args['count'].isdigit() and int(request.args['count'])>1 and int(request.args['count'])<=100:
        cuisines=[]
        for item in xrange(int(request.args['count'])):
            cuisines.append(Cuisine.Cuisine(server,features))
            features['seed']=set_seed( )
        return render_template('oneliner.html', oneliners=cuisines, oneliner=cuisines[0] ,titletext=titletext, generator='cuisine' )
    else:
        cuisine=Cuisine.Cuisine(server,features)
        return render_template('oneliner.html', oneliner=cuisine ,titletext=titletext, generator='cuisine' )


@app.route('/cuisine_builder')
def Cuisine_Builder():
    """Generate the basic data about a cuisine"""
    classname='cuisine'
    paramlist,paramstring,paramset=builder_form_data(classname)
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)
    
#########################################################################

@app.route('/deity')
def GenerateDeity():
    """Generate a simple deity"""

    features=feature_filter('deity')
    deity=Deity.Deity(server,features)
    return render_template('deity.html', tempobj=deity )

@app.route('/deity_builder')
def Deity_Builder():
    """Generate the basic data about a deity"""
    classname='deity'
    paramlist,paramstring,paramset=builder_form_data(classname)
    result= server.zrange('portfolio_domain',0,-1)

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name=classname)




#########################################################################
#########################################################################
#########################################################################





def feature_filter(generator):
    seed=set_seed( request.args.get('seed') )

    seedregex=re.compile('^\d{1,10000000}$')
    genregex=re.compile('^'+generator+'_[a-z_]+$')
    genrollregex=re.compile('^'+generator+'_[a-z_]+_(roll|chance)$')

    print "MAH SEED:",seed, request.args.get('seed') 
    features={'seed':seed,}
    for param in request.args :
        if genrollregex.match(param) and int(request.args[param])>=0 and int(request.args[param])<=100 :
            features[param]=int(request.args[param])
        elif genregex.match(param) and seedregex.match(request.args[param]):
            fieldname= re.sub(generator+'_','', param)
            features[fieldname]=server.lrange(param, int(request.args[param]), int(request.args[param]) )[0]
    return features

def builder_form_data(generator):
    paramlist={}
    paramstring={}
    paramset={}
    for key in server.keys(generator+'_*'):
        fieldname=key.replace(generator+'_','')
        if server.type(key) == 'list' :
            paramlist[fieldname]=server.lrange(key,0,-1)
        elif server.type(key) == 'string' :
            paramstring[fieldname]=server.get(key)
        elif server.type(key) == 'zset' :
            result= server.zrangebyscore(key,1,100)
            paramset[fieldname]=[]
            for field in result:
                try:
                    paramset[fieldname].append( json.loads(field))
                except ValueError as e:
                    raise Exception ("failed to parse",key,"field", field)
    return paramlist,paramstring,paramset







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
    return Filters.select_article(s)

@app.template_filter('pluralize')
def select_pluralize(s,n):
    return Filters.select_pluralize(s,n)

@app.template_filter('conjunction')
def select_conjunction(wordlist):
    return Filters.select_conjunction(wordlist)


@app.template_filter('plural_verb')
def select_plural_verb(verb,subject ):
    return Filters.select_plural_verb(verb,subject )

@app.template_filter('plural_adj')
def select_plural_adj(adj,subject ):
    return Filters.select_plural_adj(adj,subject )


if __name__ == '__main__':
    app.debug = True
    app.run()




