
from noise import snoise2
import math
import random
import json
from generators.Generator import Generator
#from Region import Region

import pprint

class Country(Generator):
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis,features)

        
# TODO start a separate fork for regions and enable this with the new class
#    def add_regions(self):
#        """ add regions to the country"""
#        if not hasattr(self, 'regions'):
#            self.regions=[]
#        for regionid in xrange(self.regioncount):
#            self.region.append( Region(self.redis ) )
        
