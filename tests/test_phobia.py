#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Phobia
import unittest2 as unittest
import fakeredis
from config import TestConfiguration


class TestPhobia(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        self.redis.lpush('phobia_template', 'You have {{params.strength["name"]}} {{params.kind_description["name"]}}, which is a fear of {{params.kind_description["description"]}}.')
        self.redis.zadd('phobia_strength', '{"name":"moderate",  "score":100    }', 100)
        self.redis.lpush('phobia_kind', 'ablutophobia')
        self.redis.hset('phobia_kind_description', 'ablutophobia', '{"name":"Ablutophobia",       "description":"washing or bathing" }')


    def tearDown(self):
        self.redis.flushall()
        
    def test_random_phobia(self):
        """  """
        phobia = Phobia(self.redis)
        self.assertEquals('You have moderate Ablutophobia, which is a fear of washing or bathing.', str(phobia))

    def test_static_text(self):
        """  """
        phobia = Phobia(self.redis, {'text': 'You have Tacophobia, which is a fear of tacos.'})
        self.assertEquals('You have Tacophobia, which is a fear of tacos.', str(phobia))

