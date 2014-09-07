#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import City, Region
import unittest2 as unittest
from mock import Mock
import redis
from config import TestConfiguration


class TestCity(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_random_city(self):
        """  """
        city = City(self.redis)
        self.assertNotEqual('', city.name)
        self.assertEquals(city.name['full'], "%s" % city)

    def test_city_region(self):
        """  """
        city = City(self.redis, {'region': Mock(Region)})
        self.assertNotEqual('', city.name)
