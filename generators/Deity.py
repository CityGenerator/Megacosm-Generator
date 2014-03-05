
import random
import json
from generators.Generator import Generator
from generators.NPC import  NPC
from jinja2 import Template
from jinja2.environment import Environment
from util import Filters

class Deity(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)

        self.avatar=NPC(redis)

        #print self.__dict__
        environment = Environment()
        environment.filters['article'] = Filters.select_article
        environment.filters['pluralize'] = Filters.select_pluralize

        avatarstats=self.avatar.stats
        avatarstats.remove('sex')
        random.shuffle(avatarstats)
        self.favored_stat=avatarstats.pop()
        self.select_portfolio()
        self.generate_sects()

    def generate_sects(self): 
        self.sects=[]
        for i in self.portfolios[1:]:
           print "TODO: generate a sect right here." 

    def select_portfolio(self):
        points=int(self.importance['points'])
        powerlevels=self.redis.lrange('deitypowerscale',0,-1)
        self.portfolios=[]
        while points>0:
            powerlevel=int(powerlevels.pop())
            #print "main loop with",points,"points, powerlevel", powerlevel
            if powerlevel <= points:
                #print "acceptable powerlevel",powerlevel
                # This level is acceptable, try again next time
                random.shuffle(powerlevels)
                powerlevels.insert(0,powerlevel)
                # snag all portfolios for this level
                portfolios=self.redis.zrevrangebyscore('deityportfolio', powerlevel,powerlevel)
                random.shuffle(portfolios)
                while powerlevel <= points :
                    newportfolio=json.loads(portfolios.pop())
                    powerlevel=int(newportfolio['score'])
                    #print "powerlevel:",powerlevel,"  points:",points
                    #print "adding ",newportfolio,"to the list"
                    self.portfolios.append(newportfolio)
                    points=points- powerlevel
            else:
                print "can't support powerlevel",powerlevel,"with",points,"points"
        #print "final portfolios:",self.portfolios
        total=0
        for portfolio in self.portfolios:
            total+=portfolio['score']
        #print total
#TODO move FILTER additions to generator
#TODO same with template rendering

#cult_acceptance
#cult_kind
#deity_age
#deity_clergytype
#deity_devotion
#deity_favored_weapon
#deity_followerzeal
#deity_holysymbol
#deity_holysymbol_type
#deity_holysymbol_type_chance
#deity_importance
#deity_jealousy
#deityportfolio
#deity_primarycolor
#deity_secondarycolor
#deity_secrecy
#deity_vow
#deity_vow_description
#deity_worship
#
#
#'clergytype': 'abbots' 'jealousy': {u'score': 90 u'name': u'selfish'} 'holysymbol': 'insect' 'vow': 'purity' 'followers': {u'score': 70 u'name': u'wide spread'} 'holysymbol_type': 'shining' 'importance': {u'score': 80 u'name': u'intermediate deity' u'points': 10} 'secrecy': {u'score': 20 u'name': u'tight lipped'} 'name': {'full': ''} 'age': {u'score': 55 u'name': u'antiquated'} 'vow_description': {u'name': u'Purity' u'description': u'avoid contact with dead flesh'} 'primarycolor': 'very dark grey' 'devotion': {u'score': 60 u'name': u'an unknown number of' {'deity_age_roll': 75, 'clergytype': 'clergy', 'deity_jealousy_roll': 58, 'redis': Redis<ConnectionPool<Connection<host=127.0.0.1,port=6379,db=0>>>, 'holysymbol': 'bell', 'vow': 'chastity', 'deity_devotion_roll': 82, 'secondarycolor': 'light red', 'favored_weapon': 'butterfly swords', 'worship': 'supplication', 'jealousy': {u'score': 60, u'name': u'covetous'}, 'deity_secrecy_roll': 92, 'followers': {u'score': 80, u'name': u'everywhere'}, 'importance': {u'score': 50, u'name': u'lesser deity', u'points': 4}, 'deity_importance_roll': 43, 'secrecy': {u'score': 100, u'name': u'open'}, 'deity_holysymbol_type_roll': 43, 'name': {'full': ''}, 'age': {u'score': 75, u'name': u'primordial'}, 'deity_followers_roll': 73, 'seed': 80150, 'vow_description': {u'name': u'Chastity', u'description': u'refrain from marriage and sex'}, 'avatar': <generators.NPC.NPC object at 0x7fa8593d1f90>, 'primarycolor': 'brown', 'devotion': {u'score': 85, u'name': u'hundreds of thousands of'}}
