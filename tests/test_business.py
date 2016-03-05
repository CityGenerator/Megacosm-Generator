#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Business, NPC
import unittest2 as unittest
import fakeredis
from mock import Mock
from config import TestConfiguration
import json


class TestBusiness(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        self.redis.lpush('name_businesstitle','Angry')
        self.redis.lpush('name_businessroot','Axe')
        self.redis.lpush('business_direction', 'west')
        self.redis.lpush('business_shade', 'bright')
        self.redis.lpush('business_windows', 'clean')
        self.redis.lpush('business_storefront', 'mud')
        self.redis.lpush('business_rooftype', 'slate')
        self.redis.lpush('business_condition', 'cluttered')
        self.redis.lpush('business_trouble', 'slumping sales')
        self.redis.zadd('business_neighborhood', '{ "name":"expensive",    "score":100 }',100)
        self.redis.zadd('business_age', '{  "name":"old"          , "score":100  }',100)
        self.redis.zadd('business_price', '{  "name":"very high"          , "score":100  }',100)
        self.redis.zadd('business_reputation', '{  "name":"being a pillar of the community"          , "score":100  }',100)
        self.redis.zadd('business_popularity', '{  "name":"is constantly crowded"                              , "score":100 }',100)
        self.redis.zadd('business_size', '{  "name":"vast"           , "score":100 }',100)
        self.redis.zadd('business_status', '{  "name":"booming",            "score":100 }',100)
        self.redis.set('bus_adventurersguild_kindname', 'adventurers guild')
        self.redis.set('bus_adventurersguild_perbuilding', '30')
        self.redis.set('bus_adventurersguild_maxfloors', '2')
        self.redis.set('bus_adventurersguild_district', 'professional')
        self.redis.lpush('business_kind', 'bus_adventurersguild')
        self.redis.lpush('bus_adventurersguild_manager', 'adventurer')
        self.redis.lpush('bus_adventurersguild_manager', 'mercenary')
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

    def tearDown(self):
        self.redis.flushall()

    def test_business(self):
        """  """
        business = Business(self.redis)
        self.assertNotEqual('', business.name)
        self.assertNotEqual('', str(business))

    def test_senses(self):
        """  """
        business = Business(self.redis, {'smell': 'stank', 'sight': 'ugly blinds', 'sound': 'cries for help'})
        self.assertNotEqual('', str(business))

    def test_maxfloors(self):
        """  """
        self.redis.set('bus_adventurersguild_maxfloors', None)
        business = Business(self.redis)
        self.assertNotEqual('', str(business))
        self.assertEqual(1, business.maxfloors)

    def test_business_params(self):
        """  """
        dummyuser = Mock(NPC)
        business = Business(self.redis,
                            {'owner': dummyuser, 'patroncount': 3, 'trailer': 'a place', 'maxfloors': 2, 'floor': 1})
        self.assertNotEqual('', str(business))

    def test_business_data(self):

        stats = ['status', 'size', 'popularity', 'reputation', 'price', 'age', 'neighborhood']
        for stat in stats:
            results = self.redis.zrangebyscore('business_'+stat, 0, 100, withscores=True)
            for (result, score) in results:
                resultobj = json.loads(result)
                self.assertEquals(score, resultobj['score'])
