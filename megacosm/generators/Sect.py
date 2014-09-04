
from megacosm.generators import Generator
from megacosm import generators
import logging
import random

class Sect(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)
        self.logger=logging.getLogger(__name__)

        if not hasattr(self, 'deity'):
            self.deity=generators.Deity.Deity(redis)


        if not hasattr(self, 'domain'):
            portfolio=self.deity.portfolios
            random.shuffle(portfolio)
            self.domain=portfolio[0]

#TODO this should have an __str__; is it using the text->template pattern?
