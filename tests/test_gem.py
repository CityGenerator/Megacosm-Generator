#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Gem
import unittest2 as unittest

import redis
from config import TestConfiguration


class TestGem(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_random_gem(self):
        """  """
        gem = Gem(self.redis)
        self.assertNotEquals('', gem.text)
        self.assertNotEquals('', gem.count)
        self.assertNotEquals('', gem.color)
        self.assertNotEquals('', str(gem))

    def test_static_gem(self):
        """  """
        gem = Gem(self.redis, {'text':'foo bar', 'count':3, 'color':'green'})
        self.assertEqual('Foo bar', gem.text)
        self.assertEqual(3, gem.count)
        self.assertEqual('green', gem.color)

