
from generators.Generator import Generator
from generators.NPC import NPC
import logging

class Legend(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)
        self.logger=logging.getLogger(__name__)

        for person in ['npc','villain' ]:
            if not hasattr(self,person):
                setattr(self,person,NPC(self.redis))
        
        if not hasattr(self,'text'):
            self.text=self.render_template(self.template)
            self.text=self.render_template(self.text)
        self.text=self.text[0].capitalize()+self.text[1:]

    def __str__(self):
        return self.text
