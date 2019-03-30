#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test Names with live data to ensure things behave as expected."""

import unittest
from megacosm.generators.Name import Name
from megacosm.generators.NPC import NPC
from config import IntegrationTestConfiguration


class TestNameIntegration(unittest.TestCase):

    def setUp(self):
        self.redis = IntegrationTestConfiguration.REDIS

    def tearDown(self):
        """Tear stuff Down."""
        # self.redis.flushall()

    def test_races(self):
        """  """
        for race in self.redis.lrange('npc_race', 0, -1):
            name = Name(self.redis, race, {'title': 'Mr.'})
            self.assertEqual(race, str(name.namesource))
            print("%s: %s | %s | %s" % (race, name.fullname, name.shortname, name.formalname))
            self.assertIn('{{params.title}} ', str(name.fullname_template))
            self.assertIn(' {{params.trailer}}', str(name.fullname_template))
            self.assertNotIn('{{', str(name.fullname))
            self.assertNotIn('}}', str(name.fullname))
            self.assertNotIn('params', str(name.fullname))
            self.assertNotIn('{{', str(name.shortname))
            self.assertNotIn('}}', str(name.shortname))
            self.assertNotIn('params', str(name.shortname))
            self.assertNotIn('{{', str(name.formalname))
            self.assertNotIn('}}', str(name.formalname))
            self.assertNotIn('params', str(name.formalname))

    def test_business(self):
        """  """
        name = Name(self.redis, 'business', {'businesstype': 'Butcher'})
        self.assertEqual('business', str(name.namesource))
        print("business: %s | %s | %s" % (name.fullname, name.shortname, name.formalname))
        self.assertIn(' {{params.noun}} ', str(name.fullname_template))
        self.assertIn('{{params.adjective}} ', str(name.fullname_template))
        self.assertNotIn('{{', str(name.fullname))
        self.assertNotIn('}}', str(name.fullname))
        self.assertNotIn('params', str(name.fullname))
        self.assertNotIn('{{', str(name.shortname))
        self.assertNotIn('}}', str(name.shortname))
        self.assertNotIn('params', str(name.shortname))
        self.assertNotIn('{{', str(name.formalname))
        self.assertNotIn('}}', str(name.formalname))
        self.assertNotIn('params', str(name.formalname))

    def test_city(self):
        """  """
        name = Name(self.redis, 'city', {'citytype': 'Butcher'})
        self.assertEqual('city', str(name.namesource))
        print("city: %s | %s | %s" % (name.fullname, name.shortname, name.formalname))
        self.assertIn('{{params.title}} ', str(name.fullname_template))
        self.assertIn(' {{params.pre}}', str(name.fullname_template))
        self.assertIn('{{params.root}}', str(name.fullname_template))
        self.assertIn('{{params.post}} ', str(name.fullname_template))
        self.assertIn(' {{params.trailer}}', str(name.fullname_template))
        self.assertNotIn('{{', str(name.fullname))
        self.assertNotIn('}}', str(name.fullname))
        self.assertNotIn('params', str(name.fullname))
        self.assertNotIn('{{', str(name.shortname))
        self.assertNotIn('}}', str(name.shortname))
        self.assertNotIn('params', str(name.shortname))
        self.assertNotIn('{{', str(name.formalname))
        self.assertNotIn('}}', str(name.formalname))
        self.assertNotIn('params', str(name.formalname))

    def test_continent(self):
        """  """
        name = Name(self.redis, 'continent', {'continenttype': 'Butcher'})
        self.assertEqual('continent', str(name.namesource))
        print("continent: %s | %s | %s" % (name.fullname, name.shortname, name.formalname))
        self.assertIn('{{params.title}} ', str(name.fullname_template))
        self.assertIn(' {{params.pre}}', str(name.fullname_template))
        self.assertIn('{{params.root}}', str(name.fullname_template))
        self.assertIn('{{params.post}}', str(name.fullname_template))
        self.assertNotIn('{{', str(name.fullname))
        self.assertNotIn('}}', str(name.fullname))
        self.assertNotIn('params', str(name.fullname))
        self.assertNotIn('{{', str(name.shortname))
        self.assertNotIn('}}', str(name.shortname))
        self.assertNotIn('params', str(name.shortname))
        self.assertNotIn('{{', str(name.formalname))
        self.assertNotIn('}}', str(name.formalname))
        self.assertNotIn('params', str(name.formalname))

    def test_country(self):
        """  """
        name = Name(self.redis, 'country')
        self.assertEqual('country', str(name.namesource))
        print("country: %s | %s | %s" % (name.fullname, name.shortname, name.formalname))
        self.assertIn('{{params.title}} ', str(name.fullname_template))
        self.assertIn(' {{params.pre}}', str(name.fullname_template))
        self.assertIn('{{params.root}}', str(name.fullname_template))
        self.assertIn('{{params.post}}', str(name.fullname_template))

        self.assertEqual(str(name.fullname), str(name.shortname))
        self.assertEqual(str(name.fullname), str(name.formalname))
        self.assertNotIn('{{', str(name.fullname))
        self.assertNotIn('}}', str(name.fullname))
        self.assertNotIn('params', str(name.fullname))
        self.assertNotIn('{{', str(name.shortname))
        self.assertNotIn('}}', str(name.shortname))
        self.assertNotIn('params', str(name.shortname))
        self.assertNotIn('{{', str(name.formalname))
        self.assertNotIn('}}', str(name.formalname))
        self.assertNotIn('params', str(name.formalname))

    def test_currency(self):
        """  """
        name = Name(self.redis, 'currency')
        self.assertEqual('currency', str(name.namesource))
        print("currency: %s | %s | %s" % (name.fullname, name.shortname, name.formalname))
        self.assertIn('{{params.pre}}', str(name.fullname_template))
        self.assertIn('{{params.root}}', str(name.fullname_template))
        self.assertIn('{{params.post}}', str(name.fullname_template))

        self.assertEqual(str(name.fullname), str(name.shortname))
        self.assertEqual(str(name.fullname), str(name.formalname))
        self.assertNotIn('{{', str(name.fullname))
        self.assertNotIn('}}', str(name.fullname))
        self.assertNotIn('params', str(name.fullname))
        self.assertNotIn('{{', str(name.shortname))
        self.assertNotIn('}}', str(name.shortname))
        self.assertNotIn('params', str(name.shortname))
        self.assertNotIn('{{', str(name.formalname))
        self.assertNotIn('}}', str(name.formalname))
        self.assertNotIn('params', str(name.formalname))

    def test_dungeon(self):
        """  """
        name = Name(self.redis, 'dungeon')
        self.assertEqual('dungeon', str(name.namesource))
        print("dungeon: %s | %s | %s" % (name.fullname, name.shortname, name.formalname))
        self.assertIn('{{params.place}} ', str(name.fullname_template))
        self.assertEqual(str(name.fullname), str(name.formalname))
        self.assertNotIn('{{', str(name.fullname))
        self.assertNotIn('}}', str(name.fullname))
        self.assertNotIn('params', str(name.fullname))
        self.assertNotIn('{{', str(name.shortname))
        self.assertNotIn('}}', str(name.shortname))
        self.assertNotIn('params', str(name.shortname))
        self.assertNotIn('{{', str(name.formalname))
        self.assertNotIn('}}', str(name.formalname))
        self.assertNotIn('params', str(name.formalname))

    def test_moon(self):
        """  """
        name = Name(self.redis, 'moon')
        self.assertEqual('moon', str(name.namesource))
        print("moon: %s | %s | %s" % (name.fullname, name.shortname, name.formalname))
        self.assertIn('{{params.pre}}', str(name.fullname_template))
        self.assertIn('{{params.root}}', str(name.fullname_template))
        self.assertIn('{{params.post}}', str(name.fullname_template))

        self.assertEqual(str(name.fullname), str(name.shortname))
        self.assertEqual(str(name.fullname), str(name.formalname))
        self.assertNotIn('{{', str(name.fullname))
        self.assertNotIn('}}', str(name.fullname))
        self.assertNotIn('params', str(name.fullname))
        self.assertNotIn('{{', str(name.shortname))
        self.assertNotIn('}}', str(name.shortname))
        self.assertNotIn('params', str(name.shortname))
        self.assertNotIn('{{', str(name.formalname))
        self.assertNotIn('}}', str(name.formalname))
        self.assertNotIn('params', str(name.formalname))

    def test_organization(self):
        """  """
        leader = NPC(self.redis)
        name = Name(self.redis, 'organization', {'leader': leader})
        self.assertEqual('organization', str(name.namesource))
        print("organization: %s | %s | %s" % (name.fullname, name.shortname, name.formalname))
        self.assertEqual(str(name.fullname), str(name.formalname))
        self.assertNotIn('{{', str(name.fullname))
        self.assertNotIn('}}', str(name.fullname))
        self.assertNotIn('params', str(name.fullname))
        self.assertNotIn('{{', str(name.shortname))
        self.assertNotIn('}}', str(name.shortname))
        self.assertNotIn('params', str(name.shortname))
        self.assertNotIn('{{', str(name.formalname))
        self.assertNotIn('}}', str(name.formalname))
        self.assertNotIn('params', str(name.formalname))

    def test_planet(self):
        """  """
        name = Name(self.redis, 'planet')
        self.assertEqual('planet', str(name.namesource))
        print("planet: %s | %s | %s" % (name.fullname, name.shortname, name.formalname))
        self.assertIn('{{params.title}} ', str(name.fullname_template))
        self.assertIn(' {{params.pre}}', str(name.fullname_template))
        self.assertIn('{{params.root}}', str(name.fullname_template))
        self.assertIn('{{params.post}} ', str(name.fullname_template))
        self.assertIn(' {{params.trailer}}', str(name.fullname_template))
        self.assertEqual(str(name.fullname), str(name.shortname))
        self.assertEqual(str(name.fullname), str(name.formalname))
        self.assertNotIn('{{', str(name.fullname))
        self.assertNotIn('}}', str(name.fullname))
        self.assertNotIn('params', str(name.fullname))
        self.assertNotIn('{{', str(name.shortname))
        self.assertNotIn('}}', str(name.shortname))
        self.assertNotIn('params', str(name.shortname))
        self.assertNotIn('{{', str(name.formalname))
        self.assertNotIn('}}', str(name.formalname))
        self.assertNotIn('params', str(name.formalname))

    def test_region(self):
        """  """
        name = Name(self.redis, 'region')
        self.assertEqual('region', str(name.namesource))
        print("region: %s | %s | %s" % (name.fullname, name.shortname, name.formalname))
        self.assertIn('{{params.title}} ', str(name.fullname_template))
        self.assertIn(' {{params.pre}}', str(name.fullname_template))
        self.assertIn('{{params.root}}', str(name.fullname_template))
        self.assertIn('{{params.post}} ', str(name.fullname_template))
        self.assertIn(' {{params.trailer}}', str(name.fullname_template))
        self.assertEqual(str(name.fullname), str(name.shortname))
        self.assertEqual(str(name.fullname), str(name.formalname))
        self.assertNotIn('{{', str(name.fullname))
        self.assertNotIn('}}', str(name.fullname))
        self.assertNotIn('params', str(name.fullname))
        self.assertNotIn('{{', str(name.shortname))
        self.assertNotIn('}}', str(name.shortname))
        self.assertNotIn('params', str(name.shortname))
        self.assertNotIn('{{', str(name.formalname))
        self.assertNotIn('}}', str(name.formalname))
        self.assertNotIn('params', str(name.formalname))

    def test_star(self):
        """  """
        name = Name(self.redis, 'star')
        self.assertEqual('star', str(name.namesource))
        print("star: %s | %s | %s" % (name.fullname, name.shortname, name.formalname))
        self.assertIn('{{params.pre}}', str(name.fullname_template))
        self.assertIn('{{params.root}}', str(name.fullname_template))
        self.assertIn('{{params.post}}', str(name.fullname_template))

        self.assertEqual(str(name.fullname), str(name.shortname))
        self.assertEqual(str(name.fullname), str(name.formalname))
        self.assertNotIn('{{', str(name.fullname))
        self.assertNotIn('}}', str(name.fullname))
        self.assertNotIn('params', str(name.fullname))
        self.assertNotIn('{{', str(name.shortname))
        self.assertNotIn('}}', str(name.shortname))
        self.assertNotIn('params', str(name.shortname))
        self.assertNotIn('{{', str(name.formalname))
        self.assertNotIn('}}', str(name.formalname))
        self.assertNotIn('params', str(name.formalname))

    def test_street(self):
        """  """
        name = Name(self.redis, 'street')
        self.assertEqual('street', str(name.namesource))
        print("street: %s | %s | %s" % (name.fullname, name.shortname, name.formalname))
        self.assertIn('{{params.title}} ', str(name.fullname_template))
        self.assertIn(' {{params.root}} ', str(name.fullname_template))
        self.assertIn(' {{params.trailer}}', str(name.fullname_template))

        self.assertIn('{{params.root}}', str(name.shortname_template))
        self.assertEqual(str(name.fullname), str(name.formalname))
        self.assertNotIn('{{', str(name.fullname))
        self.assertNotIn('}}', str(name.fullname))
        self.assertNotIn('params', str(name.fullname))
        self.assertNotIn('{{', str(name.shortname))
        self.assertNotIn('}}', str(name.shortname))
        self.assertNotIn('params', str(name.shortname))
        self.assertNotIn('{{', str(name.formalname))
        self.assertNotIn('}}', str(name.formalname))
        self.assertNotIn('params', str(name.formalname))
