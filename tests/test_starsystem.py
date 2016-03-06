#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import StarSystem,Planet, Star
import unittest2 as unittest

import fakeredis
from mock import Mock, patch, MagicMock

from config import TestConfiguration


class TestStarSystem(unittest.TestCase):

    def setUp(self):
    	self.redis = fakeredis.FakeRedis()
        self.redis.zadd('starsystem_starcount',  '{ "name":"binary star",  "count":2, "score":100  }',100.0)

        self.redis.lpush('starposition', '{"name": "companion",    "x":-150,    "y":4,  "z":4  }' )
        self.redis.lpush('starposition', '{"name": "companion2",    "x":-150,    "y":-4,  "z":4  }' )
        self.redis.zadd('planet_mooncount','{"name":"no moons",     "count":0,  "score":100   }',100.0)

    def tearDown(self):
        self.redis.flushall()

    def test_creation(self):
        """  """

        starsystem = StarSystem(self.redis,{})
        self.assertTrue(starsystem.planet)
        self.assertEqual(2, len(starsystem.stars))

