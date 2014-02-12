
import random


from generators.Generator import Generator


class Moon(Generator):
    def __init__(self, server, features={}):
        Generator.__init__(self,server,features)
        self.name=self.generate_name('moon')
        color=self.select_by_roll('mooncolor')
        self.color=color['color']
        self.color_text=color['text']

        size=self.select_by_roll('moonsize')
        self.multiplier=size['multiplier']
        self.size_text=size['text']
