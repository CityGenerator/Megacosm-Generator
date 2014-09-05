
from .generator import Generator
import logging

class Star(Generator):
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis,features)
        self.logger=logging.getLogger(__name__)
