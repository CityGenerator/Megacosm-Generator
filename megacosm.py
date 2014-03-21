"""`main` is the top level module for this application."""

# Import the stuffs!
from flask import Flask, send_file, render_template, request, url_for
from generators import Planet, NPC, MagicItem, Deity, Bond, Rumor, Cuisine, Continent, Country, Sect, Legend, Business, Star, Moon, Currency, Misfire, Region
from generators import Wanted
from generators import Resource
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
    return render_template('magicitem_'+kind+'.html',magicitem=magicitem) 

@app.route('/magicitem_builder')
def MagicItem_Builder():
    """Generate an NPC"""
    
    paramlist,paramstring,paramset=builder_form_data('magicitem')

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name='magicitem') 
    
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

    npc=NPC.NPC(server,npcfeatures)
    return render_template('npc.html',npc=npc) 

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
    paramlist,paramstring,paramset=builder_form_data('planet')

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name='planet') 


@app.route('/planet')
def GeneratePlanet():
    """Generate the basic data about a planet"""
    features=feature_filter('planet')
    planet=Planet.Planet(server,features)
    planet.add_continents()
    return render_template('planet.html', planet=planet )


#########################################################################

@app.route('/resource')
def GenerateResource():
    """Generate a simple resource"""
    features=feature_filter('resource')
    resource=Resource.Resource(server,features)
    return render_template('oneliner.html', oneliner=resource,titletext='At your disposal...', generator='resource' )

@app.route('/resource_builder')
def Resource_Builder():
    """Generate the basic data about a resource"""
    paramlist,paramstring,paramset=builder_form_data('resource')

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name='resource') 
    
#########################################################################

@app.route('/rumor')
def GenerateRumor():
    """Generate a simple rumor"""
    features=feature_filter('rumor')
    rumor=Rumor.Rumor(server,features)
    return render_template('oneliner.html', oneliner=rumor,titletext='Did you hear?', generator='rumor' )

@app.route('/rumor_builder')
def Rumor_Builder():
    """Generate the basic data about a rumor"""
    paramlist,paramstring,paramset=builder_form_data('rumor')

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name='rumor') 
    
#########################################################################

@app.route('/misfire')
def GenerateMisfire():
    """Generate a simple misfire"""
    features=feature_filter('misfire')
    misfire=Misfire.Misfire(server,features)
    return render_template('oneliner.html', oneliner=misfire,titletext='My spell misfired!', generator='misfire' )

@app.route('/misfire_builder')
def Misfire_Builder():
    """Generate the basic data about a misfire"""
    paramlist,paramstring,paramset=builder_form_data('misfire')

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name='misfire') 
    
#########################################################################


@app.route('/currency')
def GenerateCurrency():
    """Generate a simple currency"""
    features=feature_filter('currency')
    currency=Currency.Currency(server,features)
    return render_template('oneliner.html', oneliner=currency ,titletext='Spare Some Change? ', generator='currency' )

@app.route('/currency_builder')
def Currency_Builder():
    """Generate the basic data about a currency"""
    paramlist,paramstring,paramset=builder_form_data('currency')

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name='currency') 
    
#########################################################################


@app.route('/legend')
def GenerateLegend():
    """Generate a simple legend"""
    features=feature_filter('legend')
    legend=Legend.Legend(server,features)
    return render_template('oneliner.html', oneliner=legend ,titletext='Let me tell you a story...', generator='legend' )

@app.route('/legend_builder')
def Legend_Builder():
    """Generate the basic data about a legend"""
    paramlist,paramstring,paramset=builder_form_data('legend')

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name='legend') 
    
#########################################################################

@app.route('/business')
def GenerateBusiness():
    """Generate a simple business"""
    features=feature_filter('business')
    business=Business.Business(server,features)
    return render_template('business.html', business=business )


@app.route('/business_builder')
def Business_Builder():
    """Generate the basic data about a business"""

    paramlist,paramstring,paramset=builder_form_data('business')
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name='business') 
    
    
#########################################################################

@app.route('/moon')
def GenerateMoon():
    """Generate a simple moon"""
    features=feature_filter('moon')
    moon=Moon.Moon(server,features)
    return render_template('moon.html', moon=moon )


@app.route('/moon_builder')
def Moon_Builder():
    """Generate the basic data about a moon"""
    paramlist,paramstring,paramset=builder_form_data('moon')
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name='moon') 
    
    
    
