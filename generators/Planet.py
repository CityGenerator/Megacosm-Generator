
from noise import snoise2
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

        #self.generate_continents()
        self.generate_moons()


    def generate_continents(self):
        """ Generate the continents for this planet"""
        self.continent_count=random.randint(1,5);
        self.continent=[]
        for continentID in xrange(self.continent_count):
            self.continent.append( Continent(self.redis) )




    def generate_moons(self):
        """ Generate a list of moons """
        self.moons=[]
        for moonId in xrange(self.mooncount['count']):
            self.moons.append(Moon(self.redis ))
