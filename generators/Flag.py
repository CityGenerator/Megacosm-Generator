
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

        #self.define_feature('shape')
        print "==================="*10

        #self.define_feature('division')
        #self.define_feature('overlay')
        #self.define_feature('symbol')
        #self.define_feature('border')
        
    def define_feature(self,featurename):
        feature=getattr(self,featurename)

        keyname='flag'+featurename+'_'+feature['name']+"*"
            
        print "creating",keyname
        for newfeature in self.redis.keys(keyname):
            count=self.redis.llen(newfeature)-1
            featureoption=self.redis.lindex(newfeature, random.randint(0,count) )
            
            print "setting ",newfeature,"for",featurename,"to", featureoption

            getattr(self,featurename )[newfeature]=featureoption


    def get_json(self):
        jsonobj={}
#        jsonobj['color']=self.color
#        jsonobj['ratio']=self.ratio['name']
#        jsonobj['symbol']['radius_direction']
#
# "symbol":{"radius_direction":"horizontal","xlocation":".25","radius":".15","letter":"N","name":"circle","outline":"true","ylocation":".25"},"division":{"count":"3","side":"vertical","name":"stripes","color_count":"2"},"shape":{"name":"para"},"overlay":{"direction":"right-to-left","width":"0.2","name":"slash"},"shape_roll":52,"
#
#
#
# border {u'name': u'none'}
#    
#        symbol_circle_radiusdirection vertical
#    
#        overlay_circle_outlinewidth 1
#    
#        symbol_circle_outline true
#    
#        overlay_jack_horlength 1
#    
#        overlay_cross_vertwidth 0.1
#    
#        border_solid_size .08
#    
#        symbol_letter_y .25
#    
#        symbol_letter_x .5
#    
#        overlay_jack_width 0.05
#    
#        shape {u'score': 70, u'name': u'tri'}
#    
#        seed 79065
#    
#        overlay_diamond_outline true
#    
#        overlay_circle_outline false
#    
#        overlay_cross_horpos 0.33
#    
#        division_stripes_count 2
#    
#        overlay_jack_horwidth 0.10
#    
#        overlay_circle_x .5
#    
#        overlay_circle_y 1
#    
#        division_stripes_side horizontal
#    
#        overlay_cross_horwidth 0.3
#    
#        division_stripes_colorcount 3
#    
#        shape_swallow_depth 30
#    
#        overlay_x_width 0.2
#    
#        redis Redis<ConnectionPool<Connection<host=127.0.0.1,port=6379,db=0>>>
#    
#        overlay_rays_y 0
#    
#        overlay_rays_x 1
#    
#        symbol_circle_radius .20
#    
#        symbol_star_points 5
#    
#        overlay_asterisk_outline false
#    
#        symbol_letter_size .30
#    
#        shape_tongued_count 5
#    
#        symbol_letter_fontfamily Impact
#    
#        symbol_circle_y .25
#    
#        symbol_circle_x .5
#    
#        flag_shape_roll 67
#    
#        overlay_quaddiag_side east
#    
#        overlay_cross_vertlength 0.8
#    
#        division {u'name': u'diagonal'}
#    
#        overlay_rays_count 15
#    
#        overlay_jack_horpos 0.5
#    
#        shape_tongued_depth 0.1
#    
#        flag_symbol_roll 70
#    
#        symbol {u'name': u'star'}
#    
#        overlay_jack_vertlength 1
#    
#        flag_overlay_roll 25
#    
#        overlay_jack_vertwidth 0.2
#    
#        overlay_quad_side ne
#    
#        overlay {u'name': u'stripe'}
#    
#        overlay_jack_outline true
#    
#        division_diagonal_direction left-to-right
#    
#        shape_tongued_shape scallop
#    
#        overlay_x_outline true
#    
#        overlay_slash_width 0.2
#    
#        overlay_rays_offset .25
#    
#        name {'full': ''}
#    
#        overlay_stripe_count 13
#    
#        overlay_slash_direction right-to-left
#    
#        symbol_star_inset .33
#    
#        overlay_stripe_side horizontal
#    
#        overlay_circle_radius 2
#    
#        flag_division_roll 66
#    
#        flag_border_roll 9
#    
#        symbol_star_y .25
#    
#        symbol_star_x .25
#    
#        overlay_cross_horlength 0.3
#    
#        overlay_circle_radiusdirection vertical


        return jsonobj
