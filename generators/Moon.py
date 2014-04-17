
import random

from generators.Generator import Generator
import logging


class Moon(Generator):
    def __init__(self, server, features={}):
        Generator.__init__(self,server,features)
        self.logger=logging.getLogger(__name__)
