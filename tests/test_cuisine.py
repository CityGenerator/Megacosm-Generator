#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Cuisine
from megacosm.generators import Region
import unittest2 as unittest

import redis
from config import TestConfiguration


class TestCuisine(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)
        self.region = Region(self.redis)

    def test_random_cuisine(self):
        """  """

        cuisine = Cuisine(self.redis, {'region': self.region})
        print cuisine.text
        self.assertNotEqual('', cuisine.text)
