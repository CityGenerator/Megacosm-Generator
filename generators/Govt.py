
import random
import json
from generators.Generator import Generator
from generators.Country import Country
import logging
#from generators.City import 
from util import Filters

class Govt(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)
        self.logger=logging.getLogger(__name__)

        self.generate_features('govt'+self.kind)

        if not hasattr(self, 'body'):
            #TODO this should have an if statement on kind and also do cities
            self.body=Country(self.redis)
