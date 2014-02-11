
import random


from generators.Generator import Generator


class Planet(Generator):
    def __init__(self, server, features={}):
        Generator.__init__(self,server,features)
        self.name=self.generate_name('planet')


