
import random
import json
from generators.Generator import Generator
import  generators

from util import Filters

class Motivation(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)

        self.generate_features('motivation'+self.kind)

        if not hasattr(self, 'npc'):
            self.npc=generators.NPC.NPC(self.redis, {'motivation':self})

        self.text=self.render_template(self.text)
    def __str__(self):
        return self.text
