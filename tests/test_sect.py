#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Sect, Deity
import unittest2 as unittest
import fixtures
import fakeredis
from megacosm.util.Seeds import set_seed

from config import TestConfiguration


class TestSect(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis=fakeredis.FakeRedis()
        fixtures.npc.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.deity.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        self.redis.lpush('npc_race','gnome')

    def tearDown(self):
        self.redis.flushall()

    def test_random_sect(self):
        """  """
        sect = Sect(self.redis)
        self.assertNotEqual(sect.domain, '')

    def test_static_sect(self):
        """  """
	deity=Deity(self.redis)
        sect = Sect(self.redis, {'deity':deity})
        self.assertNotEqual(sect.domain, '')
        self.assertIn(sect.domain, deity.portfolios)

    def test_static_domain(self):
        """  """
        sect = Sect(self.redis, {'domain':'tacos'})
        self.assertEqual(sect.domain, 'tacos')
