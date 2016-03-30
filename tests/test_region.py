#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators import Region
import unittest2 as unittest
import fakeredis
from config import TestConfiguration
import fixtures

class TestRegion(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        fixtures.region.import_fixtures(self)

    def test_random_region(self):
        """  """
        region = Region(self.redis)
        self.assertEqual('New Lombardy', str(region))


