#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Organization
import unittest2 as unittest
from megacosm.generators import Leader
import fakeredis
from config import TestConfiguration
import fixtures
from pprint import pprint

class TestOrganization(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        fixtures.organization.import_fixtures(self)
        fixtures.npc.import_fixtures(self)
        fixtures.leader.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        fixtures.region.import_fixtures(self)
        fixtures.country.import_fixtures(self)
        fixtures.city.import_fixtures(self)
        fixtures.business.import_fixtures(self)

        self.redis.lpush('npc_race','gnome')

    def tearDown(self):
        self.redis.flushall()

    def test_random_organization(self):
        """  """
        organization = Organization(self.redis)
        self.assertEquals("Tom's Crime Ring", organization.text)
        self.assertEquals("The Crime Ring", str(organization))
        self.assertIsInstance(organization.leader, Leader)

    def test_static_organization(self):
        """  """
        leader = Leader(self.redis)
        organization = Organization(self.redis,{'leader': leader, 'text':"boooyah"})
        self.assertEquals(leader, organization.leader)
        self.assertEquals("boooyah", organization.text)
