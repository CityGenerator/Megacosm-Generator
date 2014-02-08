
import random
from generators.Star import Star

class StarSystem():
    def __init__(self, server, features={}):
        for feature, value in features.iteritems():
            setattr( self, feature, value)
            print "set",feature,"to",value
        if 'seed' not in features:
            self.seed=random.randint(1,10000000)
        random.seed(self.seed)
        self.generate_stars()
        

    def generate_stars(self):
        """ Do stuff"""
        if ( not  hasattr(self, 'stars')):
            self.stars=[]
        if ( not  hasattr(self, 'star_count')):
            self.star_count=1

        for starId in xrange(self.star_count):
            self.stars.append(Star())
