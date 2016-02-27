#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Curse
import unittest2 as unittest

import redis
from megacosm.util.Seeds import set_seed

from config import TestConfiguration


class TestCurse(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_random_curse(self):
        """  """
        curse = Curse(self.redis)
        self.assertNotEqual('', curse.text)
        self.assertNotEqual('', curse.removal)
        self.assertNotEqual('', curse.duration)
        self.assertNotEqual('', curse.kind)
    def test_static_features(self):
        """  """
        curse = Curse(self.redis, {'kind': 'greed', 'curse_duration_roll':5, 'removal':'a remove curse spell', 'template': "The {{params.kind_description['name']|title}} Curse {{params.kind_description['description']}}."})
        #pprint(vars(curse))
        self.assertEqual("causes the victim to take unnecessary risks for treasure", curse.kind_description['description'])
        self.assertEqual('a remove curse spell', curse.removal)
        self.assertEqual('appear intermittently', curse.duration['name'])
        self.assertEqual('greed', curse.kind)
        self.assertIn('params.kind_description', curse.template)
        self.assertIn('Greed Curse', curse.text)
        self.assertNotIn('Greed Curse', curse.template)

    def test_static_text(self):
        """  """
        curse = Curse(self.redis, {'text': "Nothing of value"})
        #pprint(vars(curse))
        self.assertEqual('Nothing of value', curse.text)
        self.assertEqual('Nothing of value', str(curse) )
