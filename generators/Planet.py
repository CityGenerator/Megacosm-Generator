
import random
import json
from generators.Generator import Generator
from generators.Moon import Moon
import pprint

class Planet(Generator):
    def __init__(self, server, features={}):
        Generator.__init__(self,server,features)
        self.name=self.generate_name('planet')
        self.generate_moons()
        size=Generator.select_by_roll(self,'planetsize')
        self.size=size['diameter']
        self.size_text=size['text']

    def generate_moons(self):
        """ Generate a list of moons """
        if ( not  hasattr(self, 'moons')):
            self.moons=[]
        if ( not hasattr(self, 'moon_count')):
            mooncount_data=Generator.select_by_roll(self,'mooncount')
            self.moon_count=mooncount_data['count']
            self.moon_text=mooncount_data['text']

        orbits=self.redis.lrange('moonorbit', 0,-1)

        self.moons=[]
        for moonId in xrange(self.moon_count):
            random.shuffle(orbits)
            self.moons.append(Moon(self.redis, {'orbit': json.loads(orbits.pop(0))  }))
