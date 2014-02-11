import redis
import json
import random

class Generator():
    def __init__(self,redis, features={}):
        self.redis=redis
        for feature, value in features.iteritems():
            setattr( self, feature, value)
        if 'seed' not in features:
            self.seed=random.randint(1,10000000)
        random.seed(self.seed)

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
                print "trailer set!"
                name['trailer']=self.rand_value(key+'trailer')
                name['full']+=' '+name['trailer']
            print name['full']
        return name   


    def rand_value(self,key):
        if self.redis.exists(key) and self.redis.type(key) == 'list':
            return self.redis.lindex(key, random.randint(0,self.redis.llen(key)-1 ))
        else:
            raise Exception( "the key %s doesn't appear to exist or isn't a list (%s)." % (key, self.redis.type(key)  ))


    def select_by_roll(self,roll, key):
        if self.redis.exists(key) and self.redis.type(key) == 'zset':
            rollvalue= self.redis.zrangebyscore(key, roll, 100, 0, 1);
            if rollvalue == None:
                raise Exception( "the key %s appears to be empty for a value of %s- This should never happen." % (key, roll))
            return rollvalue
        else:
            raise Exception( "the key %s doesn't appear to exist or isn't a sorted list (%s)." % (key, self.redis.type(key)))

