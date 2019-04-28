#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators.Flag import Flag
import unittest
import string
import fakeredis
from fixtures import flag


class TestFlag(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        flag.import_fixtures(self)

    def tearDown(self):
        self.redis.flushall()

    def test_random_flag(self):
        """  """
        flag = Flag(self.redis)
        self.assertIn( flag.letter, string.ascii_uppercase)
        self.assertEqual('tongued', flag.shape['name'])
        self.assertEqual('30', flag.shape_swallow_depth)
        self.assertEqual('scallop', flag.shape_tongued_shape)
        self.assertEqual('11', flag.shape_tongued_count)
        self.assertEqual('0.2', flag.shape_tongued_depth)
        self.assertEqual('2.55', flag.ratio['name'])
        self.assertEqual('stripes', flag.division['name'])
        self.assertEqual('left-to-right', flag.division_diagonal_direction)
        self.assertEqual('horizontal', flag.division_stripes_side)
        self.assertEqual('3', flag.division_stripes_count)
        self.assertEqual('2', flag.division_stripes_colorcount)
        self.assertEqual('rays', flag.overlay['name'])
        self.assertEqual('letter', flag.symbol['name'])
        self.assertEqual('solid', flag.border['name'])

    def test_random_flag_colors(self):
        """  """
        flag = Flag(self.redis)
        self.assertNotEqual('', flag.letter)
        self.assertEqual(7, len(flag.colors))
        self.assertNotEqual('', flag.colors[1]['adverb'])
        self.assertNotEqual('', flag.colors[1]['hex'])
        self.assertNotEqual('', flag.colors[1]['verb'])
        self.assertNotEqual('', flag.colors[1]['name'])

    def test_static_flag_colors(self):
        """  """
        flag = Flag(self.redis, {'colors': [{ "name":"light grey",        "hex":"#cccccc",  "verb":"wonder",     "adverb":"cautiously"   } ]})
        self.assertNotEqual('', flag.letter)
        self.assertEqual(7, len(flag.colors))
        self.assertEqual('cautiously', flag.colors[0]['adverb'])
        self.assertEqual('#cccccc', flag.colors[0]['hex'])
        self.assertEqual('wonder', flag.colors[0]['verb'])
        self.assertEqual('light grey', flag.colors[0]['name'])

    def test_static_flag_letter(self):
        """  """
        flag = Flag(self.redis, {'letter':'L'})
        self.assertEqual('L', flag.letter)

    def test_static_flag(self):
        """  """
        flag = Flag(self.redis, {'overlay_stripe_side':'vertical'})
        self.assertIn('vertical', flag.tojson())

