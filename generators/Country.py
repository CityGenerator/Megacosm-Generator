
from noise import snoise2
import math
import random
import json
from generators.Generator import Generator

import pprint

class Country(Generator):
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis,features)

#        namecountry
        # TODO add countries.
        
