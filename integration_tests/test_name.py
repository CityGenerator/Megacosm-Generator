#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test Names with live data to ensure things behave as expected."""

import unittest
from megacosm.generators.Name import Name
from megacosm.generators.NPC import NPC
from config import IntegrationTestConfiguration
from fixtures import bond, business, city, continent, country, cuisine, currency, curse, deity, drink, dungeon, event
from fixtures import flag, flaw, gem, generator, geomorphdungeon, govt, grafitti, jobposting, leader, legend, magicitem
from fixtures import misfire, moon, mundaneitem, npc, organization, motivation, planet, phobia, region, resource
from fixtures import roguedungeon, rumor, sect, star, starsystem, street, wanted, weather


class TestNameIntegration(unittest.TestCase):

    def setUp(self):
        self.redis = IntegrationTestConfiguration.REDIS
        npc.import_fixtures(self)
        star.import_fixtures(self)
        starsystem.import_fixtures(self)
        artwork.import_fixtures(self)
        bond.import_fixtures(self)
        business.import_fixtures(self)
        city.import_fixtures(self)
        continent.import_fixtures(self)
        country.import_fixtures(self)
        cuisine.import_fixtures(self)
        currency.import_fixtures(self)
        curse.import_fixtures(self)
        deity.import_fixtures(self)
        drink.import_fixtures(self)
        dungeon.import_fixtures(self)
        event.import_fixtures(self)
        flag.import_fixtures(self)
        flaw.import_fixtures(self)
        gem.import_fixtures(self)
        generator.import_fixtures(self)
        geomorphdungeon.import_fixtures(self)
        govt.import_fixtures(self)
        grafitti.import_fixtures(self)
        jobposting.import_fixtures(self)
        leader.import_fixtures(self)
        legend.import_fixtures(self)
        magicitem.import_fixtures(self)
        misfire.import_fixtures(self)
        moon.import_fixtures(self)
        mundaneitem.import_fixtures(self)
        npc.import_fixtures(self)
        organization.import_fixtures(self)
        motivation.import_fixtures(self)
        planet.import_fixtures(self)
        phobia.import_fixtures(self)
        region.import_fixtures(self)
        resource.import_fixtures(self)
        roguedungeon.import_fixtures(self)
        rumor.import_fixtures(self)
        sect.import_fixtures(self)
        star.import_fixtures(self)
        starsystem.import_fixtures(self)
        street.import_fixtures(self)
        wanted.import_fixtures(self)
        weather.import_fixtures(self)

    def tearDown(self):
        """Tear stuff Down."""
        self.redis.flushall()

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
