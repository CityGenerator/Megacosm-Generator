
import random
import json
from generators.Generator import Generator
from generators.NPC import  NPC
from jinja2 import Template
from jinja2.environment import Environment
from util import Filters

class Deity(NPC):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)
        
       
        print self.__dict__ 
        environment = Environment()
        environment.filters['article'] = Filters.select_article
        environment.filters['pluralize'] = Filters.select_pluralize

#TODO move FILTER additions to generator
#TODO same with template rendering
