#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators.JobPosting import JobPosting
from megacosm.generators.NPC import NPC
import unittest
import fixtures
import fakeredis
from config import TestConfiguration


class TestJobPosting(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
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

