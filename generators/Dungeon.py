
from noise import snoise2
import math
import random
import json
from generators.Generator import Generator

import pprint

class Dungeon(Generator):
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis,features)
        


#http://www.roguebasin.com/index.php?title=Complete_Roguelike_Tutorial,_using_python%2Blibtcod,_part_3
