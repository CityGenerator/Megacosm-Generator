"""`Worldmap` is dedicated to drawing the world map."""

# Import the stuffs!
from noise import snoise2, snoise3, snoise4
from StringIO import StringIO
import png
import random
#import pprint


WIDTH=400
HEIGHT=250
PIXEL_DEPTH=255.0
SEALEVEL=135
DEEPWATER=SEALEVEL*0.85
DEEPESTWATER=SEALEVEL*0.65
NOISEOCTAVES=6

def generate_name(worldId,server):
    random.seed(worldId)
    #FIXME this is friggen manual as hell and needs refactoring to use chances
    name = server.lindex('worldnamepre',  random.randint(0,server.llen('worldnamepre')-1 ))
    name+= server.lindex('worldnameroot', random.randint(0,server.llen('worldnameroot')-1 ))
    name+= server.lindex('worldnamepost', random.randint(0,server.llen('worldnamepost')-1 ))
    return name

def generate_map(worldId=0,width=WIDTH,height=HEIGHT,xoffset=0.0,yoffset=0.0,zoom=1.0):
    """ Return a simple matrix of simplex noise from 0-255."""
    mapdata = []
    random.seed(worldId)
    zoom=zoom * 100.0
    riversource=[]
    for x in xrange(height):
        row=[]
        for y in xrange (width):
            xparam=float((x+xoffset)/zoom)
            yparam=float((y+yoffset)/zoom)
            noisevalue=snoise2(xparam, yparam,  NOISEOCTAVES, 0.52,2.0, height/zoom*2, width/zoom, float(worldId) )
            #convert 1.0...-1.0 to 255...0
            pixel=int((noisevalue+1)/2*PIXEL_DEPTH-1)
            cell={'height': pixel, 'x':x, 'y':y }
            if (pixel < SEALEVEL):
                cell['type']='water'
            else:
                cell['type']='land'
                if (random.randint(0,10000) <5):
                    cell['riverhead']=True
                    riversource.append(cell)
                    
            row.append( cell )
        mapdata.append(row)


    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(riversource) 
    return mapdata

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
    waterline=145
    for row in mapdata:
        imagerow=[]
        for cell in row:
            pixel=cell['height'];
            color=(255,255,255) # land
            if (pixel >= waterline):
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
