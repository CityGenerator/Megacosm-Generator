
import random
import json
from generators.Generator import Generator
from generators.NPC import  NPC

class Business(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)

        self.generate_features(self.kind)
        self.senses=[]

        if hasattr(self,  'smell'):
            self.smell='you smell '+self.smell
            self.senses.append(self.smell)
        if hasattr(self,  'sound'):
            self.sound='you hear '+self.sound
            self.senses.append(self.sound)
        if hasattr(self,  'sight'):
            self.sight='you see '+self.sight
            self.senses.append(self.sight)
        


        self.owner=NPC(redis)
        #TODO patrons should be better calculated
        self.patroncount=random.randint(1,10);

        if hasattr(self,  'trailer'):
            self.name['trailer']=self.trailer
            self.name['full']=self.name['full'] +' '+self.trailer.title() 


        if not hasattr(self,  'maxfloors'):
            self.maxfloors=1

        self.floor= random.randint(1,int(self.maxfloors))


