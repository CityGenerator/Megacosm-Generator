#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Leader
import unittest2 as unittest
from megacosm.generators import City
from megacosm.generators import Organization
from megacosm.generators import Country
import fakeredis
from config import TestConfiguration
import fixtures

class TestLeader(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        fixtures.npc.import_fixtures(self)
        fixtures.leader.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        fixtures.region.import_fixtures(self)
        fixtures.organization.import_fixtures(self)
        fixtures.business.import_fixtures(self)
        fixtures.country.import_fixtures(self)
        fixtures.city.import_fixtures(self)
        self.redis.lpush('npc_race','human')
        self.redis.lpush('leader_kind', 'guild')
    def test_random_leader(self):
        """  """
        leader = Leader(self.redis)
        self.assertEqual('Guildmaster Drucilla LaSalvae', str(leader))
        self.assertEqual('organization', str(leader.kind_description['scope']))


    def test_static_leader_location(self):
        """  """
        location=City(self.redis)
        leader = Leader(self.redis, {'location':location})
        self.assertEqual('Guildmaster Drucilla LaSalvae', str(leader))
        self.assertEqual('organization', str(leader.kind_description['scope']))
        self.assertIs(location, leader.location)

    def test_static_leader_country_scope(self):
        """  """
        self.redis.lpush('leader_kind', 'absolutemonarchy')
        leader = Leader(self.redis, {'kind':'absolutemonarchy'})
        self.assertEqual('Queen Drucilla LaSalvae', str(leader))
        self.assertEqual('country', str(leader.kind_description['scope']))

    def test_static_leader_city_scope(self):
        """  """
        self.redis.lpush('leader_kind', 'magistrate')
        leader = Leader(self.redis, {'kind':'magistrate'})
        self.assertEqual('Magistrate Drucilla LaSalvae', str(leader))
        self.assertEqual('city', str(leader.kind_description['scope']))

    def test_static_leader_organization_scope(self):
        """  """
        self.redis.lpush('leader_kind', 'guild')
        leader = Leader(self.redis, {'kind':'guild'})
        self.assertEqual('Guildmaster Drucilla LaSalvae', str(leader))
        self.assertEqual('organization', str(leader.kind_description['scope']))

