#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import JobPosting, NPC
import unittest2 as unittest
import fixtures
import fakeredis
from config import TestConfiguration


class TestJobPosting(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        fixtures.jobposting.import_fixtures(self)
        fixtures.business.import_fixtures(self)
        fixtures.npc.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)

        self.redis.lpush('npc_race','gnome')

    def tearDown(self):
        self.redis.flushall()

    def test_random_jobposting(self):
        """  """
        jobposting = JobPosting(self.redis)
        self.assertEquals('house', jobposting.valuedpossession)

    def test_jobposting_static_npc(self):
        """  """
        npc = NPC(self.redis)
        jobposting = JobPosting(self.redis, {'npc':npc})
        self.assertEquals(npc, jobposting.npc)

