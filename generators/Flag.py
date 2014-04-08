
import random
import json
from generators.Generator import Generator

class Flag(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)

        self.select_colors()


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
        return json.dumps(data, skipkeys=True, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=4, separators=(', ', ': '), encoding="utf-8", default=None, sort_keys=False, )

        return jsonobj
