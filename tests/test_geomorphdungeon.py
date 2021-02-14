#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

import sys
import fixtures
import json
import fakeredis
import unittest2 as unittest
from megacosm.generators import GeomorphDungeon


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
        gd = GeomorphDungeon(self.redis)
        self.assertEqual('Lost Panopticon Of The King Of Chaos', str(gd.name))
        self.assertEqual('Lost Panopticon Of The King Of Chaos', str(gd))
        self.assertEqual(6, gd.width)
        self.assertEqual(4, gd.height)


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

    def test_generate_grid(self):
        gd = GeomorphDungeon(self.redis, {'height':8, 'width':7})
        gd.grid=None
        self.assertEqual(None, gd.grid)
        self.assertEqual(7, gd.width)
        self.assertEqual(8, gd.height)

        gd.generate_grid()
        self.assertEqual(8, len(gd.grid))
        self.assertEqual(7, len(gd.grid[0]))
        for row in gd.grid:
            for tile in row:
                self.assertIsInstance(tile,GeomorphDungeon.Tile)

    def test_generate_connections(self):
        gd = GeomorphDungeon(self.redis)
        self.assertEqual(gd.width*gd.height, len(gd.alltiles))

    def test_calculate_defaults(self):
        """ Ensure that Connections behave as expected. """
        gd = GeomorphDungeon(self.redis, {'height':2, 'width':2})

        gd.grid=None
        gd.generate_grid()
        gd.calculate_top(gd.grid[0][0])
        self.assertEqual(False, gd.grid[0][0].top)
        gd.calculate_left(gd.grid[0][0])
        self.assertEqual(False, gd.grid[0][0].left)
        gd.calculate_right(gd.grid[0][0])
        self.assertEqual(True, gd.grid[0][0].right)
        gd.calculate_bottom(gd.grid[0][0])
        self.assertEqual(True, gd.grid[0][0].bottom)

        gd.grid=None
        gd.generate_grid()
        gd.calculate_top(gd.grid[1][1])
        self.assertEqual(True, gd.grid[1][1].top)
        gd.calculate_left(gd.grid[1][1])
        self.assertEqual(True, gd.grid[1][1].left)
        gd.calculate_right(gd.grid[1][1])
        self.assertEqual(False, gd.grid[1][1].right)
        gd.calculate_bottom(gd.grid[1][1])
        self.assertEqual(False, gd.grid[1][1].bottom)


        gd = GeomorphDungeon(self.redis, {'height':2, 'width':2, 'segmentation':{'name':'none', 'connection_chance':0, 'score':0}})

        gd.grid=None
        gd.generate_grid()
        gd.calculate_top(gd.grid[0][0])
        self.assertEqual(False, gd.grid[0][0].top)
        gd.calculate_left(gd.grid[0][0])
        self.assertEqual(False, gd.grid[0][0].left)
        gd.calculate_right(gd.grid[0][0])
        self.assertEqual(False, gd.grid[0][0].right)
        gd.calculate_bottom(gd.grid[0][0])
        self.assertEqual(False, gd.grid[0][0].bottom)

        gd.grid=None
        gd.generate_grid()
        gd.calculate_top(gd.grid[1][1])
        self.assertEqual(False, gd.grid[1][1].top)
        gd.calculate_left(gd.grid[1][1])
        self.assertEqual(False, gd.grid[1][1].left)
        gd.calculate_right(gd.grid[1][1])
        self.assertEqual(False, gd.grid[1][1].right)
        gd.calculate_bottom(gd.grid[1][1])
        self.assertEqual(False, gd.grid[1][1].bottom)


    def test_calculate_static_true(self):
        """ Ensure that Connections behave as expected. """
        gd = GeomorphDungeon(self.redis, {'height':2, 'width':2})
        gd.grid=None
        gd.generate_grid()
        gd.calculate_top(gd.grid[0][0], True)
        self.assertEqual(True, gd.grid[0][0].top)
        gd.calculate_left(gd.grid[0][0], True)
        self.assertEqual(True, gd.grid[0][0].left)
        gd.calculate_right(gd.grid[0][0], True)
        self.assertEqual(True, gd.grid[0][0].right)
        gd.calculate_bottom(gd.grid[0][0], True)
        self.assertEqual(True, gd.grid[0][0].bottom)

        gd.grid=None
        gd.generate_grid()
        gd.calculate_top(gd.grid[1][1], True)
        self.assertEqual(True, gd.grid[1][1].top)
        gd.calculate_left(gd.grid[1][1], True)
        self.assertEqual(True, gd.grid[1][1].left)
        gd.calculate_right(gd.grid[1][1], True)
        self.assertEqual(True, gd.grid[1][1].right)
        gd.calculate_bottom(gd.grid[1][1], True)
        self.assertEqual(True, gd.grid[1][1].bottom)

    def test_calculate_static_false(self):
        """ Ensure that Connections behave as expected. """
        gd = GeomorphDungeon(self.redis, {'height':2, 'width':2})
        gd.grid=None
        gd.generate_grid()
        gd.calculate_top(gd.grid[0][0], False)
        self.assertEqual(False, gd.grid[0][0].top)
        gd.calculate_left(gd.grid[0][0], False)
        self.assertEqual(False, gd.grid[0][0].left)
        gd.calculate_right(gd.grid[0][0], False)
        self.assertEqual(False, gd.grid[0][0].right)
        gd.calculate_bottom(gd.grid[0][0], False)
        self.assertEqual(False, gd.grid[0][0].bottom)

        gd.grid=None
        gd.generate_grid()
        gd.calculate_top(gd.grid[1][1], False)
        self.assertEqual(False, gd.grid[1][1].top)
        gd.calculate_left(gd.grid[1][1], False)
        self.assertEqual(False, gd.grid[1][1].left)
        gd.calculate_right(gd.grid[1][1], False)
        self.assertEqual(False, gd.grid[1][1].right)
        gd.calculate_bottom(gd.grid[1][1], False)
        self.assertEqual(False, gd.grid[1][1].bottom)

    def test_generate_tiletype(self):
        """ Testing the top row's tile types because that should be sufficient."""
        gd = GeomorphDungeon(self.redis, {'height':3, 'width':3})
        #Top Left should only have connections on the bottom and right, aka a 2-sided adjacent with one rotation.
        self.assertEqual(0b110, int(gd.grid[0][0].tiletype,2))
        self.assertEqual(0b0010, gd.grid[0][0].imagetype)

        #Top middle should have connections on the bottom, left and right, aka a 3-sided with one rotation.
        self.assertEqual(0b1110, int(gd.grid[0][1].tiletype,2))
        self.assertEqual(0b0100, gd.grid[0][1].imagetype)

        #Top right should only have connections on the bottom and left, aka a 2-sided adjacent with two rotations.
        self.assertEqual(0b1100, int(gd.grid[0][2].tiletype,2))
        self.assertEqual(0b0010, gd.grid[0][2].imagetype)


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




