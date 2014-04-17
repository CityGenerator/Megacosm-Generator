
import math
import random
import json
from generators.Generator import Generator
from Region import Region
import logging
import pprint

class Country(Generator):
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis,features)
        self.logger=logging.getLogger(__name__)

        if not hasattr(self, 'regioncount'):
            self.regioncount=random.randint(self.regiondetails['mincount'], self.regiondetails['maxcount'])
        
    def add_regions(self):
        """ add regions to the country"""
        if not hasattr(self, 'regions'):
            self.regions=[]
        for regionid in xrange(self.regioncount):
            self.regions.append( Region(self.redis,{'country':self } ) )
        
    def __str__(self):
        return "%s with %s regions" %(self.name['full'], self.regioncount)
