#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Loot, Gem, Artwork, Currency, MundaneItem, MagicItem
import unittest2 as unittest

import redis
from config import TestConfiguration


class TestLoot(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_random_Loot(self):
        """  """
        loot= Loot(self.redis)
        self.assertNotEqual('', loot.kind)
        self.assertNotEqual('', loot.kind_description)

