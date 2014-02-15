
from generators.Generator import Generator

class Star(Generator):
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis,features)
