
import random
import json
from generators.Generator import Generator
from generators.NPC import  NPC
from jinja2 import Template
from jinja2.environment import Environment
from util import Filters



class MagicItem(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)
        self.generate_features(self.kind)
        
        self.npc=NPC(redis)
        print self.creator_template

        environment = Environment()
        environment.filters['article'] = Filters.select_article
        environment.filters['pluralize'] = Filters.select_pluralize
        template= environment.from_string(self.creator_template)

        self.creator=template.render(npc=self.npc)

        template= environment.from_string(self.name_template)
        self.name=template.render(magicitem=self)

#TODO move FILTER additions to generator
#TODO same with template rendering
