#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Cuisine
from megacosm.generators import Motivation
from megacosm.generators import Region
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser
import os
from megacosm.util.Seeds import *

from config import TestConfiguration


class TestCuisine(unittest.TestCase):

    def setUp(self):
        """  """

        self.redis = redis.from_url(TestConfiguration.REDIS_URL)
        self.region = Region(self.redis)

#        self.seed=set_seed( "3" )

    def test_random_cuisine(self):
        """  """

        cuisine = Cuisine(self.redis, {'region': self.region})
        print cuisine.text
        self.assertNotEqual(cuisine.text, '')


