#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Moon
import unittest2 as unittest

import fakeredis

from config import TestConfiguration


class TestMoon(unittest.TestCase):

    def setUp(self):
        """  """

        self.redis = fakeredis.FakeRedis()
        self.redis.zadd('moon_size', '{  "name":"massive", "multiplier":0.8 , "score":100  }', 100)
        self.redis.zadd('moon_color', '{  "name":"dull brown", "color":"0x876e4b" , "score":100  }', 100)

    def tearDown(self):
        self.redis.flushall()

    def test_random_moon(self):
        """  """

        moon = Moon(self.redis)
        self.assertNotEqual(moon.color, '')
        self.assertNotEqual(moon.size, '')
