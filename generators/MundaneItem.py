
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

        if not hasattr(self,'text'):
            #TODO move this to the data file
            #self.text=self.render_template("{{params.quality['name']|article}} {{params.kind}}, {{params.repair['name']}}")
            self.text=self.render_template("{{params.kind}}")
        self.text=self.text[0].capitalize()+self.text[1:]

    def __str__(self):
        return self.text
