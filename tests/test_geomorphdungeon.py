#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators import GeomorphDungeon
import unittest2 as unittest

import fakeredis
from config import TestConfiguration
import fixtures
import json

class TestGeomorphDungeon(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        fixtures.dungeon.import_fixtures(self)
        fixtures.geomorphdungeon.import_fixtures(self)

    def tearDown(self):
        self.redis.flushall()

    def test_random_geomorphdungeon(self):
        """  """
        geomorphdungeon = GeomorphDungeon(self.redis)
        self.assertEqual('Lost Panopticon Of The King Of Chaos', str(geomorphdungeon))

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




