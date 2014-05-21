
from generators.Country import Country
from generators.Generator import Generator
import logging

class Govt(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)
        self.logger=logging.getLogger(__name__)

        self.generate_features('govt'+self.kind)

        if not hasattr(self, 'body'):
            #TODO this should have an if statement on kind and also do cities
            self.body=Country(self.redis)
