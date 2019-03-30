#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import argparse
import redis
from config import BaseConfiguration
from importer import Importer



parser = argparse.ArgumentParser(usage="Import Megacosm data into Redis")

parser.add_argument('-r', '--redishost', help='host to connect to.', default='localhost')
parser.add_argument('-p', '--redisport', help='host port to connect to.', default=6379)

args = parser.parse_args()

BaseConfiguration.REDIS = redis.Redis(host=args.redishost, port=int(args.redisport), decode_responses=True)


server = BaseConfiguration.REDIS
pipe = server.pipeline()

pipe.flushall()

imp = Importer(server)

for filename in sorted(glob.glob('data/**/*.data', recursive=True)):
    imp.parse_data_file(filename)

for image in glob.glob('megacosm/static/images/geomorphs/*/*/*/*.png'):
    image = image[9:]
    imp.create_geomorphimage_record(image)

for image in sorted(glob.glob('megacosm/static/images/backgrounds/*.png')):
    image = image[9:]
    imp.create_dungeonbackground_record(image)

pipe.set('geomorphdungeon_decoration_chance', 30)

for image in sorted(glob.glob('megacosm/static/images/decorations/*.png')):
    image = image[9:]
    imp.create_dungeondecoration_record(image)

pipe.execute()

print(imp.command_count, 'Commands were run.')
print(imp.image_count, 'geomorphs documented.')
print(imp.json_validate, 'JSON strings validated.')
