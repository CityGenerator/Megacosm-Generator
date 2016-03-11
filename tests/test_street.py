#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Street
import unittest2 as unittest

import fakeredis

from config import TestConfiguration

class TestStreet(unittest.TestCase):

    def setUp(self):
        self.redis = fakeredis.FakeRedis()
        self.redis.lpush('streetname_title','new')
        self.redis.lpush('streetname_root','alba')
        self.redis.lpush('streetname_trailer','byway')
        self.redis.lpush('streetname_fullname_template', '{{params.title}} {{params.root}} {{params.trailer}}')
        self.redis.lpush('streetname_shortname_template', '{{params.root}} {{params.trailer}}')
        self.redis.lpush('streetname_formalname_template', '{{params.fullname}}')

    def tearDown(self):
        self.redis.flushall()


    def test_random_street(self):
        """  """
        street = Street(self.redis)
        self.assertEqual('New Alba Byway', str(street))


