#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import NPC, Phobia, Motivation
import unittest2 as unittest
import fakeredis
import fixtures
from megacosm.util.Seeds import set_seed
from config import TestConfiguration

class TestNPC(unittest.TestCase):

    def setUp(self):
        """  """

        self.redis = fakeredis.FakeRedis()
        fixtures.npc.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)

    def tearDown(self):
        self.redis.flushall()

    def test_generated_race(self):
        """  """
	# only human is in the npc_race array
	self.redis.lpush('npc_race','human')

        npc = NPC(self.redis)
        self.assertEqual('human', npc.race)
        npc = NPC(self.redis, {})
        self.assertEqual('human', npc.race)

    def test_races(self):
        """  """
	self.redis.lpush('npc_race','kobold')

        npc = NPC(self.redis, {'race': 'kobold'})
        self.assertIn('kobold', npc.race)
        self.assertEqual('Kole',npc.name.fullname)

        with self.assertRaisesRegexp(Exception, 'turkeys is not a valid race and has no associated data'):
            npc = NPC(self.redis, {'race': 'turkeys'})

    def test_race_details(self):
        """  """
	self.redis.lpush('npc_race','human')

        npc = NPC(self.redis, {'race': 'human'})
        self.assertEqual(npc.race, 'human')

        self.assertEqual(npc.details['name'], 'Human')
        self.assertEqual(npc.details['size'], 'medium')
        self.assertEqual(npc.details['description'], 'quick growth and adaptability')

    def test_names(self):
        """  """
	self.redis.lpush('npc_race','human')
	self.redis.lpush('humanname_title', 'Lady')
	self.redis.lpush('humanname_trailer', 'Esq.')

        npc = NPC(self.redis, {'race': 'human'})
        self.assertEqual(npc.race, 'human')
        self.assertEqual('Lady Drucilla LaSalvae Esq.',npc.name.fullname)
        self.assertEqual('Lady Drucilla LaSalvae Esq.',str(npc))

    def test_phobias(self):
        """ Test NPC Phobias """
	#Our Static Phobia
	phobia = Phobia(self.redis)
	self.redis.lpush('npc_race','human')

        npc = NPC(self.redis, {'race':'human'})
        self.assertNotEqual('',npc.race)
        self.assertNotEqual('',npc.phobia.text)
	#This should be random, not our static
        self.assertNotEqual(phobia ,npc.phobia)
        self.assertEqual('You have moderate Ablutophobia, which is a fear of washing or bathing.',npc.phobia.text)


        npc = NPC(self.redis, {'race':'human','phobia':phobia})
	#This should be our static Phobia
        self.assertEqual(phobia ,npc.phobia)
        self.assertEqual('You have moderate Ablutophobia, which is a fear of washing or bathing.',npc.phobia.text)


    def test_motivations(self):
        """ Test NPC Motivations """
	#Our Static Motivation
	self.redis.lpush('npc_race','human')
	self.redis.lpush('npc_race','kobold')

	motivation = Motivation(self.redis)

        npc = NPC(self.redis, {'race':'human'})
        self.assertNotEqual('',npc.race)
        self.assertNotEqual('',npc.motivation.text)
	#This should be random, not our static
        self.assertNotEqual(motivation ,npc.motivation)
        self.assertEqual('to impress someone',npc.motivation.text)

        npc = NPC(self.redis, {'race':'human','motivation':motivation})
	#This should be our static Motivation
        self.assertEqual(motivation ,npc.motivation)
        self.assertEqual('to impress someone',npc.motivation.text)

