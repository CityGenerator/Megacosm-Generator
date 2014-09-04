
from megacosm.generators.Gem import Gem
from megacosm.generators import Generator
import logging

class Artwork(Generator):
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis,features)
        self.logger=logging.getLogger(__name__)

        if not hasattr(self,'gem'):
            setattr(self,'gem',Gem(self.redis))

        if not hasattr(self,'text'):
            self.text=self.render_template(self.template)
            self.text=self.render_template(self.text)
        self.text=self.text[0].capitalize()+self.text[1:]
 
    def __str__(self):
        return self.text


