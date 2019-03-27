#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators.Deity import Deity
from megacosm.generators.Sect import Sect
import unittest2 as unittest
import fixtures
import fakeredis
from megacosm.util.Seeds import set_seed

from config import TestConfiguration


class TestSect(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis=fakeredis.FakeRedis(decode_responses=True)
        fixtures.npc.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.deity.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        fixtures.sect.import_fixtures(self)
        self.redis.lpush('npc_race','gnome')

    def tearDown(self):
        self.redis.flushall()

    def test_random_sect(self):
        """  """
        sect = Sect(self.redis)
        self.assertIn('name',sect.domain)
        self.assertEqual('Order of the Oreibalic',str(sect) )

    def test_static_sect(self):
        """  """
        deity=Deity(self.redis)
        sect = Sect(self.redis, {'deity':deity})
        self.assertIn('name',sect.domain)
        self.assertIn(sect.domain, deity.portfolios)

#    def test_static_domain(self):
#        """  """
#        sect = Sect(self.redis, {'domain':'tacos'})
#        self.assertEqual(sect.domain, 'tacos')
