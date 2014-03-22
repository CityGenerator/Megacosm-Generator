
import random
import json
from generators.Generator import Generator
from generators.NPC import  NPC
from jinja2 import Template
from jinja2.environment import Environment
from util import Filters



class MundaneItem(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)

        self.text=self.kind
