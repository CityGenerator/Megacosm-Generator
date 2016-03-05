#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Misfire
import unittest2 as unittest

import fakeredis
from config import TestConfiguration


class TestMisfire(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        self.redis.lpush('misfire_template', '{{params.target}} grow a pair of small horns (2 in each) on the forehead, which contrasts with skin color.  A remove curse may remove them.')
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
        self.redis.zadd('npc_sex', '{"name":"male",       "pronoun":"he", "possessive":"his",  "third-person":"him", "spouse":"wife",    "score":100  }', 100)

    def tearDown(self):
        self.redis.flushall()

    def test_random_misfire(self):
        """  """
        misfire = Misfire(self.redis)
        print misfire.text
        self.assertNotEqual(misfire.text, '')
        self.assertEqual('%s' % misfire, misfire.text)

    def test_static_misfire_text(self):
        """  """
        misfire = Misfire(self.redis, {'text': 'you fail at life'})
        #Remember it capitalizes
        self.assertEqual('You fail at life',str(misfire))

    def test_misfire_data(self):
        misfire = Misfire(self.redis)
        total = self.redis.llen('misfire_template')
        for i in range(0, total):
            misfire.template = self.redis.lindex('misfire_template', i)
            print "%s\n" % misfire.template
            results = misfire.render_template(misfire.template)
            self.assertNotEquals("", results)
            self.assertNotIn("{{", results)
