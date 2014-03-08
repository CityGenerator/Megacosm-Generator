
import random
import json
from generators.Generator import Generator
from generators.NPC import  NPC
from jinja2 import Template
from jinja2.environment import Environment
from util import Filters



class Bond(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)

        if not hasattr(self,'you'):
            self.you='you' 

        if not hasattr(self,'other'):
            self.other=NPC(self.redis).name['full'] 


        members=[self.you,self.other]
        random.shuffle(members)
        if not hasattr(self,'either'):
            self.either=members[0] 
        random.shuffle(members)

        if not hasattr(self,'partyA'):
            self.partyA=members.pop() 
        if not hasattr(self,'partyB'):
            self.partyB=members.pop() 

        
        if not hasattr(self,'text'):
            if hasattr(self,'when'):
                self.template=self.when+', '+self.template

            self.text=self.render_template(self.template) 
        self.text=self.text[0].capitalize()+self.text[1:]
            
        print "wee",self.__dict__

