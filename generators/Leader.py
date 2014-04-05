
import random
import json
from generators.Generator import Generator
from generators.NPC import  NPC
from generators.Sect import  Sect
from generators.Country import Country
from generators.City import City


class Leader(NPC):
    """ Generate a god for your world"""
    def __init__(self, redis, features={}):
        NPC.__init__(self,redis,features, 'npc')

        self.generate_features('leader')
        self.generate_features('leader'+self.kind)

        if self.kind_description['scope'] == 'country':
            self.location=Country(self.redis, {'leader':self})
#        elif self.kind_description['scope'] == 'city':
#            self.location=City(self.redis, {'leader':self})
        else:
#           TODO This should default to organization...
            self.location=Country(self.redis, {'leader':self})
        


        self.set_title()

    def set_title(self):
        self.name['title']=self.leader_description[self.sex['name']]
        self.name['fulltitled']=self.name['title'] +" "+self.name['full']
