#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fully test this module's functionality through the use of fixtures."""

from megacosm.generators.JobPosting import JobPosting
from megacosm.generators.NPC import NPC
import unittest
from fixtures import jobposting, business, npc, phobia, motivation
import fakeredis


class TestJobPosting(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        jobposting.import_fixtures(self)
        business.import_fixtures(self)
        npc.import_fixtures(self)
        phobia.import_fixtures(self)
        motivation.import_fixtures(self)

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

