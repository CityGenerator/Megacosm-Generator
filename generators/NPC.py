
from generators.Generator import Generator
import generators
import json
import logging
import random

class NPC(Generator):
    def __init__(self, redis, features={}, namekey=None ):

        Generator.__init__(self,redis,features,namekey)
        self.logger=logging.getLogger(__name__)

        if self.race not in self.redis.lrange('npc_race',0,-1):
            raise Exception, " %s is not a valid race and has no associated data" % (self.race)
        self.generate_features(self.race)
        self.generate_features(self.covering)
        self.coveringtext=self.render_template(self.covertemplate)

        self.details=json.loads(self.details)

        self.select_names()

        if not hasattr(self,'motivation'):
            self.motivation=generators.Motivation.Motivation(self.redis, {'npc':self})


    def select_names(self):
        nameorder= self.redis.zrange(self.race+'_name_order',0,-1)
        for namejson in nameorder :
            name=json.loads(namejson)['name']
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