#########################################################################

@app.route('/star')
def GenerateStar():
    """Generate a simple star"""
    features=feature_filter('star')
    star=Star.Star(server,features)
    return render_template('star.html', star=star )


@app.route('/star_builder')
def Star_Builder():
    """Generate the basic data about a star"""
    paramlist,paramstring,paramset=builder_form_data('star')
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name='star') 
    
    
    
#########################################################################

@app.route('/continent')
def GenerateContinent():
    """Generate a simple continent"""
    features=feature_filter('continent')
    continent=Continent.Continent(server,features)
    continent.add_countries()
    return render_template('continent.html', continent=continent )


@app.route('/continent_builder')
def Continent_Builder():
    """Generate the basic data about a continent"""
    paramlist,paramstring,paramset=builder_form_data('continent')
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name='continent') 
    
#########################################################################

@app.route('/region')
def GenerateRegion():
    """Generate a simple region"""
    features=feature_filter('region')
    region=Region.Region(server,features)
#    region.add_cities()
#    region.add_locations()()
    return render_template('region.html', region=region )


@app.route('/region_builder')
def Region_Builder():
    """Generate the basic data about a region"""
    paramlist,paramstring,paramset=builder_form_data('region')
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name='region') 
    
#########################################################################

@app.route('/sect')
def GenerateSect():
    """Generate a simple sect"""

    features=feature_filter('sect')
    sect=Sect.Sect(server,features)
    return render_template('sect.html', sect=sect, name='sect' )


@app.route('/sect_builder')
def Sect_Builder():
    """Generate the basic data about a sect"""
    paramlist,paramstring,paramset=builder_form_data('sect')
    result= server.zrange('portfolio_domain',0,-1)

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name='sect') 


    
#########################################################################

@app.route('/wanted')
def GenerateWanted():
    """Generate a simple wanted"""
    features=feature_filter('wanted')
    wanted=Wanted.Wanted(server,features)
    return render_template('wanted.html', wanted=wanted )


@app.route('/wanted_builder')
def Wanted_Builder():
    """Generate the basic data about a wanted"""
    paramlist,paramstring,paramset=builder_form_data('wanted')
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name='wanted') 


#########################################################################

@app.route('/country')
def GenerateCountry():
    """Generate a simple country"""
    features=feature_filter('country')
    country=Country.Country(server,features)
    country.add_regions()
    return render_template('country.html', country=country )


@app.route('/country_builder')
def Country_Builder():
    """Generate the basic data about a country"""
    paramlist,paramstring,paramset=builder_form_data('country')
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name='country') 


#########################################################################

@app.route('/cuisine')
def GenerateCuisine():
    """Generate a simple cuisine"""
    features=feature_filter('cuisine')
    cuisine=Cuisine.Cuisine(server,features)
    return render_template('cuisine.html', cuisine=cuisine )


@app.route('/cuisine_builder')
def Cuisine_Builder():
    """Generate the basic data about a cuisine"""
    paramlist,paramstring,paramset=builder_form_data('cuisine')
    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name='cuisine') 
    
#########################################################################

@app.route('/deity')
def GenerateDeity():
    """Generate a simple deity"""

    features=feature_filter('deity')
    deity=Deity.Deity(server,features)
    return render_template('deity.html', deity=deity, name='deity' )

@app.route('/deity_builder')
def Deity_Builder():
    """Generate the basic data about a deity"""
    paramlist,paramstring,paramset=builder_form_data('deity')
    result= server.zrange('portfolio_domain',0,-1)

    return render_template('generic_builder.html',paramlist=paramlist,paramstring=paramstring, paramset=paramset, name='deity') 




#########################################################################
#########################################################################
#########################################################################





def feature_filter(generator):
    seed=set_seed( request.args.get('seed') )

    print "MAH SEED:",seed, request.args.get('seed') 
    features={'seed':seed,}
    for param in request.args :
        if re.match('^'+generator+'_[a-z_]+_(roll|chance)$',param) and int(request.args[param])>=0 and int(request.args[param])<=100 :
            features[param]=int(request.args[param])
        elif re.match('^'+generator+'_[a-z_]+$',param) and re.match('^\d{1,10000}$',request.args[param]):
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



if __name__ == '__main__':
    app.debug = True
    app.run()




