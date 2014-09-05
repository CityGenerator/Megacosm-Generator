#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Moon
import unittest2 as unittest

import redis

from config import TestConfiguration


class TestMoon(unittest.TestCase):

    def setUp(self):
        """  """

        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_random_moon(self):
        """  """

        moon = Moon(self.redis)
        self.assertNotEqual(moon.color, '')
        self.assertNotEqual(moon.size, '')
