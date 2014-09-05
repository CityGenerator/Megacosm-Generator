#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Continent
import unittest2 as unittest

import redis
from config import TestConfiguration


class TestContinent(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_random_continent(self):
        """  """
        continent = Continent(self.redis)
        continent.add_countries()
        self.assertGreaterEqual(len(continent.countries), 0)

    def test_continent_country(self):
        """  """
        continent = Continent(self.redis, {'countrycount': 25})
        continent.add_countries()
        self.assertEqual(len(continent.countries), 25)
