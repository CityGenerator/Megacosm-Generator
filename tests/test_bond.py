#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators.Bond import Bond
import unittest2 as unittest
import fixtures
import fakeredis


class TestBond(unittest.TestCase):
    """ Test the functionality of the Bond module. """
    def setUp(self):
        """ Set up the required fixtures """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        fixtures.bond.import_fixtures(self)
        fixtures.npc.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        self.redis.lpush('npc_race', 'gnome')

    def tearDown(self):
        """ Clean up any changes from the last run. """
        self.redis.flushall()

    def test_random_bond(self):
        """  Test a "random" bond. """
        bond = Bond(self.redis)
        self.assertIn(bond.text, ['Way back when, you amused Tom Gyro in an unusual way.',
                                  'Way back when, Tom Gyro amused you in an unusual way.'])

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
        self.assertEqual('Recently, Jesse Will Tony Shaun Rich', str(bond))


    def test_bond_static_text(self):
        """  Pass in all bond fields. """
        bond = Bond(self.redis, {
            'text': 'Tacos Tacos Tacos',
            })
        self.assertEqual('Tacos Tacos Tacos', bond.text)
