
from noise import snoise2
import math
import random
import json
from generators.Generator import Generator

import pprint

class Continent(Generator):
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis,features)
        if not hasattr(self, 'countrycount'):
            self.countrycount=random.randint(self.countrydetails['mincount'], self.countrydetails['maxcount'])

        # TODO add countries.
        
