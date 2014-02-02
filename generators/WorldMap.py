"""`Worldmap` is dedicated to drawing the world map."""

# Import the stuffs!
from noise import snoise2, snoise3, snoise4
from StringIO import StringIO
import png
import random


import redis


def generate_name(worldId,server):
    random.seed(worldId)
    name = server.lindex('worldnamepre',  random.randint(0,server.llen('worldnamepre')-1 ))
    name+= server.lindex('worldnameroot', random.randint(0,server.llen('worldnameroot')-1 ))
    name+= server.lindex('worldnamepost', random.randint(0,server.llen('worldnamepost')-1 ))
    
    return name



def generate_map(worldId=0,width=800,height=500,xoffset=0.0,yoffset=0.0,zoom=1.0):
    """ Return a simple matrix of simplex noise from 0-255."""
    mapdata = []
    print worldId
    zoom=zoom * 100.0
    for x in xrange(height):
        row=[]
        for y in xrange (width):
            xparam=float((x+xoffset)/zoom)
            yparam=float((y+yoffset)/zoom)
            noisevalue=snoise2(xparam, yparam,  6, 0.52,2.0, height/zoom*2, width/zoom, float(worldId) )
            pixel=int((noisevalue+1)/2*255-1)
            row.append(pixel)
        mapdata.append(row)
    return mapdata

def colorize_map(mapdata):
    """ Convert the black and white pixel data to actual map-looking colors."""
    image=[]
    waterline=145
    for row in mapdata:
        imagerow=[]
        for y in row:
            pixel=y;
            color=(pixel,pixel,pixel) # land
            if (pixel < waterline-50):
                color=(0,0,205) # Deepest
            elif (pixel <waterline-15):
                color=(10,10,255) # Deep
            elif (pixel <waterline):
                color=(55,55,255) # Shallow
            #Note that this is actually tripling the width of the array for RGB values.
            imagerow.extend(color)
        image.append(imagerow)
    # Create a temp file for writing the image
    img_io = StringIO()

    # Convert the matrix of pixels into a png, then write it to the temp file
    imagewriter = png.Writer(len(image[0])/3, len(image))
    imagewriter.write(img_io,image) 

    #ensure the image is properly flushed
    img_io.seek(0)

    return img_io






#json_data=open('data/worldnames.json')
#data = json.load(json_data)
#
##pprint(data)
#for feature in data:
#    if (feature.find("_chance") != -1 ):
#        server.set('worldname'+feature, data[feature])
#    else:
#        featurelist=data[feature]
#        server.sadd('worldname'+feature, *featurelist)
#
#    
# 
#print server.srandmember('worldnamepre')+server.srandmember('worldnameroot')+server.srandmember('worldnamepost')
#
#
#
#json_data.close()
#
