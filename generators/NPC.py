
import random
import json
from generators.Generator import Generator

class NPC(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)

        self.select_race()
        self.select_names()

        # This list tells us which of the attributes are actually stats
        self.stats=self.redis.lrange('stat_npc',0,-1)

    def select_race(self):
        #print self.redis.llen('race')
        if hasattr(self,'race'):
            if self.race not in self.redis.lrange('race',0,-1) :
                raise Exception( "%s is not a valid race and has no associated data" % self.race)
        else:
            self.race=self.rand_value('race')
        
        if self.redis.exists(self.race+"_details"):
            self.details=json.loads(self.redis.get(self.race+"_details"));
        else:
            self.details={}
            self.details['name']=self.race.title()
            self.details['size']="medium"
            self.details['description']="nothing special"

    def select_names(self):
        nameorder= self.redis.zrange(self.race+'_name_order',0,-1)
        #print nameorder
        for name in nameorder :
            self.name[name]={}
            nameparts=self.redis.hgetall(self.race+"_name_"+name)
            for namepart in nameparts :
                namepartkey=self.race+"_name_"+name+"_"+namepart
                # if random number is less than  nape part chance
                if random.randint(0,100) <= int( nameparts[namepart]):
                    self.name[name][namepart] = self.rand_value(namepartkey)
            
            self.name[name+"name"]=""
            for namepart in ['title','pre', 'root', 'post','trailer']:
                if namepart in self.name[name]:
                    if namepart == 'trailer': #space goes before namepart
                        self.name[name+"name"]+=" " 
                    self.name[name+"name"]+=self.name[name][namepart]
                    if namepart == 'title': #space goes after namepart
                        self.name[name+"name"]+=" "

            self.name['full']+=self.name[name+"name"]+" "
        self.name['full']=self.name['full'].strip()
