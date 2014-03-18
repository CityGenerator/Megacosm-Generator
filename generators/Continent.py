
from noise import snoise2
import math
import random
import json
from generators.Generator import Generator
from Country import Country

import pprint

class Continent(Generator):
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis,features)
        # set a random count 
        if not hasattr(self, 'countrycount'):
            self.countrycount=random.randint(self.countrydetails['mincount'], self.countrydetails['maxcount'])


    def add_countries(self):
        """ add countries to the continent"""
        if not hasattr(self, 'countries'):
            self.countries=[]
        for countryid in xrange(self.countrycount):
            self.countries.append( Country(self.redis, {'continent':self} ) )
        
