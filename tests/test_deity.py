#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Deity
import unittest2 as unittest

import redis
from config import TestConfiguration


class TestDeity(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_deity(self):
        """  """
        deity = Deity(self.redis)
        self.assertNotEqual('', deity.name)

    def test_deity_sects(self):
        """  """

        deity = Deity(self.redis, {'deity_unity_roll': 100, 'deity_importance_roll': 100})
        deity.add_sects()
        self.assertEqual(len(deity.sects), 0)

        deity = Deity(self.redis, {'deity_unity_roll': 0, 'deity_importance_roll': 100})
        deity.add_sects()
        self.assertGreaterEqual(len(deity.sects), 1)
