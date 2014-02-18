"""`MakeMap` Takes an object with Map Data and produces an image"""

# Import the stuffs!
from StringIO import StringIO
import png
import math


def generate_image(mapdata):
    """ Convert Cell colors to an actual image object"""
    COLORDEPTH=3 # RGB, no A
    image=[]
    for row in mapdata:
        imagerow=[]
        for cell in row:
            if (len(cell['color']) > COLORDEPTH):
                raise Exception("A Cell had more than 3 colors! ")
            imagerow.extend(cell['color'])
        image.append(imagerow)

    # Create a temp file for writing the image
    img_io = StringIO()

    # Convert the matrix of pixels into a png, then write it to the temp file
    imagewriter = png.Writer(len(image[0])/COLORDEPTH, len(image))
    imagewriter.write(img_io,image) 

    #ensure the image is properly flushed
    img_io.seek(0)

    return img_io

def generate_bump_image(mapdata):
    """ Convert Cell colors to an actual image object"""
    COLORDEPTH=3 # RGB, no A
    image=[]
    for row in mapdata:
        imagerow=[]
        for cell in row:
            if cell['bump'] > 120:
                print cell['bump']
            bumplevel=(cell['bump'],cell['bump'],cell['bump'])
            imagerow.extend(bumplevel)
        image.append(imagerow)

    # Create a temp file for writing the image
    img_io = StringIO()

    # Convert the matrix of pixels into a png, then write it to the temp file
    imagewriter = png.Writer(len(image[0])/COLORDEPTH, len(image))
    imagewriter.write(img_io,image) 

    #ensure the image is properly flushed
    img_io.seek(0)

    return img_io


def generate_specular_image(mapdata):
    """ Convert Cell colors to an actual image object"""
    COLORDEPTH=3 # RGB, no A
    image=[]
    for row in mapdata:
        imagerow=[]
        for cell in row:
            if cell['type'] == 'land' :
                imagerow.extend((0,0,0))
            else:
                imagerow.extend((255,255,255))
        image.append(imagerow)

    # Create a temp file for writing the image
    img_io = StringIO()

    # Convert the matrix of pixels into a png, then write it to the temp file
    imagewriter = png.Writer(len(image[0])/COLORDEPTH, len(image))
    imagewriter.write(img_io,image) 

    #ensure the image is properly flushed
    img_io.seek(0)

    return img_io


