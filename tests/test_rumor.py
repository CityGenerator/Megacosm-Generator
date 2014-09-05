#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Rumor
import unittest2 as unittest

import redis
from megacosm.util.Seeds import set_seed

from config import TestConfiguration


class TestRumor(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)
        self.seed = set_seed('3')

    def test_random_rumor(self):
        """  """
        rumor = Rumor(self.redis)
        self.assertNotEqual('', rumor.text)
