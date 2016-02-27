#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Adventure
import unittest2 as unittest

import redis
from config import TestConfiguration


class TestAdventure(unittest.TestCase):

    def setUp(self):
        """  """

        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_random_adventure(self):
        """  """
        adventure = Adventure(self.redis)
        self.assertNotEqual('', adventure.kind)
        self.assertNotEqual('', adventure.mcguffin)
        self.assertNotEqual('', adventure.theme)

