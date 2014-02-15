
from noise import snoise2
import math
import random
import json
from generators.Generator import Generator
from generators.Moon import Moon
import pprint

class Planet(Generator):
    WIDTH=500
    HEIGHT=300
    PIXEL_DEPTH=255.0
    SEALEVEL=135
    DEEPWATER=SEALEVEL*0.85
    DEEPESTWATER=SEALEVEL*0.65
    NOISEOCTAVES=6
    ZOOMFACTOR=100.0
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis,features)

        self.generate_map()
        self.generate_moons()


    def generate_map(self):
        random.seed(self.seed)
        self.mapdata = []
        self.riversource=[]
        for y in xrange(self.HEIGHT):
            row=[]
            latitude=math.fabs(self.HEIGHT/2.0-y) *(180.0/self.HEIGHT)
            for x in xrange (self.WIDTH):
                heightnoise= snoise2(x/self.ZOOMFACTOR, y/self.ZOOMFACTOR, self.NOISEOCTAVES, 0.52,2.0, self.WIDTH/self.ZOOMFACTOR, self.HEIGHT/self.ZOOMFACTOR*10.0, self.seed/100.0 )
                moisturenoise= snoise2(x/self.ZOOMFACTOR, (self.HEIGHT+y)/self.ZOOMFACTOR, 5, 0.52,2.0, self.WIDTH/self.ZOOMFACTOR, self.HEIGHT/self.ZOOMFACTOR*10, (self.seed)/100.0 )
                #convert 1.0...-1.0 to 255...0
                heightvalue  =int((heightnoise  +1)/2*self.PIXEL_DEPTH-1)
                moisturevalue=int((moisturenoise+1)/2*self.PIXEL_DEPTH-1)
                cell={'height': heightvalue, 'x':x, 'y':y, 'moisture':moisturevalue, 'latitude':latitude }
                if (heightvalue < self.SEALEVEL):
                    cell=self.colorize_ocean(cell)
                else:
                    cell=self.colorize_land(cell)
                    if (random.randint(0,10000) <5):
                        cell['riverhead']=True
                        self.riversource.append(cell)
                row.append( cell )
            self.mapdata.append(row)


    def colorize_land(self,cell):
        cell['type']='land'
        cell['color']=( cell['height'],cell['height'],cell['height'] )
        return cell

    def colorize_ocean(self,cell):
        cell['type']='water'
        colorrange=50         #range of color that the water can show
        bluemultiplier=1.5    #RGB's B is 1.5x more affected.
        darkestblue=self.PIXEL_DEPTH-colorrange*bluemultiplier   # Darkest blue is the pixeldepth minus the blue colorrange
    
        if (cell['height'] < self.DEEPESTWATER):
            cell['color']=(0,0,int(darkestblue)) # Deepest dark water
        elif (cell['height'] < self.DEEPWATER and cell['height'] >self.DEEPESTWATER):
            #colors in this range should be 0-50 because that provides the best color range.
            mod=(cell['height']-self.DEEPESTWATER)/(self.DEEPWATER-self.DEEPESTWATER)*colorrange
            cell['color']=(int(0+mod),int(0+mod),int(darkestblue+(mod*bluemultiplier))) # Deep
        else:
            cell['color']=(colorrange,colorrange,int(self.PIXEL_DEPTH)) # Shallow
        return cell



    def generate_moons(self):
        """ Generate a list of moons """
        self.moons=[]
        for moonId in xrange(self.mooncount['count']):
            self.moons.append(Moon(self.redis ))
