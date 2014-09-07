#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Star
import unittest2 as unittest

import redis

from config import TestConfiguration


class TestStar(unittest.TestCase):

    def setUp(self):
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_creation(self):
        """  """

        star = Star(self.redis)
        self.assertNotEquals('', star.name)
