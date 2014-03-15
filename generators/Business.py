
import random
import json
from generators.Generator import Generator
from generators.NPC import  NPC

class Business(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)

        self.generate_features(self.kind)

#        self.owner=NPC(redis)
