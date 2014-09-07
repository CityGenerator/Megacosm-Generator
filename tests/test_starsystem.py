#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import StarSystem
import unittest2 as unittest

import redis
from config import TestConfiguration


class TestStarSystem(unittest.TestCase):

    def setUp(self):
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_creation(self):
        """  """

        starsystem = StarSystem(self.redis, {'seed': 1007})
        self.assertTrue(starsystem.planet)

    def test_starcount(self):
        """ """

        stars = StarSystem(self.redis, {'seed': 1, 'starsystem_starcount_roll': 100})
        self.assertEqual(stars.seed, 1)
        self.assertEqual(len(stars.stars), 3)
