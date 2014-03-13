
import random
import json
from generators.Generator import Generator

import Deity

from jinja2 import Template
from jinja2.environment import Environment
from util import Filters

class Sect(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)

        if 'deity' not in self.__dict__:
            self.deity=Deity.Deity(redis)


        if 'domain' not in self.__dict__:
            portfolio=self.deity.portfolios
            random.shuffle(portfolio)
            self.domain=portfolio[0]


