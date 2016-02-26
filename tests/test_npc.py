#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import NPC
import unittest2 as unittest
import redis
from megacosm.util.Seeds import set_seed
from config import TestConfiguration

class TestNPC(unittest.TestCase):

    def setUp(self):
        """  """

        self.redis = redis.from_url(TestConfiguration.REDIS_URL)
        self.seed = set_seed('3')

    def test_generated_race(self):
        """  """

        npc = NPC(self.redis)
        self.assertNotEqual('', npc.race)
        npc = NPC(self.redis, {})
        self.assertNotEqual('', npc.race)

    def test_races(self):
        """  """

        npc = NPC(self.redis, {'race': 'kobold'})
        self.assertEqual(npc.race, 'kobold')

        # FIXME: subraces broke this assertion
        # self.assertIn(npc.race, self.redis.lrange('npc_race',0,-1))

        with self.assertRaisesRegexp(Exception, 'turkeys is not a valid race and has no associated data'):
            npc = NPC(self.redis, {'race': 'turkeys'})

        npc = NPC(self.redis, {'race': 'human'})
        self.assertEqual(npc.race, 'human')

    def test_race_details(self):
        """  """

        npc = NPC(self.redis, {'race': 'human'})
        self.assertEqual(npc.race, 'human')

        self.assertEqual(npc.details['name'], 'Human')
        self.assertEqual(npc.details['size'], 'medium')
        self.assertEqual(npc.details['description'], 'quick growth and adaptability')

    def test_names(self):
        """  """

        npc = NPC(self.redis, {'race': 'human'})
        self.assertEqual(npc.race, 'human')
        self.assertRegexpMatches(npc.name['full'], '.+ .+')

    def test_phobias(self):
        """ Test NPC Phobias """
        npc = NPC(self.redis, {'race':'human'})
        self.assertNotEqual('',npc.race)
        self.assertNotEqual('',npc.phobia.text)
        self.assertIn('which is a fear of',npc.phobia.text)

    def test_motivation(self):
        """  """
        npc = NPC(self.redis)
        self.assertNotEqual('',npc.motivation.text)
