#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Flaw
import unittest2 as unittest

import fakeredis
from config import TestConfiguration


class TestFlaw(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        self.redis.zadd('flaw_scope', '{ "name":"major"    , "score":100  }', 100)
        self.redis.zadd('flaw_quality', '{ "name":"poor"    , "score":100  }', 100)
        self.redis.lpush('flaw_allergy', 'horses')
        self.redis.lpush('flaw_enemytrait', 'vicious')
        self.redis.lpush('flaw_template', "You have {{params.scope['name']|article}} an allergy to {{params.allergy}}")

    def tearDown(self):
        self.redis.flushall()

    def test_random_flaw(self):
        """  """
        flaw = Flaw(self.redis)
        self.assertNotEquals('', flaw.text)
    def test_static_text(self):
        """  """
        flaw = Flaw(self.redis,{'text':'You are a loser.'})
        self.assertEquals('You are a loser.', str(flaw))
