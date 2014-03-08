import redis
import json
import random
from jinja2 import Template
from jinja2.environment import Environment
from util import Filters



class Generator(object):
    def __init__(self,redis, features={}):
        """ set any features and generate a seed if one is not included. """

        self.redis=redis
        namekey= self.__class__.__name__.lower()
        self.name=self.generate_name('name'+namekey)

        # For each feature, set it as an attribute for this generator
        for feature, value in features.iteritems():
            setattr( self, feature, value)
        # If a seed isn't included, generate one.

        if 'seed' not in features:
            self.seed=random.randint(1,10000000)

        self.generate_features(namekey)

    def generate_features(self,namekey):
        """ Given a namekey, add those features to this object."""
        #print "my namekey", namekey
        #print self.redis.keys(namekey+'_*')
        for key in self.redis.keys(namekey+'_*'):
            #print "testing key",key
            if  self.redis.exists(key+"_chance"):
                chance=int(self.redis.get(key+"_chance"))
                #print "==",key,"_chance exists:",chance
                if key+"_roll" not in self.__dict__:
                      setattr( self, key+"_roll", random.randint(1,100) )
                if int(getattr(self,key+"_roll")) > chance:
                    print key+"_roll (",getattr(self,key+"_roll"),") vs ",chance
                    print key," failed its roll"
                    continue

                
            if self.redis.type(key) == 'zset':
                feature=key.replace(namekey+'_','')
                #print "adding zset",feature,"to ", namekey
                setattr( self, feature, Generator.select_by_roll(self,key) )
            elif self.redis.type(key) == 'list' :
                feature=key.replace(namekey+'_','')
                if feature not in self.__dict__ :
                    #print "adding list",feature,"to ", namekey
                    setattr( self, feature, Generator.rand_value(self,key) )
                if self.redis.exists(key+"_description") and feature+"_description" not in self.__dict__ :
                    #print "adding list",feature,"to ", namekey
                    #print key+"_description", "has ",getattr(self,feature),"returns",self.redis.hmget(key+"_description",getattr(self,feature)  )

                    setattr( self, feature+"_description", json.loads(self.redis.hmget(key+"_description",getattr(self,feature) )[0] ) )
                
            #else:
                #print "no idea ",key,"what ",self.redis.type(key),"is."
# 

    def generate_name(self,key):
        """ Given a key, query redis and check if all 5 parts of a name exist, then generate a name structure.
            This creates the structure "Title PreRootPost Trailer"
            Note that in the full name, the title has a trailing space and the triler has a preceeding space.
            Pre, Root and Post have no spaces."""
        name={'full':''}

        if self.redis.exists(key+'title'):
            roll=random.randint(1,100)
            if (not self.redis.exists(key+'title_chance')) or (roll < int(self.redis.get(key+'title_chance'))):
                name['title']=self.rand_value(key+'title')
                name['full']=name['title']+' '

        for part in [ 'pre', 'root', 'post']:
            if self.redis.exists(key+part):
                if (not self.redis.exists(key+part+'_chance')) or (random.randint(1,100) < int(self.redis.get(key+part+'_chance'))):
                    name[part]=self.rand_value(key+part)
                    name['full']+=name[part]

        if self.redis.exists(key+'trailer'):
            roll=random.randint(1,100)
            if (not self.redis.exists(key+'trailer_chance')) or (roll < int(self.redis.get(key+'trailer_chance'))):
                #print "trailer set!"
                name['trailer']=self.rand_value(key+'trailer')
                name['full']+=' '+name['trailer']
            #print name['full']
        return name   

    def rand_value(self,key):
        """ Select a Random Value from the list matching the key in redis. """
        if self.redis.exists(key) and self.redis.type(key) == 'list':
            value=self.redis.lindex(key, random.randint(0,self.redis.llen(key)-1 ))
            return value
        else:
            raise Exception( "the key (%s) doesn't appear to exist or isn't a list (%s)." % (key, self.redis.type(key)  ))

    def select_by_roll(self,key ):
        """ Using roll, select the closest matching score from key in Redis. """
        if key+'_roll' not in self.__dict__ :
            setattr(self,key+'_roll', random.randint(1,100))

        roll=max(1,min(getattr(self,key+'_roll'),100))

        if self.redis.exists(key) and self.redis.type(key) == 'zset':
            rollvalue= self.redis.zrangebyscore(key, roll, 100, 0, 1)
            if rollvalue == None:
                raise Exception( "the key (%s) appears to be empty for a roll of %s- This should never happen." % (key, roll))
            try:
                return json.loads(rollvalue[0])
            except Exception as e:
                print "couldn't read json",rollvalue[0]
                raise e
        else:
            raise Exception( "the key (%s) doesn't appear to exist or isn't a zset (%s)." % (key, self.redis.type(key)))

    def render_template(self,template):
        """ Renders a given template using itself."""
        environment = Environment()
        environment.filters['article'] = Filters.select_article
        environment.filters['pluralize'] = Filters.select_pluralize
        template= environment.from_string(template)

        return template.render(params=self)

