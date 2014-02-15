"""`Worldmap` is dedicated to drawing the world map."""

# Import the stuffs!
from noise import snoise2, snoise3, snoise4
from generators.Star import Star
from generators.Planet import Planet
from StringIO import StringIO
import png
import math
import random
#import pprint


WIDTH=400
HEIGHT=250
PIXEL_DEPTH=255.0
SEALEVEL=135
DEEPWATER=SEALEVEL*0.85
DEEPESTWATER=SEALEVEL*0.65
NOISEOCTAVES=6


def colorize_map(mapdata):
    """ Convert the black and white pixel data to actual map-looking colors."""
    image=[]
    for row in mapdata:
        imagerow=[]
        for cell in row:
            pixel=cell['height'];
            color=(pixel,pixel,pixel) # land
            if (cell['type'] is 'water'):
                color=colorize_ocean(pixel)
#          elif ('riverhead' in cell):
#                color=(255,0,0)

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

def colorize_ocean(pixel):
    """ Convert the black and white pixel data to actual ocean colors if below SEALEVEL."""
    # Caution, voodoo math ahead.
    colorrange=50         #range of color that the water can show
    bluemultiplier=1.5    #RGB's B is 1.5x more affected.
    darkestblue=PIXEL_DEPTH-colorrange*bluemultiplier   # Darkest blue is the pixeldepth minus the blue colorrange

    if (pixel < DEEPESTWATER):
        color=(0,0,int(darkestblue)) # Deepest dark water
    elif (pixel < DEEPWATER and pixel >DEEPESTWATER):
        #colors in this range should be 0-50 because that provides the best color range.
        mod=(pixel-DEEPESTWATER)/(DEEPWATER-DEEPESTWATER)*colorrange
        color=(int(0+mod),int(0+mod),int(darkestblue+(mod*bluemultiplier))) # Deep
    else:
        color=(colorrange,colorrange,int(PIXEL_DEPTH)) # Shallow
    return color


def bump_map(mapdata):
    """ Convert the black and white pixel data to actual map-looking colors."""
    image=[]
    for row in mapdata:
        imagerow=[]
        for cell in row:
            pixel=cell['height'];
            color=(0,0,0) # land
            if (pixel >SEALEVEL):
                pixel=int( (pixel-SEALEVEL)/(PIXEL_DEPTH-SEALEVEL) *PIXEL_DEPTH)
                color=(pixel,pixel,pixel) #water is flat

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

def specular_map(mapdata):
    """ Convert the black and white pixel data to actual map-looking colors."""
    image=[]
    for row in mapdata:
        imagerow=[]
        for cell in row:
            pixel=cell['height'];
            color=(255,255,255) # land
            if (pixel >= SEALEVEL):
                color=(0,0,0) #water is flat

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
