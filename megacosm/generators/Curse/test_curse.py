#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators.Curse import Curse
import unittest

import fakeredis
from fixtures import curse


class TestCurse(unittest.TestCase):

    def setUp(self):
        """ Set up the required fixtures """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        curse.import_fixtures(self)

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
