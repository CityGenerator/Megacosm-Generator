#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Star
import unittest2 as unittest

import fakeredis

from config import TestConfiguration

class TestStar(unittest.TestCase):

    def setUp(self):
        self.redis = fakeredis.FakeRedis()

    def tearDown(self):
        self.redis.flushall()

    def test_creation(self):
        """  """

        star = Star(self.redis)
        self.assertNotEquals('', star.name)
