#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fully test this module's functionality through the use of fixtures."""

from megacosm.generators.Leader import Leader
import unittest
import fakeredis
from fixtures import npc, leader, phobia, motivation, region, organization, business, country, city


class TestLeader(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        npc.import_fixtures(self)
        leader.import_fixtures(self)
        phobia.import_fixtures(self)
        motivation.import_fixtures(self)
        region.import_fixtures(self)
        organization.import_fixtures(self)
        business.import_fixtures(self)
        country.import_fixtures(self)
        city.import_fixtures(self)
        self.redis.lpush('npc_race', 'human')

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
