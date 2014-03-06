
import random
import json
from generators.Generator import Generator
from generators.NPC import  NPC
import  Deity
from jinja2 import Template
from jinja2.environment import Environment
from util import Filters

class Sect(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)

        if 'deity' not in self.__dict__:
            self.deity=Deity(self.redis)

        if not self.domain:
            self.domain=random.shuffle(self.deity.portfolios)



