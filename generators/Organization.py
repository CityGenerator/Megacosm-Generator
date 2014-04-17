
from generators.Generator import Generator
from generators.Leader import Leader
import logging

class Organization(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)
        self.logger=logging.getLogger(__name__)

        if not hasattr(self,'leader'):
            self.leader=Leader(self.redis, {'kind':self.kind,'location':self })

        if not hasattr(self,'text'):
            self.text=self.render_template(self.template)
        self.oldname=self.name['full']
        self.name['full']=self.text

