#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators import Moon
import unittest2 as unittest

import fakeredis
import fixtures
from config import TestConfiguration


class TestMoon(unittest.TestCase):

    def setUp(self):
        """  """

        self.redis = fakeredis.FakeRedis()
        fixtures.moon.import_fixtures(self)

    def tearDown(self):
        self.redis.flushall()

    def test_random_moon(self):
        """  """

        moon = Moon(self.redis)
        self.assertEqual('dull brown',moon.color['name'])
        self.assertEqual('massive', moon.size['name'])
        self.assertEqual('Himalase', str(moon))
