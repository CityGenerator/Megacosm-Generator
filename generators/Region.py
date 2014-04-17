
from noise import snoise2
import math
import random
import json
from generators.Generator import Generator
import logging
#from City import City

import pprint

class Region(Generator):
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis,features)
        self.logger=logging.getLogger(__name__)

# TODO start a separate fork for cities and enable this with the new class
#    def add_cities(self):
#        """ add cities to the region"""
#        if not hasattr(self, 'cities'):
#            self.cities=[]
#        for cityid in xrange(self.citycount):
#            self.city.append( City(self.redis,{'region':self} ) )
