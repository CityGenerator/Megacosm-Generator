#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Planet
import unittest2 as unittest

import redis
from config import TestConfiguration


class TestPlanet(unittest.TestCase):

    def setUp(self):
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_creation(self):
        """  """
        planet = Planet(self.redis, {'seed': 1007})
        self.assertNotEquals('', planet.name)

    def test_randomseed(self):
        planet = Planet(self.redis)
        self.assertNotEquals('', planet.name)
