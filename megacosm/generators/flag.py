
from .generator import Generator
import json
import logging
import random
import string

class Flag(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)
        self.logger=logging.getLogger(__name__)

        self.select_colors()

        self.overlay_stripe_countselected=random.randint(0,int(self.overlay_stripe_count))
        if not hasattr(self, 'letter'):
            self.letter=random.choice(string.ascii_uppercase)

    def select_colors(self):
        colornames=self.redis.lrange('flagcolor',0,-1)
        random.shuffle(colornames)
        
        if not hasattr(self,'colors'):
            self.colors=[]

        for i in range(7-len(self.colors)):
            colorname=colornames[i]
            jsonstring=self.redis.hget('flagcolor_description',colorname)
            #FIXME Note this still overwrites
            self.colors.append(json.loads(jsonstring))

    def tojson(self):
        data=self.__dict__
        del data['redis']
        del data['pipeline']
        del data['logger']
        return json.dumps(data, skipkeys=True, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=4, separators=(', ', ': '), encoding="utf-8", default=None, sort_keys=False, )

        return jsonobj
