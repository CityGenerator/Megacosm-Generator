#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Gem
import unittest2 as unittest

import fakeredis
from config import TestConfiguration


class TestGem(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        self.redis.hset('gem_kind_description', 'zircon', '{ "name":"zircon", "color":["blue","orange","red","white","yellow"]   }')
        self.redis.lpush('gem_cut', 'trillion')
        self.redis.lpush('gem_kind', 'zircon')
        self.redis.lpush('gem_template', 'You find {{params.amount["name"]}} {{params.quality["name"]}} {{params.cut}} {{params.kind_description["name"]|pluralize(params.count)}}. The color is {{params.saturation["name"]}} {{params.color}}. {{"This"| plural_adj(params.count)}} {{"gem"| pluralize(params.count)}} {{"is"| plural_verb(params.count)}} {{params.value["name"]}}.')
        self.redis.zadd('gem_amount', '{ "name":"a large pile of",    "min":30,   "max":120,  "score":100 }', 100)
        self.redis.zadd('gem_quality', '{ "name":"perfect"     , "score":100  }', 100)
        self.redis.zadd('gem_saturation', '{ "name":"vibrant",     "score":100 }', 100)
        self.redis.zadd('gem_value', '{ "name":"worth a king\'s ransom",    "score":100  }', 100)

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

