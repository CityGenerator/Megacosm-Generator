#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Moon
import unittest2 as unittest

import fakeredis

from config import TestConfiguration


class TestMoon(unittest.TestCase):

    def setUp(self):
        """  """

        self.redis = fakeredis.FakeRedis()
        self.redis.zadd('moon_size', '{  "name":"massive", "multiplier":0.8 , "score":100  }', 100)
        self.redis.zadd('moon_color', '{  "name":"dull brown", "color":"0x876e4b" , "score":100  }', 100)
        self.redis.lpush('moonname_fullname_template', '{{params.pre}}{{params.root}}{{params.post}}')
        self.redis.lpush('moonname_shortname_template', '{{params.fullname}}')
        self.redis.lpush('moonname_formalname_template', '{{params.fullname}}')
        self.redis.lpush('moonname_pre', 'Hima')
        self.redis.lpush('moonname_root', 'la')
        self.redis.lpush('moonname_post', 'se')

    def tearDown(self):
        self.redis.flushall()

    def test_random_moon(self):
        """  """

        moon = Moon(self.redis)
        self.assertEqual('dull brown',moon.color['name'])
        self.assertEqual('massive', moon.size['name'])
        self.assertEqual('Himalase', moon.name.fullname)
