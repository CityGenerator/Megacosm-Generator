
import random
import json
from generators.Generator import Generator
import  generators
from util import Filters



class City(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)

        if not hasattr(self, 'region'):
            self.region=generators.Region.Region(self.redis)
        self.calculate_population()

    def calculate_population(self):
        self.population_estimate= random.randint(int(self.size['minpop']), int(self.size['maxpop']))
        self.population_density=  random.randint(int(self.size['min_density']), int(self.size['max_density']))

