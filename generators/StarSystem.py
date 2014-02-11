
import random
from generators.Star import Star
from generators.Generator import Generator

class StarSystem(Generator):
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis, features)
        self.generate_stars()

    def generate_stars(self):
        """ Do stuff"""
        if ( not  hasattr(self, 'stars')):
            self.stars=[]
        if ( not  hasattr(self, 'star_count')):
            self.star_count=1

        for starId in xrange(self.star_count):
            self.stars.append(Star(self.redis))
