#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators import Resource, Region
import unittest2 as unittest
import fixtures
import fakeredis
from config import TestConfiguration


class TestResource(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        fixtures.resource.import_fixtures(self)
        fixtures.region.import_fixtures(self)
    def tearDown(self):
        self.redis.flushall()

    def test_random_resource(self):
        """  """
        resource = Resource(self.redis)
        self.assertNotEquals('', resource.text)

    def test_static_text(self):
        """  """
        resource = Resource(self.redis,{'text':'static resource text'})
        self.assertEquals('Static resource text', str(resource))

    def test_static_region(self):
        """  """
        region=Region(self.redis)
        resource = Resource(self.redis,{'place':region})
        self.assertEquals(str(region), str(region))
