#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Phobia
import unittest2 as unittest

import redis
from config import TestConfiguration


class TestPhobia(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)
        
    def test_random_phobia(self):
        """  """
        phobia = Phobia(self.redis)
        self.assertNotEquals('', phobia.text)

