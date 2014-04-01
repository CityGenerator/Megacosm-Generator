#!/usr/bin/python

import redis
import ConfigParser, os
import glob
import sys
from pprint import pprint
import re


COMMANDCOUNT=0

def parse_file(pipe, filename):
    linenumber=0
    global COMMANDCOUNT
    raw_data=open(filename)
    for line in raw_data:
        linenumber+=1
        line=line.rstrip()
        if line:
            #print line
            if line.startswith('#'):
                continue;
            else:
                COMMANDCOUNT+=1
                command, args = line.split(' ',1)
                command=command.upper()
                try:
                    if command == 'SET':
                        key,value=args.split(None,1)
                        pipe.set(key,value)
                        #print "setting",key,"to",value
                    elif command == "LPUSH":
                        key,value=args.split(' ',1)
                        pipe.lpush(key,value)
                    elif command == "ZADD":
                        key,score,value=args.split(None,2)
                        pipe.zadd(key,value,score)
                    elif command == "HSET":
                        name,key,value=args.split(None,2)
                        pipe.hset(name,key,value)
                    elif command == "DEL":
                        pipe.delete(args)
                    else:
                        #print "I have no idea what ",line,"is."
                        raise Exception("line #%s in %s: %s is an unsupported command." % (linenumber, filename, command) )
                except ValueError:
                    print "There was a problem reading",filename,"near line",linenumber,""
    raw_data.close()



config = ConfigParser.RawConfigParser()
config.read('data/config.ini')

url = config.get('redis', 'url')

server=redis.from_url(url)
pipe=server.pipeline()

pipe.flushall()

for filename in glob.glob("data/*.data") :
    parse_file(pipe, filename)

for filename in glob.glob("data/*/*.data") :
    parse_file(pipe, filename)


IMAGECOUNT=0
def create_geomorphimage_record(pipe, image):
    m = re.search('geomorphs/(.*)/(.*)/([0-5])/.*\.png', image)
    global IMAGECOUNT
    if m:
        author = m.group(1)
        tileset = m.group(2)
        imagetype = m.group(3)
        pipe.lpush('geomorph_type_'+imagetype,' { "path":"/%s", "author":"%s", "tileset":"%s"   }' % (image, author,tileset )  )
        IMAGECOUNT+=1
    else:
        print "WARNING,",image,"is not in the right format."
#static/images/geomorphs/1/basic2.png

for image in glob.glob("static/images/geomorphs/*/*/*/*.png") :
    create_geomorphimage_record(pipe, image);






def create_dungeonbackground_record(pipe, image):
    m = re.search('backgrounds/(.*)\.png', image)
    global IMAGECOUNT
    if m:
        tilename = m.group(1)
        pipe.lpush('geomorphdungeon_background' ,tilename  )
        IMAGECOUNT+=1
    else:
        print "WARNING,",image,"is not in the right format."

for image in glob.glob("static/images/backgrounds/*.png") :
    create_dungeonbackground_record(pipe, image);





pipe.execute()

print COMMANDCOUNT, "Commands were run."
print IMAGECOUNT, "geomorphs documented."


