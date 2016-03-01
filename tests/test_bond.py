#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Bond
import unittest2 as unittest

import fakeredis
from config import TestConfiguration


class TestBond(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        self.redis.lpush('bond_template', 'Bob accepted you despite obvious failings. Which failing was the hardest?')
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


    def test_random_bond(self):
        """  Test a "random" bond. """
        bond = Bond(self.redis)
        self.assertEqual('Bob accepted you despite obvious failings. Which failing was the hardest?', bond.text)

    def test_bond_features(self):
        """  Pass in all bond fields. """
        bond = Bond(self.redis, {
            'you': 'Jesse',
            'other': 'Will',
            'either': 'Tony',
            'partyA': 'Shaun',
            'partyB': 'Rich',
            'template': '{{params.you}} {{params.other}} {{params.either}} {{params.partyA}} {{params.partyB}}',
            'bond_when_roll': 5,
            'when': 'Recently',
            })
        self.assertEqual('Recently, Jesse Will Tony Shaun Rich', bond.text)
        self.assertEqual('Recently, Jesse Will Tony Shaun Rich', "%s" % bond)


    def test_bond_static_text(self):
        """  Pass in all bond fields. """
        bond = Bond(self.redis, {
            'text': 'Tacos Tacos Tacos',
            })
        self.assertEqual('Tacos Tacos Tacos', bond.text)
