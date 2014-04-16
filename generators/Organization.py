
import random
import json
from generators.Generator import Generator
from generators.Leader import Leader
from util import Filters



class Organization(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)


        if not hasattr(self,'leader'):
            self.leader=Leader(self.redis)

        if not hasattr(self,'text'):
            self.text=self.render_template(self.template)
        self.oldname=self.name['full']
        self.name['full']=self.text

