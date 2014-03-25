
import math
import random
import json
from generators.Generator import Generator
from generators.NPC import NPC
from generators.Business import Business
#from City import City

import pprint

class JobPosting(Generator):
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis,features)
        
        for field in [ 'contact','npc']:
            if not hasattr(self,field):
                setattr(self,field,NPC(self.redis))
        if not hasattr(self,'business'):
            setattr(self,'business',Business(self.redis))


        if not hasattr(self,'text'):

            for field in [ 'hook', 'request']:
                if hasattr(self,field):
                    self.template= getattr(self, field) +' '+self.template

            for field in [ 'requirement', 'disclaimer', 'payment']:
                if hasattr(self,field):
                    self.template= self.template+' '+getattr(self, field)

            self.template=self.template+' Contact '+self.contact.name['full']
            self.template=self.template+" at the "+self.business.name['full']
            if hasattr(self, 'detail'):
                self.template=self.template+" "+self.detail

            self.template+="."

            self.text=self.render_template(self.template)
            self.text=self.render_template(self.text)
        self.text=self.text[0].capitalize()+self.text[1:]

    def __str__(self):
        return self.text

