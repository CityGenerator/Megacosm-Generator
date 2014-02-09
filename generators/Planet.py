
import random

class Planet():
    def __init__(self, server, features={}):
        for feature, value in features.iteritems():
            setattr( self, feature, value)
            print "set",feature,"to",value
        if 'seed' not in features:
            self.seed=random.randint(1,10000000)
        random.seed(self.seed)
        
