#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators.Motivation import Motivation
from megacosm.generators.NPC import NPC
import unittest
import fixtures
import fakeredis

from config import TestConfiguration


class TestMotivation(unittest.TestCase):

    def setUp(self):
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        fixtures.motivation.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.npc.import_fixtures(self)
        self.redis.lpush('npc_race','gnome')

    def tearDown(self):
        self.redis.flushall()

    def test_random_motivation(self):
        """  """

        motivation = Motivation(self.redis)
        self.assertNotEqual(motivation.text, '')

    def test_motivation_w_npc(self):
        """  """

        npc = NPC(self.redis)
        motivation = Motivation(self.redis, {'npc': npc})
        self.assertNotEqual(motivation.text, '')
        self.assertEqual(motivation.npc, npc)
        self.assertNotEqual('%s' % motivation, '')

    def test_motivation_w_fear(self):
        """  """

        npc = NPC(self.redis)
        motivation = Motivation(self.redis, {'npc': npc, 'kind': 'fear'})
        self.assertNotEqual(motivation.text, '')
        self.assertEqual(motivation.npc, npc)
        self.assertNotEqual('%s' % motivation, '')
