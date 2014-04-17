
import random
import json
from generators.Generator import Generator
import logging

import Deity


class Sect(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)
        self.logger=logging.getLogger(__name__)

        if not hasattr(self, 'deity'):
            self.deity=Deity.Deity(redis)


        if not hasattr(self, 'domain'):
            portfolio=self.deity.portfolios
            random.shuffle(portfolio)
            self.domain=portfolio[0]

#TODO this should have an __str__; is it using the text->template pattern?
