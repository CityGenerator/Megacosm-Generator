
from generators.Generator import Generator


class Star(Generator):
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis,features)
        self.name=self.generate_name('star')
        color=self.select_by_roll('starcolor')
        self.color=color['color']
        self.color_text=color['text']

        size=self.select_by_roll('starsize')
        self.multiplier=size['multiplier']
        self.size_text=size['text']
