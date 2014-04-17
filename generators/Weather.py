
import random
import json
from generators.Generator import Generator
from util import Filters
import logging



class Weather(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)
        self.logger=logging.getLogger(__name__)


