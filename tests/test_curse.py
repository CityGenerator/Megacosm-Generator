#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Curse
import unittest2 as unittest

import fakeredis
import fixtures
from megacosm.util.Seeds import set_seed

from config import TestConfiguration


class TestCurse(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        fixtures.curse.import_fixtures(self)
    def tearDown(self):
        self.redis.flushall()

    def test_random_curse(self):
        """  """
        curse = Curse(self.redis)
        self.assertNotEqual('', curse.text)
        self.assertNotEqual('', curse.removal)
        self.assertNotEqual('', curse.duration)
        self.assertNotEqual('', curse.kind)
    def test_static_features(self):
        """  """
        curse = Curse(self.redis, {'kind': 'bezerker', 'removal':'a remove curse spell', 'template': "The {{params.kind_description['name']|title}} Curse {{params.kind_description['description']}}."})
        #pprint(vars(curse))
        self.assertEqual("causes intermittent, uncontrollable rage in the victim", curse.kind_description['description'])
        self.assertEqual('a remove curse spell', curse.removal)
        self.assertEqual('bezerker', curse.kind)
        self.assertIn('params.kind_description', curse.template)
        self.assertIn('Bezerker Curse', curse.text)
        self.assertNotIn('Bezerker Curse', curse.template)

    def test_static_text(self):
        """  """
        curse = Curse(self.redis, {'text': "Nothing of value"})
        #pprint(vars(curse))
        self.assertEqual('Nothing of value', curse.text)
        self.assertEqual('Nothing of value', str(curse) )
