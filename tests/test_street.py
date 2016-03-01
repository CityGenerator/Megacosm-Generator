#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Street
import unittest2 as unittest

import fakeredis

from config import TestConfiguration

class TestStreet(unittest.TestCase):

    def setUp(self):
        self.redis = fakeredis.FakeRedis()
        self.redis.lpush('name_streettitle','new')
        self.redis.lpush('name_streetroot','alba')
        self.redis.lpush('street_kind', 'byway')

    def tearDown(self):
        self.redis.flushall()


    def test_random_street(self):
        """  """
        street = Street(self.redis)
        self.assertEqual('New Alba Byway', street.name['full'])


    def test_random_stree_trailer(self):
        """  """
        self.redis.lpush('name_streettrailer','alley')
        street = Street(self.redis)
        self.assertEqual('New Alba Alley', street.name['full'])
