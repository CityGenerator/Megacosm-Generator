#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import redis
import glob
import sys
import json
from config import BaseConfiguration
import re

COMMANDCOUNT = 0

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def parse_file(pipe, filename):
    linenumber = 0
    global COMMANDCOUNT
    raw_data = open(filename)
    for line in raw_data:
        
        linenumber += 1
        line = line.rstrip()
        if line:

            # print line

            if line.startswith('#'):
                continue
            else:
                if not is_ascii( line):
                    raise Exception('line #%s in %s contains invalid unicode characters.' % (linenumber, filename))
                COMMANDCOUNT += 1
                (command, args) = line.split(' ', 1)
                command = command.upper()
                try:
                    if command == 'SET':
                        (key, value) = args.split(None, 1)
                        pipe.set(key, value)
                    elif command == 'LPUSH':

                        # print "setting", key, "to", value

                        (key, value) = args.split(' ', 1)
                        pipe.lpush(key, value)
                    elif command == 'ZADD':
                        (key, score, value) = args.split(None, 2)
                        jsontxt=validate_json(value, filename, linenumber)
                        if not jsontxt.has_key('score'):
                            print "Warning: Score isn't a parameter of jsontxt: %s: %s %s" % (key, score, value)
                        elif int(score) != int(jsontxt['score']):
                            print "Warning: Score is invalid for %s: %s == %s" % (key, score, jsontxt['score'])
                        if not jsontxt.has_key('name'):
                            print "Warning: Name is missing from %s: %s %s" % (key, score, value)
                        pipe.zadd(key, value, score)
                    elif command == 'HSET':
                        (name, key, value) = args.split(None, 2)
                        validate_json(value, filename, linenumber)
                        pipe.hset(name, key, value)
                    elif command == 'DEL':
                        pipe.delete(args)
                    else:

                        # print "I have no idea what ", line, "is."

                        raise Exception('line #%s in %s: %s is an unsupported command.' % (linenumber, filename,
                                        command))
                except ValueError:
                    print 'There was a problem reading', filename, 'near line', linenumber, ''
    raw_data.close()


JSONVALIDATE = 0


def validate_json(value, filename, linenumber):
    global JSONVALIDATE
    try:
        jsontxt=json.loads(value)
        JSONVALIDATE += 1
        return jsontxt
    except Exception:
        print 'ERROR: The following value is not proper JSON:'
        print filename, 'near line', linenumber, ':'
        print value
        sys.exit(1)

server = redis.from_url(BaseConfiguration.REDIS_URL)
pipe = server.pipeline()

pipe.flushall()

for filename in sorted(glob.glob('data/*.data')):
    parse_file(pipe, filename)

for filename in sorted(glob.glob('data/*/*.data')):
    parse_file(pipe, filename)

IMAGECOUNT = 0


def create_geomorphimage_record(pipe, image):
    m = re.search('geomorphs/(.*)/(.*)/([0-5])/.*\.png', image)
    global IMAGECOUNT
    if m:
        author = m.group(1)
        tileset = m.group(2)
        imagetype = m.group(3)
        pipe.lpush('geomorph_type_' + imagetype, ' { "path":"/%s", "author":"%s", "tileset":"%s"   }' % (image, author,
                   tileset))
        IMAGECOUNT += 1
    else:
        print 'WARNING, ', image, 'is not in the right format.'


# static/images/geomorphs/1/basic2.png

for image in glob.glob('megacosm/static/images/geomorphs/*/*/*/*.png'):
    image = image[9:]
    create_geomorphimage_record(pipe, image)


def create_dungeonbackground_record(pipe, image):
    m = re.search('backgrounds/(.*)\.png', image)
    global IMAGECOUNT
    if m:
        tilename = m.group(1)
        pipe.lpush('geomorphdungeon_background', tilename)
        IMAGECOUNT += 1
    else:
        print 'WARNING, ', image, 'is not in the right format.'


for image in sorted(glob.glob('megacosm/static/images/backgrounds/*.png')):
    image = image[9:]
    create_dungeonbackground_record(pipe, image)

pipe.set('geomorphdungeon_decoration_chance', 30)


def create_dungeondecoration_record(pipe, image):
    image = image[9:]
    m = re.search('decorations/(.*)\.png', image)
    global IMAGECOUNT
    if m:
        tilename = m.group(1)
        pipe.lpush('geomorphdungeon_decoration', tilename)
        IMAGECOUNT += 1
    else:
        print 'WARNING, ', image, 'is not in the right format.'


for image in sorted(glob.glob('megacosm/static/images/decorations/*.png')):
    image = image[9:]
    create_dungeondecoration_record(pipe, image)

pipe.execute()

print COMMANDCOUNT, 'Commands were run.'
print IMAGECOUNT, 'geomorphs documented.'
print JSONVALIDATE, 'JSON strings validated.'
