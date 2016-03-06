#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import GeomorphDungeon
import unittest2 as unittest

import fakeredis
from config import TestConfiguration
import json

class TestGeomorphDungeon(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        self.redis.zadd('geomorphdungeon_gridwidth', '{"name":"6",     "tiles":6,   "score": 100  }', 100)
        self.redis.zadd('geomorphdungeon_gridheight', '{"name":"4",    "tiles":4,    "score": 100  }', 100)
        self.redis.zadd('geomorphdungeon_segmentation', '{"name":"all",        "solidchance":0,        "score": 100  }', 100)
        self.redis.zadd('geomorphdungeon_decorationoffset', '{"name":"80%",   "offset":0.8,  "score":100 }', 100)
        self.redis.lpush('dungeon_template', '{{params.descriptor}} {{params.place}} of {{params.thing}}')
        self.redis.lpush('dungeon_place', 'panopticon')
        self.redis.lpush('dungeon_descriptor', 'lost')
        self.redis.lpush('dungeon_thingtype', 'king')
        self.redis.lpush('dungeon_thing', 'chaos')
        self.redis.lpush('geomorph_type_0', '{ "path":"/somewhere", "author":"someone", "tileset":"stone"   }' )
        self.redis.lpush('geomorph_type_1', '{ "path":"/somewhere", "author":"someone", "tileset":"stone"   }' )
        self.redis.lpush('geomorph_type_2', '{ "path":"/somewhere", "author":"someone", "tileset":"stone"   }' )
        self.redis.lpush('geomorph_type_3', '{ "path":"/somewhere", "author":"someone", "tileset":"stone"   }' )
        self.redis.lpush('geomorph_type_4', '{ "path":"/somewhere", "author":"someone", "tileset":"stone"   }' )
        self.redis.lpush('geomorph_type_5', '{ "path":"/somewhere", "author":"someone", "tileset":"stone"   }' )

    def tearDown(self):
        self.redis.flushall()

    def test_random_geomorphdungeon(self):
        """  """
        geomorphdungeon = GeomorphDungeon(self.redis)
        self.assertEqual('Lost Panopticon Of Chaos', str(geomorphdungeon))
    def test_static_text(self):
        """  """
        geomorphdungeon = GeomorphDungeon(self.redis,{'text':'You are a loser.'})
        self.assertEqual('You Are A Loser.', str(geomorphdungeon))

    def test_simplify_for_json(self):
        """  """
        geomorphdungeon = GeomorphDungeon(self.redis)
        json_structure=geomorphdungeon.simplify_for_json()
        self.assertEqual(type(json_structure), list)
        for row in json_structure:
            self.assertEqual(type(row), list)
            for tile in row:
                self.assertTrue(tile['path'])
                self.assertIn(tile['rotation'], [0,1,2,3])

#    def generate_grid(self):
#    def generate_connections(self):
#    def calculate_top(self, cell):
#    def calculate_right(self, cell):
#    def calculate_bottom(self, cell):
#    def calculate_left(self, cell):

#TODO test gridwith and gridheights

    def test_Tile_creation(self):
            tile=GeomorphDungeon.Tile(5,9)
            self.assertEqual(tile.left,None)
            self.assertEqual(tile.right,None)
            self.assertEqual(tile.top,None)
            self.assertEqual(tile.bottom,None)
            self.assertEqual(tile.char,'#')
            self.assertEqual(tile.x,5)
            self.assertEqual(tile.y,9)




