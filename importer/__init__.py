#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re


class Importer(object):
    """ Import data"""

    def __init__(self, pipe):
        self.command_count = 0
        self.json_validate = 0
        self.image_count = 0
        self.pipe = pipe
        self.pipe.flushall()
        print("importing stuff.")

    def parse_data_file(self, file_to_parse):
        linenumber = 0
        raw_data = open(file_to_parse)
        for line in raw_data:
            linenumber += 1
            line = line.rstrip()

            if line:
                if line.startswith('#') or re.match('^\\s*$', line):
                    continue
                else:
                    try:
                        Importer.is_ascii(line)
                        self.command_count += 1
                        (command, args) = line.split(' ', 1)
                        command = command.upper()
                        if command == 'SET':
                            self.process_set(args)
                        elif command == 'LPUSH':
                            (key, value) = args.split(' ', 1)
                            self.pipe.lpush(key, value)
                        elif command == 'ZADD':
                            self.process_zadd(args)
                        elif command == 'HSET':
                            self.process_hset(args)
                        elif command == 'DEL':
                            self.pipe.delete(args)
                        else:
                            raise Exception('line #%s in %s: %s is an unsupported command.' %
                                            (linenumber, file_to_parse, command))
                    except ValueError as e:
                        print(e)
                        print("This was near line %s in %s" % (linenumber, file_to_parse))
        self.pipe.execute()
        raw_data.close()

    def process_set(self, args):
        (key, value) = args.split(None, 1)
        self.pipe.set(key, value)

    def process_hset(self, args):
        (name, key, value) = args.split(None, 2)
        self.validate_json(value)
        self.pipe.hset(name, key, value)

    def process_zadd(self, args):
        (key, score, value) = args.split(None, 2)
        jsontxt = self.validate_json(value)
        if 'score' not in jsontxt:
            print("Warning: Score isn't a parameter of jsontxt: %s: %s %s" % (key, score, value))
        elif int(score) != int(jsontxt['score']):
            print("Warning: Score is invalid for %s: %s == %s" % (key, score, jsontxt['score']))
        if 'name' not in jsontxt:
            print("Warning: Name is missing from %s: %s %s" % (key, score, value))
        self.pipe.zadd(key, {value: score})

    def validate_json(self, value):
        try:
            jsontxt = json.loads(value)
            self.json_validate += 1
            return jsontxt
        except json.JSONDecodeError:
            print('ERROR: The following value is not proper JSON:')
            print(value)
            raise json.JSONDecodeError

    def create_geomorphimage_record(self, image_name):
        m = re.search('geomorphs/(.*)/(.*)/([0-5])/.*\\.png', image_name)
        if m:
            author = m.group(1)
            tileset = m.group(2)
            imagetype = m.group(3)
            self.pipe.lpush('geomorph_type_' + imagetype,
                            ' { "path":"/%s", "author":"%s", "tileset":"%s"   }' % (image_name, author, tileset))
            self.image_count += 1
        else:
            print('WARNING, ', image_name, 'is not in the right format.')
        self.pipe.execute()

    def create_dungeonbackground_record(self, image_name):
        m = re.search('backgrounds/(.*)\\.png', image_name)
        if m:
            tilename = m.group(1)
            self.pipe.lpush('geomorphdungeon_background', tilename)
            self.image_count += 1
        else:
            print('WARNING, ', image_name, 'is not in the right format.')
        self.pipe.execute()

    def create_dungeondecoration_record(self, image_name):
        image_name = image_name[9:]
        m = re.search('decorations/(.*)\\.png', image_name)
        if m:
            tilename = m.group(1)
            self.pipe.lpush('geomorphdungeon_decoration', tilename)
            self.image_count += 1
        else:
            print('WARNING, ', image_name, 'is not in the right format.')
        self.pipe.execute()

    @staticmethod
    def is_ascii(s):
        if not all(ord(char) < 128 for char in s):
            raise ValueError("'%s' contains an invalid character")
