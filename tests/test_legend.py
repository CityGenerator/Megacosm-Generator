#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators.Legend import Legend
from megacosm.generators.NPC import NPC
import unittest2 as unittest
import fixtures
import fakeredis
from config import TestConfiguration


class TestLegend(unittest.TestCase):

    def setUp(self):
        """  """

        self.redis = fakeredis.FakeRedis(decode_responses=True)
        fixtures.npc.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        fixtures.legend.import_fixtures(self)
        self.redis.lpush('npc_race','gnome') 

    def tearDown(self):
        self.redis.flushall()

    def test_random_legend(self):
        """  """
        legend = Legend(self.redis)
        self.assertEqual('In olden times, a devil named Tom Gyro haunted the swamps when the wind blows from the west and was drawn towards thieves. People say that if you confront her, you will be stricken blind unless you offer a sacrifice.', str(legend))

    def test_legend_static_npc(self):
        """  """
        npc=NPC(self.redis)
        villian=NPC(self.redis)
        villian.name.fullname="jango fett"
        legend = Legend(self.redis, {'npc':npc, 'villain':villian})
        self.assertIn(villian.name.fullname, legend.text)

    def test_legend_static_text(self):
        """  """
        legend = Legend(self.redis, {'text':'something spooky'})
        self.assertNotEqual('something spooky', str(legend))
