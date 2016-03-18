from flask import render_template, request
from megacosm.generators import Artwork
from megacosm.generators import Bond
from megacosm.generators import Curse
from megacosm.generators import Resource
from megacosm.generators import Rumor
from megacosm.generators import Flaw
from megacosm.generators import Misfire
from megacosm.generators import Currency
from megacosm.generators import Event
from megacosm.generators import Gem
from megacosm.generators import Grafitti
from megacosm.generators import Motivation
from megacosm.generators import Phobia
from megacosm.generators import JobPosting
from megacosm.generators import Legend
from megacosm.generators import MundaneItem
from megacosm.generators import Cuisine
from megacosm.generators import NPC
from megacosm.generators import Region
from megacosm.generators import Drink

from megacosm.util.Seeds import set_seed

from megacosm import app, feature_filter, builder_form_data

#########################################################################

@app.route('/drink')
def generatedrink():
    """Generate a drink"""

    features = feature_filter('drink')
    features['region'] = Region(app.server)
    titletext = "What's on tap today?"
    if ('count' in request.args and
            request.args['count'].isdigit() and
            int(request.args['count']) > 1 and
            int(request.args['count']) <= 100):
        drinks = []
        for _ in xrange(int(request.args['count'])):
            drinks.append(Drink(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=drinks,
                               oneliner=drinks[0], titletext=titletext, generator='drink')
    else:
        drinks = Drink(app.server, features)
        return render_template('oneliner.html', oneliner=drinks, titletext=titletext, generator='drink')

@app.route('/drink_builder')
def drink_builder():
    """Build a drink"""
    classname = 'drink'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################
def valid_count(count):
    if ( count.isdigit() and
            int(count) > 1 and
            int(count) <= 100):
        return True
    else:
        return False

#########################################################################


@app.route('/artwork')
def generateartwork():
    """Generate a artwork"""
    features = feature_filter('artwork')
    titletext = 'A Work of Art...'
    if ('count' in request.args and valid_count(request.args['count'])):
        artworks = []
        for _ in xrange(int(request.args['count'])):
            artworks.append(Artwork(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=artworks,
                               oneliner=artworks[0], titletext=titletext, generator='artwork')
    else:
        artwork = Artwork(app.server, features)
        return render_template('oneliner.html', oneliner=artwork, titletext=titletext, generator='artwork')


@app.route('/artwork_builder')
def artwork_builder():
    """Build a a artwork"""
    classname = 'artwork'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################


@app.route('/bond')
def generatebond():
    """Generate a bond"""

    features = feature_filter('bond')
    titletext = 'The Ties that Bind Us...'
    features['npc'] = NPC(app.server, {})
    if ('count' in request.args and valid_count(request.args['count'])):
        bonds = []
        for _ in xrange(int(request.args['count'])):
            bonds.append(Bond(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=bonds,
                               oneliner=bonds[0], titletext=titletext, generator='bond')
    else:
        bond = Bond(app.server, features)
        return render_template('oneliner.html', oneliner=bond, titletext=titletext, generator='bond')


@app.route('/bond_builder')
def bond_builder():
    """Build a bond"""

    statinfo = {}
    for stat in ['when', 'template']:
        statinfo[stat] = []
        for statstring in app.server.lrange('bond_'+stat, 0, -1):
            statinfo[stat].append(statstring)

    return render_template('bond_builder.html', statinfo=statinfo)

#########################################################################


@app.route('/curse')
def generatecurse():
    """Generate a curse"""

    features = feature_filter('curse')
    titletext = 'Unforseen Consequences...'
    if ('count' in request.args and valid_count(request.args['count'])):
        curses = []
        for _ in xrange(int(request.args['count'])):
            curses.append(Curse(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=curses,
                               oneliner=curses[0], titletext=titletext, generator='curse')
    else:
        curse = Curse(app.server, features)
        return render_template('oneliner.html', oneliner=curse, titletext=titletext, generator='curse')


@app.route('/curse_builder')
def curse_builder():
    """Build a a curse"""
    classname = 'curse'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)
#########################################################################




@app.route('/resource')
def generateresource():
    """Generate a resource"""

    features = feature_filter('resource')
    titletext = 'At Your Disposal...'
    features['npc'] = NPC(app.server)
    if ('count' in request.args and valid_count(request.args['count'])):
        resources = []
        for _ in xrange(int(request.args['count'])):
            resources.append(Resource(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=resources,
                               oneliner=resources[0], titletext=titletext, generator='resource')
    else:
        resource = Resource(app.server, features)
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
    if ('count' in request.args and
            request.args['count'].isdigit() and
            int(request.args['count']) > 1 and
            int(request.args['count']) <= 100):
        artworks = []
        for _ in xrange(int(request.args['count'])):
            artworks.append(Artwork(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=artworks,
                               oneliner=artworks[0], titletext=titletext, generator='artwork')
    else:
        artwork = Artwork(app.server, features)
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
    features['npc'] = NPC(app.server)
    if ('count' in request.args and valid_count(request.args['count'])):
        rumors = []
        for _ in xrange(int(request.args['count'])):
            rumors.append(Rumor(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=rumors,
                               oneliner=rumors[0], titletext=titletext, generator='rumor')
    else:
        rumor = Rumor(app.server, features)
        return render_template('oneliner.html', oneliner=rumor, titletext=titletext, generator='rumor')


@app.route('/rumor_builder')
def rumor_builder():
    """Build a a rumor"""
    classname = 'rumor'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################


@app.route('/grafitti')
def generategrafitti():
    """Generate a grafitti"""

    features = feature_filter('grafitti')
    titletext = 'Scrawled on a Nearby Wall...'
    features['npc'] = NPC(app.server, {})
    if ('count' in request.args and valid_count(request.args['count'])):
        grafittis = []
        for _ in xrange(int(request.args['count'])):
            grafittis.append(Grafitti(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=grafittis,
                               oneliner=grafittis[0], titletext=titletext, generator='grafitti')
    else:
        grafitti = Grafitti(app.server, features)
        return render_template('oneliner.html', oneliner=grafitti, titletext=titletext, generator='grafitti')


@app.route('/grafitti_builder')
def grafitti_builder():
    """Build a a grafitti"""
    classname = 'grafitti'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)


#########################################################################


@app.route('/misfire')
def generatemisfire():
    """Generate a misfire"""

    features = feature_filter('misfire')
    titletext = 'My Spell Misfired!'
    features['npc'] = NPC(app.server)
    if ('count' in request.args and valid_count(request.args['count'])):
        misfires = []
        for _ in xrange(int(request.args['count'])):
            misfires.append(Misfire(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=misfires,
                               oneliner=misfires[0], titletext=titletext, generator='misfire')
    else:
        misfire = Misfire(app.server, features)
        return render_template('oneliner.html', oneliner=misfire, titletext=titletext, generator='misfire')


@app.route('/misfire_builder')
def misfire_builder():
    """Build a a misfire"""
    classname = 'misfire'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################


@app.route('/flaw')
def generateflaw():
    """Generate a flaw"""
    features = feature_filter('flaw')
    titletext = 'My Greatest Flaw...'

    if ('count' in request.args and valid_count(request.args['count'])):
        flaws = []
        for _ in xrange(int(request.args['count'])):
            flaws.append(Flaw(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=flaws,
                               oneliner=flaws[0], titletext=titletext, generator='flaw')
    else:
        flaw = Flaw(app.server, features)
        return render_template('oneliner.html', oneliner=flaw, titletext=titletext, generator='flaw')


@app.route('/flaw_builder')
def flaw_builder():
    """Build a a flaw"""
    classname = 'flaw'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################


@app.route('/currency')
def generatecurrency():
    """Generate a currency"""
    features = feature_filter('currency')
    titletext = 'Spare Some Change?'
    features['npc'] = NPC(app.server)
    if ('count' in request.args and valid_count(request.args['count'])):
        currencys = []
        for _ in xrange(int(request.args['count'])):
            currencys.append(Currency(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=currencys,
                               oneliner=currencys[0], titletext=titletext, generator='currency')
    else:
        currency = Currency(app.server, features)
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
    features['npc'] = NPC(app.server)
    if ('count' in request.args and valid_count(request.args['count'])):
        jobpostings = []
        for _ in xrange(int(request.args['count'])):
            jobpostings.append(JobPosting(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=jobpostings,
                               oneliner=jobpostings[0], titletext=titletext, generator='jobposting')
    else:
        jobposting = JobPosting(app.server, features)
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
    features['npc'] = NPC(app.server)
    if ('count' in request.args and valid_count(request.args['count'])):
        events = []
        for _ in xrange(int(request.args['count'])):
            events.append(Event(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=events,
                               oneliner=events[0], titletext=titletext, generator='event')
    else:
        event = Event(app.server, features)
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
    features['npc'] = NPC(app.server)
    if ('count' in request.args and valid_count(request.args['count'])):
        motivations = []
        for _ in xrange(int(request.args['count'])):
            motivations.append(Motivation(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=motivations,
                               oneliner=motivations[0], titletext=titletext, generator='motivation')
    else:
        motivation = Motivation(app.server, features)
        return render_template('oneliner.html', oneliner=motivation, titletext=titletext, generator='motivation')


@app.route('/motivation_builder')
def motivation_builder():
    """Build a a motivation"""
    classname = 'motivation'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################


@app.route('/phobia')
def generatephobia():
    """Generate a phobia"""
    features = feature_filter('phobia')
    titletext = 'You know what really scares me?'

    if ('count' in request.args and valid_count(request.args['count'])):
        phobias = []
        for _ in xrange(int(request.args['count'])):
            phobias.append(Phobia(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=phobias,
                               oneliner=phobias[0], titletext=titletext, generator='phobia')
    else:
        phobia = Phobia(app.server, features)
        return render_template('oneliner.html', oneliner=phobia, titletext=titletext, generator='phobia')


@app.route('/phobia_builder')
def phobia_builder():
    """Build a a phobia"""
    classname = 'phobia'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################


@app.route('/gem')
def generategem():
    """Generate a gem"""
    features = feature_filter('gem')
    titletext = 'OOOH, Shiny...'
    if ('count' in request.args and valid_count(request.args['count'])):
        gems = []
        for _ in xrange(int(request.args['count'])):
            gems.append(Gem(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=gems, oneliner=gems[0], titletext=titletext, generator='gem')
    else:
        gem = Gem(app.server, features)
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
    if ('count' in request.args and valid_count(request.args['count'])):
        mundaneitems = []
        for _ in xrange(int(request.args['count'])):
            mundaneitems.append(MundaneItem(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=mundaneitems,
                               oneliner=mundaneitems[0], titletext=titletext, generator='mundaneitem')
    else:
        mundaneitem = MundaneItem(app.server, features)
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
    if ('count' in request.args and valid_count(request.args['count'])):
        legends = []
        for _ in xrange(int(request.args['count'])):
            legends.append(Legend(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=legends,
                               oneliner=legends[0], titletext=titletext, generator='legend')
    else:
        legend = Legend(app.server, features)
        return render_template('oneliner.html', oneliner=legend, titletext=titletext, generator='legend')


@app.route('/legend_builder')
def legend_builder():
    """Build a a legend"""
    classname = 'legend'
    plist, pstring, pset = builder_form_data(classname)

    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)

#########################################################################


@app.route('/cuisine')
def generatecuisine():
    """Generate a cuisine"""
    features = feature_filter('cuisine')
    features['region'] = Region(app.server)
    titletext = 'What\'s for Dinner?'
    if ('count' in request.args and valid_count(request.args['count'])):
        cuisines = []
        for _ in xrange(int(request.args['count'])):
            cuisines.append(Cuisine(app.server, features))
            features['seed'] = set_seed()
        return render_template('oneliner.html', oneliners=cuisines,
                               oneliner=cuisines[0], titletext=titletext, generator='cuisine')
    else:
        cuisine = Cuisine(app.server, features)
        return render_template('oneliner.html', oneliner=cuisine, titletext=titletext, generator='cuisine')


@app.route('/cuisine_builder')
def cuisine_builder():
    """Build a a cuisine"""
    classname = 'cuisine'
    plist, pstring, pset = builder_form_data(classname)
    return render_template('generic_builder.html', plist=plist, pstring=pstring, pset=pset, name=classname)
