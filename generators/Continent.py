
from Country import Country
from generators.Generator import Generator
import logging
import random

class Continent(Generator):
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis,features)
        self.logger=logging.getLogger(__name__)
        # set a random count 
        if not hasattr(self, 'countrycount'):
            self.countrycount=random.randint(self.countrydetails['mincount'], self.countrydetails['maxcount'])

    def add_countries(self):
        """ add countries to the continent"""
        if not hasattr(self, 'countries'):
            self.countries=[]
        for countryid in xrange(self.countrycount):
            self.countries.append( Country(self.redis, {'continent':self} ) )
        
    def __str__(self):
        return "%s with %s countries" %(self.name['full'], self.countrycount)
