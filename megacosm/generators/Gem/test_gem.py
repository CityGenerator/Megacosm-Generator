#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fully test this module's functionality through the use of fixtures."""

from megacosm.generators.Gem import Gem
import unittest

import fakeredis
from fixtures import gem

class TestGem(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        gem.import_fixtures(self)

    def tearDown(self):
        self.redis.flushall()

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

