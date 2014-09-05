#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Country
import unittest2 as unittest

import redis
from config import TestConfiguration


class TestCountry(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_random_country(self):
        """  """
        country = Country(self.redis)
        self.assertNotEqual('', country.name)

    def test_country_region(self):
        """  """

        country = Country(self.redis, {'regioncount': 25})
        country.add_regions()
        self.assertNotEqual('', country.name)

        self.assertEqual(25, len(country.regions))
