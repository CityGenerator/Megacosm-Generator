
import math
import random
import json
from generators.Generator import Generator
from generators.Moon import Moon
from generators.Continent import Continent
import pprint

class Planet(Generator):

    def __init__(self, redis, features={}):
        Generator.__init__(self,redis,features)


    def add_continents(self):
        """ Generate the continents for this planet"""
        # Ensure that we have a continents array
        if not hasattr(self, 'continents'):
            self.continents=[]

        # Ensure that we have a target number of continents
        if not hasattr(self, 'continentcount'):
            self.continentcount=random.randint(1,5);
        # Banzai, er generate continents!
        for continentID in xrange(self.continentcount):
            self.continents.append( Continent(self.redis) )


    def add_moons(self):
        """ Generate a list of moons """
        if not hasattr(self, 'moons'):
            self.moons=[]

        # Note that mooncount is a planet stat

        for moonId in xrange(self.mooncount['count']):
            self.moons.append(Moon(self.redis ))
