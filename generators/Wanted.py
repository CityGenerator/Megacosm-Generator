
import random
import json
from generators.Generator import Generator
from generators.NPC import  NPC
from jinja2 import Template
from jinja2.environment import Environment
from util import Filters
import logging



class Wanted(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)
        self.logger=logging.getLogger(__name__)

        for person in ['npc','victim' ]:
            if not hasattr(self,person):
                setattr(self,person,NPC(self.redis))
        

        self.headline=self.render_template(self.headline)
        self.lastseen=self.render_template(self.lastseen)

