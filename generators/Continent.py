
from noise import snoise2
import math
import random
import json
from generators.Generator import Generator
from generators.Moon import Moon
import pprint

class Continent(Generator):
    WIDTH=500
    HEIGHT=500
    PIXEL_DEPTH=255.0
    SEALEVEL=135
    DEEPWATER=SEALEVEL*0.85
    DEEPESTWATER=SEALEVEL*0.65
    NOISEOCTAVES=6
    ZOOMFACTOR=100.0
    def __init__(self, redis, features={}):
        Generator.__init__(self,redis,features)

        self.generate_map()


    def generate_map(self):
        random.seed(self.seed)
        self.mapdata = []
        self.riversource=[]

        # Putting these here to improve readability and reduce calculations
        ymidpoint=self.HEIGHT/2
        xmidpoint=self.WIDTH/2

        for y in xrange(self.HEIGHT):
            row=[]

            # yEdgePenalty ranges from 2 on the edges to 0 in the middle
            yedgepenalty = math.fabs(   y - ymidpoint)/(self.HEIGHT/4)
            for x in xrange (self.WIDTH):

                # xEdgePenalty ranges from 2 on the edges to 0 in the middle
                xedgepenalty =  math.fabs(   x - xmidpoint)/(self.WIDTH/4)

                # Penalty range is 0.3 in the center to -1.3 on the edges
                # This keeps continents solid in the center, but  away from edges
                penalty=  min( .3, - math.hypot(yedgepenalty, xedgepenalty)+1.5)

                # Select the Perlin noise location, returning a -1.0 to 1.0 value for the height of the pixel
                heightnoise= snoise2(x/self.ZOOMFACTOR, y/self.ZOOMFACTOR, self.NOISEOCTAVES, 0.52,2.0, self.WIDTH/self.ZOOMFACTOR, self.HEIGHT/self.ZOOMFACTOR*10.0, self.seed/100.0 )

                # To fully understand the impact of the penalty equations, uncomment heightnoise
                #heightnoise=0

                # Select the Perlin noise location, returning a -1.0 to 1.0 value for the moisture of the pixel
                # Note that the height is shifted one screen so that moisture is not an exact match.
                moisturenoise= snoise2(x/self.ZOOMFACTOR, (self.HEIGHT+y)/self.ZOOMFACTOR, 5, 0.52,2.0, self.WIDTH/self.ZOOMFACTOR, self.HEIGHT/self.ZOOMFACTOR*10, (self.seed)/100.0 )


                #convert (-1.0 to 1.0)+ penalty to  (0 to 2). This allows for some slop, then cleans it up
                heightvalue  =  min(2,max(0,(heightnoise+1.0 + penalty ))) #range 0-2
                # convert from (0 to 2) to (0 to 255)
                heightvalue  = int((heightvalue/2.0) * self.PIXEL_DEPTH)


                moisturevalue=int((moisturenoise+1)/2*self.PIXEL_DEPTH-1)
                cell={'height': heightvalue, 'x':x, 'y':y, 'moisture':moisturevalue }
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
        cell['type']='ocean'
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



