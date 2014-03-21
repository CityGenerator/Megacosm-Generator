
import random
import json
from generators.Generator import Generator
from generators.NPC import  NPC
from generators.Region import  Region
from jinja2 import Template
from jinja2.environment import Environment
from util import Filters



class Resource(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)

        del self.name

        if not hasattr(self,'place'):
            self.place=Region(self.redis)

        self.subkind=self.kind+'_'+self.rand_value(self.kind+"_kind")

        self.generate_features(self.subkind)

        if not hasattr(self,'text'):
            self.text=self.render_template(self.template)
            self.text=self.render_template(self.text)
        self.text=self.text[0].capitalize()+self.text[1:]

