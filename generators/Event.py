
from noise import snoise2
import math
import random
import json
from generators.Generator import Generator
#from City import City

import pprint

class Event(Generator):
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis,features)
        


        self.generate_features('event'+self.kind )

        if not hasattr(self,'text'):
            self.template="{{params.variety }} {{params.kind}}, which is {{params.magnitude['name']}} to the people in the area."
            self.text=self.render_template(self.template)
            self.text=self.render_template(self.text)
        self.text=self.text[0].capitalize()+self.text[1:]


