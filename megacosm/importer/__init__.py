#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import re


class Importer(object):
    """ Import data"""

    def __init__(self, redis_server):
        self.command_count = 0
        self.json_validate = 0
        self.image_count = 0
        self.pipe = redis_server.pipeline()
        self.pipe.flushall()
        print("importing stuff.")

    @staticmethod
    def is_ascii(text):
        return lambda s: len(s) == len(s.encode())
#        return all(ord(c) < 128 for c in text)

    def parse_data_file(self, file_to_parse):
        linenumber = 0
        raw_data = open(file_to_parse)
        for line in raw_data:

            linenumber += 1
            line = line.rstrip()
            if line:

                # print(line)

                if line.startswith('#'):
                    continue
                else:
                    if not Importer.is_ascii(line):
                        raise Exception('line #%s in %s contains invalid unicode characters.' %
                                        (linenumber, file_to_parse))
                    self.command_count += 1
                    (command, args) = line.split(' ', 1)
                    command = command.upper()
                    try:
                        if command == 'SET':
                            (key, value) = args.split(None, 1)
                            self.pipe.set(key, value)
                        elif command == 'LPUSH':

                            # print("setting", key, "to", value)

                            (key, value) = args.split(' ', 1)
                            self.pipe.lpush(key, value)
                        elif command == 'ZADD':
                            (key, score, value) = args.split(None, 2)
                            jsontxt = self.validate_json(value, file_to_parse, linenumber)
                            if 'score' not in jsontxt:
                                print("Warning: Score isn't a parameter of jsontxt: %s: %s %s" % (key, score, value))
                            elif int(score) != int(jsontxt['score']):
                                print("Warning: Score is invalid for %s: %s == %s" % (key, score, jsontxt['score']))
                            if 'name' not in jsontxt:
                                print("Warning: Name is missing from %s: %s %s" % (key, score, value))
                            from pprint import pprint
                            self.pipe.zadd(key, {value: score})
                        elif command == 'HSET':
                            (name, key, value) = args.split(None, 2)
                            self.validate_json(value, file_to_parse, linenumber)
                            self.pipe.hset(name, key, value)
                        elif command == 'DEL':
                            self.pipe.delete(args)
                        else:

                            # print("I have no idea what ", line, "is.")

                            raise Exception('line #%s in %s: %s is an unsupported command.' % (linenumber,
                                                                                               file_to_parse,
                                                                                               command))
                    except ValueError:
                        print('There was a problem reading', file_to_parse, 'near line', linenumber, '')
        raw_data.close()

    def validate_json(self, value, json_file, linenumber):
        try:
            jsontxt = json.loads(value)
            self.json_validate += 1
            return jsontxt
        except json.JSONDecodeError:
            print('ERROR: The following value is not proper JSON:')
            print(json_file, 'near line', linenumber, ':')
            print(value)
            sys.exit(1)

    def create_geomorphimage_record(self, gimage):
        m = re.search('geomorphs/(.*)/(.*)/([0-5])/.*\\.png', gimage)
        if m:
            author = m.group(1)
            tileset = m.group(2)
            imagetype = m.group(3)
            self.pipe.lpush('geomorph_type_' + imagetype,
                            ' { "path":"/%s", "author":"%s", "tileset":"%s"   }' % (gimage, author, tileset))
            self.image_count += 1
        else:
            print('WARNING, ', gimage, 'is not in the right format.')

    def create_dungeonbackground_record(self, dbg_image):
        m = re.search('backgrounds/(.*)\\.png', dbg_image)
        if m:
            tilename = m.group(1)
            self.pipe.lpush('geomorphdungeon_background', tilename)
            self.image_count += 1
        else:
            print('WARNING, ', dbg_image, 'is not in the right format.')

    def create_dungeondecoration_record(self, dd_image):
        dd_image = dd_image[9:]
        m = re.search('decorations/(.*)\\.png', dd_image)
        if m:
            tilename = m.group(1)
            self.pipe.lpush('geomorphdungeon_decoration', tilename)
            self.image_count += 1
        else:
            print('WARNING, ', dd_image, 'is not in the right format.')
