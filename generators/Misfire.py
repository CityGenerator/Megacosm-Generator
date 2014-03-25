
import random
import json
from generators.Generator import Generator
from generators.NPC import  NPC
from jinja2 import Template
from jinja2.environment import Environment
from util import Filters



class Misfire(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)

        if not hasattr(self,'text'):
            self.text=self.render_template(self.template)
            self.text=self.render_template(self.text)
        self.text=self.text[0].capitalize()+self.text[1:]

    def __str__(self):
        return self.text
