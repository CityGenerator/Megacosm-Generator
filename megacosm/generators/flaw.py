
from .generator import Generator
from .npc import NPC
import logging
import random

class Flaw(Generator):
    """ Define a flaw to be used in your game """
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)
        self.logger=logging.getLogger(__name__)

        # Double parse the template to fill in templated template values.
        if not hasattr(self,'text'):
            self.text=self.render_template(self.template)
            self.text=self.render_template(self.text)
        self.text=self.text[0].capitalize()+self.text[1:]

    def __str__(self):
        return self.text

