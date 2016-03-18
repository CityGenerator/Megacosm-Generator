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
from pprint import pprint
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
    def tearDown(self):
        self.redis.flushall()

    def test_random_leader(self):
        """  """
        leader = Leader(self.redis)
        self.assertIn('Drucilla LaSalvae', str(leader))
        self.assertIn(str(leader.scope), ['country','region','city','organization'])


    def test_static_leader_country_scope(self):
        """  """
        leader = Leader(self.redis, {'scope':'country'})
        self.assertEqual('Queen Drucilla LaSalvae', str(leader))
        self.assertEqual('country', str(leader.scope))

    def test_static_leader_city_scope(self):
        """  """
        leader = Leader(self.redis, {'scope':'city'})
        self.assertEqual('Mayor Drucilla LaSalvae', str(leader))
        self.assertEqual('city', str(leader.scope))

    def test_static_leader_organization_scope(self):
        """  """
        leader = Leader(self.redis, {'scope':'organization'})
        self.assertEqual('Gang Leader Drucilla LaSalvae', str(leader))
        self.assertEqual('organization', str(leader.scope))


    def test_static_leader_bogus_scope(self):
        """  """
        self.redis.lpush('leader_kind', 'bogus')
        self.redis.lpush('leaderbogus_leader', 'bogusmaster')
        self.redis.hset('leader_kind_description', 'bogus', '{ "scope":"bogusscope"   }')
        self.redis.hset('leaderbogus_leader_description', 'bogusmaster', '{ "male":"Bogusmaster",    "female":"Bogusmaster"     }')
        leader = Leader(self.redis, {'scope':'bogus'})
        self.assertEqual('Bogusmaster Drucilla LaSalvae', str(leader))
        self.assertEqual('organization', str(leader.scope))

#
#    def test_static_leader_organization_scope(self):
#        """  """
#        leader = Leader(self.redis, {'scope':'organization'})
#        self.assertEqual('Bogusmaster Drucilla LaSalvae', str(leader))
#        self.assertEqual('organization', str(leader.scope))
#
