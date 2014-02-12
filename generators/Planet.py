
import random

from generators.Generator import Generator
from generators.Moon import Moon
import pprint

class Planet(Generator):
    def __init__(self, server, features={}):
        Generator.__init__(self,server,features)
        self.name=self.generate_name('planet')
        self.generate_moons()


    def generate_moons(self):
        if ( not hasattr(self, 'moon_count')):
            mooncount_data=Generator.select_by_roll(self,'mooncount')
            self.moon_count=mooncount_data['count']
            self.moon_text=mooncount_data['text']
        self.moons=[]
        for moonId in xrange(self.moon_count):
            self.moons.append(Moon(self.redis))
