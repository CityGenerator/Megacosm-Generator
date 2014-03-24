
import random
import json
from generators.Generator import Generator
from generators.NPC import  NPC
from jinja2 import Template
from jinja2.environment import Environment
from util import Filters



class Rumor(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)

        for person in ['victim', 'culprit', 'source', 'believer' ]:
            if not hasattr(self,person):
                setattr(self,person,NPC(self.redis).name['full'])
        
        if not hasattr(self,'text'):
            self.text=self.render_template(self.template)
            self.text=self.render_template(self.text)
        self.text=self.text[0].capitalize()+self.text[1:]

