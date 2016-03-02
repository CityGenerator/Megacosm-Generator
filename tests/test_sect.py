#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Sect, Deity
import unittest2 as unittest

import fakeredis
from megacosm.util.Seeds import set_seed

from config import TestConfiguration


class TestSect(unittest.TestCase):

    def setUp(self):
        """  """
	self.redis=fakeredis.FakeRedis()
	self.redis.zadd( 'sect_acceptance','{"name":"saintly",  "score":100   }',100)

	#Deity NPC details
        self.redis.lpush('npc_race','gnome')
        self.redis.lpush('gnome_covering','skin')
        self.redis.set('gnome_details',  '{"name": "Gnome",      "size": "small",   "description": "having engineering and intellectual expertise" }')
        self.redis.set('skin_covertemplate', '{{params.skinkind}}, {{params.skincolor}} skin')
        self.redis.lpush('skin_skincolor','alabaster')
        self.redis.lpush('skin_skinkind', 'thick')
        self.redis.lpush('phobia_template', "You are afraid.")
        self.redis.lpush('motivation_kind', 'acceptance')
        self.redis.lpush('motivationacceptance_text', 'to impress someone')
        self.redis.lpush('gnome_name_first_post', 'Tom')
        self.redis.lpush('gnome_name_last_pre', 'Gyro')

	#Deity Details
	self.redis.lpush('deity_favored_stat','skill')
	self.redis.zadd('deity_importance', '{"name":"over deity",          "score":100, "points":21 }',100)
	self.redis.zadd('portfolio_domain', '{"name":"good",                       "score":16 }', 16)
	self.redis.zadd('portfolio_domain', '{"name":"cold",                       "score":4 }', 4)
	self.redis.zadd('portfolio_domain', '{"name":"zeal",                       "score":3 }', 3)
	self.redis.zadd('portfolio_domain', '{"name":"song",                       "score":2 }', 2)
	self.redis.zadd('portfolio_domain', '{"name":"adventure",                       "score":1 }', 1)
	self.redis.lpush('portfolio_level',16)
	self.redis.lpush('portfolio_level',4)
	self.redis.lpush('portfolio_level',3)
	self.redis.lpush('portfolio_level',2)
	self.redis.lpush('portfolio_level',1)

    def tearDown(self):
        self.redis.flushall()

    def test_random_sect(self):
        """  """
        sect = Sect(self.redis)
        self.assertNotEqual(sect.domain, '')

    def test_static_sect(self):
        """  """
	deity=Deity(self.redis)
        sect = Sect(self.redis, {'deity':deity})
        self.assertNotEqual(sect.domain, '')
        self.assertIn(sect.domain, deity.portfolios)

    def test_static_domain(self):
        """  """
        sect = Sect(self.redis, {'domain':'tacos'})
        self.assertEqual(sect.domain, 'tacos')
