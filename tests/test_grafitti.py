#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Grafitti, NPC
import unittest2 as unittest

import fakeredis


class TestGrafitti(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        self.redis.lpush('grafitti_template', 'Grafitti Template')

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
        self.redis.lpush('npc_profession', 'butcher')

        self.redis.hset('gnome_name_first','post', 100)
        self.redis.hset('gnome_name_last','pre', 100)
        self.redis.zadd('gnome_name_order','{ "name":"first" }',50)
        self.redis.zadd('gnome_name_order','{ "name":"last"}',100)

    def test_random_grafitti(self):
        """  """
        grafitti = Grafitti(self.redis)
        self.assertEqual('Grafitti Template', grafitti.text)
        self.assertEqual('Grafitti Template', str(grafitti))


    def test_static_npc(self):
        """  """
        npc = NPC(self.redis)
        grafitti = Grafitti(self.redis, {'npc':npc})
        self.assertEqual('Grafitti Template', grafitti.text)
        self.assertEqual('Tom Gyro', grafitti.npcname)

    def test_static_npcprofession(self):
        """  """
        grafitti = Grafitti(self.redis, {'npcprofession': 'Spaceman'})
        self.assertEqual('Grafitti Template', grafitti.text)
        self.assertEqual('Spaceman', grafitti.npcprofession)

    def test_static_npcpname(self):
        """  """
        grafitti = Grafitti(self.redis, {'npcname': 'Guenter'})
        self.assertEqual('Grafitti Template', grafitti.text)
        self.assertEqual('Guenter', grafitti.npcname)

    def test_static_text(self):
        """  """
        grafitti = Grafitti(self.redis, {'text': 'Nothing good.'})
        self.assertEqual('Nothing good.', str(grafitti))

    def test_static_signature(self):
        """  """
        grafitti = Grafitti(self.redis, {'signature': 'by the crazy guy.'})
        self.assertIn('by the crazy guy.', str(grafitti))

    def test_static_age(self):
        """  """
        grafitti = Grafitti(self.redis, {'age': 'super old.'})
        self.assertIn("You'd guess the message is super old.", str(grafitti))
