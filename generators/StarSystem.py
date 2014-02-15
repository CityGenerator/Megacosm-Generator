
import random
import json
from generators.Star import Star
from generators.Planet import Planet
from generators.Generator import Generator

class StarSystem(Generator):
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis, features)
        self.generate_stars()
        self.generate_planet()

    def generate_stars(self):
        """ Do stuff"""
        self.stars=[]

        positions=self.redis.lrange('starposition', 0,-1)

        for starId in xrange(self.starcount['count']):
            random.shuffle(positions)
            self.stars.append(Star(self.redis, {'pos': json.loads(positions.pop(0))  }))

    def generate_planet(self):
        """ Do stuff"""
        self.planet=Planet(self.redis)
