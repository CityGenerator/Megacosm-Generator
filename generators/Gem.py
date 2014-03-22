
import random
import json
from generators.Generator import Generator
from util import Filters



class Gem(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)


        if not hasattr(self, 'color'):
            self.color=random.choice(self.kind_description['color'])
        print "color:",self

        if not hasattr(self,'text'):
            self.text=self.render_template(self.template)
            self.text=self.render_template(self.text)
        self.text=self.text[0].capitalize()+self.text[1:]
    def __str__(self):
        return "%s %s %s, %s" % (self.quality['name'],self.color, self.kind_description['name'], self.value['name'])

