
import random
import json
from generators.Generator import Generator

class Flag(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)

        colornames=self.redis.lrange('flagcolor',0,-1)
        random.shuffle(colornames)
        #TODO make colornames parameterized

        self.colors=[]
        for i in range(7):
            colorname=colornames[i]
            jsonstring=self.redis.hget('flagcolor_description',colorname)
            print jsonstring
            self.colors.append(json.loads(jsonstring))

        self.define_feature('shape')
        print "==================="*10
        self.define_feature('division')
        self.define_feature('overlay')
        self.define_feature('symbol')
        self.define_feature('border')
        
    def define_feature(self,featurename):
        feature=getattr(self,featurename)
        print "This is featurename",feature
        keyname=''
        if 'name' in feature:
            keyname='flag'+featurename+'_'+feature['name']+"*"
        else:
            keyname='flag'+featurename+'_'+feature+"*"
            
        print "creating",keyname
        for newfeature in self.redis.keys(keyname):
            print "newfeature:",newfeature
            count=self.redis.llen(newfeature)-1
            featureoption=self.redis.lindex(newfeature, random.randint(0,count) )
            print "new option:",featureoption
            getattr(self,featurename )[newfeature]=featureoption


#        division diagquads
#    
#        name {'full': ''}
#        overlay stripe
#        color lightyellow
#        symbol letter
#    
#        color_description {u'verb': u'surpass', u'hex': u'ffff99', u'name': u'light yellow', u'adverb': u'happily'}
#    
#        shape {u'score': 90, u'name': u'swallow'}
#        border none
#        flag_shape_roll 85

    def get_json(self):
        jsonobj={}
        jsonobj['ratio']=self.ratio
        jsonobj['symbol']=self.symbol
        jsonobj['division']=self.division
        jsonobj['shape']=self.shape
        jsonobj['overlay']=self.overlay
        jsonobj['colors']=self.colors
        jsonobj['seed']=self.seed

        return json.dumps(jsonobj,ensure_ascii=True)
