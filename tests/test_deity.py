#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Deity, Sect
import unittest2 as unittest

import fakeredis
from config import TestConfiguration


class TestDeity(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
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
        self.redis.hset('gnome_name_first','post', 100)
        self.redis.hset('gnome_name_last','pre', 100)
        self.redis.zadd('gnome_name_order','{ "name":"first" }',50)
        self.redis.zadd('gnome_name_order','{ "name":"last"}',100)

        self.redis.hset('deity_primarycolor_description', 'aquamarine', '{"name":"aquamarine", "hex":"7FFFD4" }')
        self.redis.hset('deity_vow_description', 'humility', '{"name":"Humility",         "description":"abstain from extolling your own virtues"}')
        self.redis.lpush('deity_favored_stat', 'piety')
        self.redis.lpush('deity_favored_weapon', 'bows')
        self.redis.lpush('deity_form', 'talking jackal')
        self.redis.lpush('deity_holysymbol', 'axe')
        self.redis.lpush('deity_holysymbol_type', 'rocking')
        self.redis.lpush('deity_primarycolor', 'aquamarine')
        self.redis.lpush('deity_vow', 'humility')
        self.redis.lpush('deity_worship', 'supplication')
        self.redis.zadd('deity_importance', '{"name":"over deity",          "score":100,"points":21 }', 100)
        self.redis.zadd('deity_organized', '{"name":"rigidly",         "score":100 }', 100)
        self.redis.zadd('deity_unity', '{"name":"unified",     "score":100 }', 100)
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

    def test_deity(self):
        """  """
        deity = Deity(self.redis)
        self.assertNotEqual('', deity.name)

    def test_deity_sects(self):
        """  """
        deity = Deity(self.redis, {'deity_unity_roll': 100, 'deity_importance_roll': 100})
        deity.add_sects()
        self.assertEqual(len(deity.sects), 0)

        deity = Deity(self.redis, {'deity_unity_roll': 0, 'deity_importance_roll': 100})
        deity.add_sects()
        self.assertGreaterEqual(len(deity.sects), 1)

        sect=Sect(self.redis)
        wrongdeity=sect.deity
        deity = Deity(self.redis, {'sects':[sect]})
        self.assertIsNot(deity, wrongdeity)
        deity.add_sects()
        self.assertIs(deity, sect.deity)

        self.assertGreaterEqual(len(deity.sects), 1)

    def test_deity_portfolios(self):
        """  """

        deity = Deity(self.redis, {'portfolios':['tacos','burritos']})
        deity.add_sects()
        self.assertIn( 'tacos', deity.portfolios )
