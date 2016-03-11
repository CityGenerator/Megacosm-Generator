#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Star
import unittest2 as unittest

import fakeredis

from config import TestConfiguration

class TestStar(unittest.TestCase):

    def setUp(self):
        self.redis = fakeredis.FakeRedis()
        self.redis.lpush('starname_fullname_template', '{{params.pre}}{{params.root}}{{params.post}}')
        self.redis.lpush('starname_shortname_template', '{{params.fullname}}')
        self.redis.lpush('starname_formalname_template', '{{params.fullname}}')
        self.redis.lpush('starname_pre', 'Kro')
        self.redis.lpush('starname_root', 'j')
        self.redis.lpush('starname_post', 'el')

    def tearDown(self):
        self.redis.flushall()

    def test_creation(self):
        """  """

        star = Star(self.redis)
        self.assertEqual('Krojel', str(star.name))
