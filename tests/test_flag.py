#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Flag
import unittest2 as unittest

import redis
from config import TestConfiguration


class TestFlag(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_random_flag(self):
        """  """
        flag = Flag(self.redis)
        self.assertNotEqual('', flag.letter)
        self.assertNotEqual('', flag.shape)
        self.assertNotEqual('', flag.shape_swallow_depth)
        self.assertNotEqual('', flag.shape_tongued_shape)
        self.assertNotEqual('', flag.shape_tongued_count)
        self.assertNotEqual('', flag.shape_tongued_depth)
        self.assertNotEqual('', flag.ratio['name'])
        self.assertNotEqual('', flag.division['name'])
        self.assertNotEqual('', flag.division_diagonal_direction)
        self.assertNotEqual('', flag.division_stripes_side)
        self.assertNotEqual('', flag.division_stripes_count)
        self.assertNotEqual('', flag.division_stripes_colorcount)
        self.assertNotEqual('', flag.overlay['name'])
        self.assertNotEqual('', flag.overlay_quaddiag_side)
        self.assertNotEqual('', flag.overlay_quad_side)
        self.assertNotEqual('', flag.overlay_stripe_side)
        self.assertNotEqual('', flag.overlay_stripe_count)
        self.assertNotEqual('', flag.overlay_slash_direction)
        self.assertNotEqual('', flag.overlay_slash_width)
        self.assertNotEqual('', flag.overlay_x_outline)
        self.assertNotEqual('', flag.overlay_x_width)
        self.assertNotEqual('', flag.symbol['name'])
        self.assertNotEqual('', flag.border['name'])

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

