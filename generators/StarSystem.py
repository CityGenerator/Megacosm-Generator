
import random
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
        if ( not  hasattr(self, 'stars')):
            self.stars=[]
        if ( not  hasattr(self, 'star_count')):
            starcount_data=Generator.select_by_roll(self,'starcount')
            self.star_count=starcount_data['count']
            self.star_text=starcount_data['text']

        for starId in xrange(self.star_count):
            self.stars.append(Star(self.redis))

    def generate_planet(self):
        """ Do stuff"""
        self.planet=Planet(self.redis)
