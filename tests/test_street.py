#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators import Street
import unittest2 as unittest
import fixtures
import fakeredis

from config import TestConfiguration

class TestStreet(unittest.TestCase):

    def setUp(self):
        self.redis = fakeredis.FakeRedis()
        fixtures.street.import_fixtures(self)

    def tearDown(self):
        self.redis.flushall()


    def test_random_street(self):
        """  """
        street = Street(self.redis)
        self.assertEqual('New Alba Byway', str(street))


