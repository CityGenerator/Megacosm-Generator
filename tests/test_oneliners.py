#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fully test this module's functionality through the use of fixtures."""
#
import megacosm
from flask_testing import TestCase
import fakeredis
import fixtures
from megacosm import oneliners
import re


class MegacosmFlaskTestCast(TestCase):

    def create_app(self):
        """ """
        app = megacosm.create_app('config.TestConfiguration')
        app.debug = True
        app.config['TESTING'] = True
        app.config['REDIS'] = fakeredis.FakeRedis(decode_responses=True)
        return app

    def setUp(self):
        megacosm.app.config['REDIS'] = fakeredis.FakeRedis(decode_responses=True)
        self.app = megacosm.app.test_client()
        self.redis = megacosm.app.config['REDIS']
        fixtures.artwork.import_fixtures(self)
        fixtures.bond.import_fixtures(self)
        fixtures.business.import_fixtures(self)
        fixtures.city.import_fixtures(self)
        fixtures.continent.import_fixtures(self)
        fixtures.country.import_fixtures(self)
        fixtures.cuisine.import_fixtures(self)
        fixtures.currency.import_fixtures(self)
        fixtures.curse.import_fixtures(self)
        fixtures.deity.import_fixtures(self)
        fixtures.dungeon.import_fixtures(self)
        fixtures.event.import_fixtures(self)
        fixtures.flag.import_fixtures(self)
        fixtures.flaw.import_fixtures(self)
        fixtures.gem.import_fixtures(self)
        fixtures.geomorphdungeon.import_fixtures(self)
        fixtures.govt.import_fixtures(self)
        fixtures.grafitti.import_fixtures(self)
        fixtures.jobposting.import_fixtures(self)
        fixtures.leader.import_fixtures(self)
        fixtures.legend.import_fixtures(self)
        fixtures.misfire.import_fixtures(self)
        fixtures.magicitem.import_fixtures(self)
        fixtures.moon.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        fixtures.mundaneitem.import_fixtures(self)
        fixtures.npc.import_fixtures(self)
        fixtures.organization.import_fixtures(self)
        fixtures.planet.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.region.import_fixtures(self)
        fixtures.resource.import_fixtures(self)
        fixtures.roguedungeon.import_fixtures(self)
        fixtures.rumor.import_fixtures(self)
        fixtures.sect.import_fixtures(self)
        fixtures.star.import_fixtures(self)
        fixtures.starsystem.import_fixtures(self)
        fixtures.street.import_fixtures(self)
        fixtures.weather.import_fixtures(self)
        fixtures.wanted.import_fixtures(self)
        self.redis.lpush('npc_race', 'kobold')

    def tearDown(self):
        self.app = None
        self.redis.flushall()

    def test_valid_count(self):
        self.assertFalse(oneliners.valid_count('1'))
        self.assertTrue(oneliners.valid_count('7'))
        self.assertFalse(oneliners.valid_count('1000'))
        self.assertFalse(oneliners.valid_count('-1000'))
        self.assertFalse(oneliners.valid_count('Waffles'))

################################################################

    def test_artwork_route(self):
        response = self.app.get('/artwork')
        self.assertTemplateUsed('oneliner.html')
        self.assertIn(b'A Work of Art...', response.data)
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_artwork_count(self):
        """ test a regular count"""
        response = self.app.get('/artwork?count=10')
        self.assertEqual(10,   len(re.findall(b'artwork_oneliner', response.data)))
        self.assert200(response)

    def test_multi_artwork_count_bad(self):
        """ """
        response = self.app.get('/artwork?count=crackers')
        self.assertEqual(0,   len(re.findall(b'artwork_oneliner', response.data)))
        self.assert200(response)

    def test_artwork_builder_route(self):
        response = self.app.get('/artwork_builder')
        self.assertTemplateUsed('generic_builder.html')
        self.assertIn(b'Lets build an Artwork', response.data)
        self.assert200(response)

################################################################

    def test_bond_route(self):
        response = self.app.get('/bond')
        self.assertTemplateUsed('oneliner.html')
        self.assertIn(b'The Ties that Bind Us...', response.data)
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_bond_route_count(self):
        """ Test the route count and ensure the right number appear"""
        response = self.app.get('/bond?count=90')
        self.assertEqual(90,   len(re.findall(b'bond_oneliner', response.data)))
        self.assert200(response)

    def test_bond_route_count_bad(self):
        """ Test the route count for a bad value"""
        response = self.app.get('/bond?count=crackers')
        self.assertEqual(0,   len(re.findall(b'bond_oneliner', response.data)))
        self.assert200(response)

    def test_bond_builder_route(self):
        response = self.app.get('/bond_builder')
        self.assertTemplateUsed('bond_builder.html')
        self.assertIn(b'Create a Bond', response.data)
        self.assert200(response)

################################################################

    def test_resource_route(self):
        response = self.app.get('/resource')
        self.assertTemplateUsed('oneliner.html')
        self.assertIn(b'At Your Disposal...', response.data)
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_resource_count(self):
        """ """
        response = self.app.get('/resource?count=10')
        self.assertEqual(10,   len(re.findall(b'resource_oneliner', response.data)))
        self.assert200(response)

    def test_multi_resource_toohigh_route(self):
        response = self.app.get('/resource?count=101')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_resource_builder_route(self):
        response = self.app.get('/resource_builder')
        self.assertTemplateUsed('generic_builder.html')
        self.assertIn(b"Create a Resource", response.data)
        self.assert200(response)

###############################################################

    def test_rumor_route(self):
        response = self.app.get('/rumor')
        self.assertTemplateUsed('oneliner.html')
        self.assertIn(b'Did You Hear?', response.data)
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_rumor_count(self):
        """ """
        response = self.app.get('/rumor?count=10')
        self.assertEqual(10,   len(re.findall(b'rumor_oneliner', response.data)))
        self.assert200(response)

    def test_multi_rumor_toohigh_route(self):
        """ """
        response = self.app.get('/rumor?count=crackers')
        self.assertEqual(0,   len(re.findall(b'rumor_oneliner', response.data)))
        self.assert200(response)

    def test_rumor_builder_route(self):
        response = self.app.get('/rumor_builder')
        self.assertTemplateUsed('generic_builder.html')
        self.assertIn(b'Create a Rumor', response.data)
        self.assert200(response)

################################################################

    def test_grafitti_route(self):
        response = self.app.get('/grafitti')
        self.assertTemplateUsed('oneliner.html')
        self.assertIn(b'Scrawled on a Nearby Wall...', response.data)
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_grafitti_route_count(self):
        """ Test the route count and ensure the right number appear"""
        response = self.app.get('/grafitti?count=90')
        self.assertEqual(90,   len(re.findall(b'grafitti_oneliner', response.data)))
        self.assert200(response)

    def test_grafitti_route_count_bad(self):
        """ Test the route count for a bad value"""
        response = self.app.get('/grafitti?count=crackers')
        self.assertEqual(0,   len(re.findall(b'grafitti_oneliner', response.data)))
        self.assert200(response)

    def test_grafitti_builder_route(self):
        response = self.app.get('/grafitti_builder')
        self.assertTemplateUsed('generic_builder.html')
        self.assertIn(b'Create a Grafitti', response.data)
        self.assert200(response)
################################################################

    def test_misfire_route(self):
        response = self.app.get('/misfire')
        self.assertTemplateUsed('oneliner.html')
        self.assertIn(b'My Spell Misfired!', response.data)
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_misfire_count(self):
        """ """
        response = self.app.get('/misfire?count=10')
        self.assertEqual(10,   len(re.findall(b'misfire_oneliner', response.data)))
        self.assert200(response)

    def test_multi_misfire_count_bad(self):
        """ """
        response = self.app.get('/misfire?count=duck')
        self.assertEqual(0,   len(re.findall(b'misfire_oneliner', response.data)))
        self.assert200(response)

    def test_misfire_builder_route(self):
        response = self.app.get('/misfire_builder')
        self.assertTemplateUsed('generic_builder.html')
        self.assertIn(b'Create a Misfire', response.data)
        self.assert200(response)

###############################################################

    def test_flaw_route(self):
        response = self.app.get('/flaw')
        self.assertTemplateUsed('oneliner.html')
        self.assertIn(b'My Greatest Flaw...', response.data)
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_flaw_count(self):
        """ """
        response = self.app.get('/flaw?count=10')
        self.assertEqual(10,   len(re.findall(b'flaw_oneliner', response.data)))
        self.assert200(response)

    def test_multi_flaw_count_bad(self):
        response = self.app.get('/flaw?count=duck')
        self.assertEqual(0,   len(re.findall(b'flaw_oneliner', response.data)))
        self.assert200(response)

    def test_flaw_builder_route(self):
        response = self.app.get('/flaw_builder')
        self.assertTemplateUsed('generic_builder.html')
        self.assertIn(b'Create a Flaw', response.data)
        self.assert200(response)

##############################################################

    def test_currency_route(self):
        response = self.app.get('/currency')
        self.assertTemplateUsed('oneliner.html')
        self.assertIn(b'Spare Some Change?', response.data)
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_currency_count(self):
        """ """
        response = self.app.get('/currency?count=10')
        self.assertEqual(10,   len(re.findall(b'currency_oneliner', response.data)))
        self.assert200(response)

    def test_multi_currency_nondigit_route(self):
        """ """
        response = self.app.get('/currency?count=duck')
        self.assertEqual(0,   len(re.findall(b'currency_oneliner', response.data)))
        self.assert200(response)

    def test_currency_builder_route(self):
        response = self.app.get('/currency_builder')
        self.assertTemplateUsed('generic_builder.html')
        self.assertIn(b'Create a Currency', response.data)
        self.assert200(response)

##############################################################

    def test_jobposting_route(self):
        response = self.app.get('/jobposting')
        self.assertIn(b'Help Wanted!', response.data)
        self.assertTemplateUsed('oneliner.html')
        self.assert200(response)

    def test_multi_jobposting_count(self):
        """ """
        response = self.app.get('/jobposting?count=10')
        self.assertEqual(10,   len(re.findall(b'jobposting_oneliner', response.data)))
        self.assert200(response)

    def test_multi_jobposting_nondigit_route(self):
        """ """
        response = self.app.get('/jobposting?count=duck')
        self.assertEqual(0,   len(re.findall(b'jobposting_oneliner', response.data)))
        self.assert200(response)

    def test_jobposting_builder_route(self):
        response = self.app.get('/jobposting_builder')
        self.assertTemplateUsed('generic_builder.html')
        self.assertIn(b'Create a Jobposting', response.data)
        self.assert200(response)

##############################################################

    def test_curse_route(self):
        response = self.app.get('/curse')
        self.assertIn(b'Unforseen Consequences...', response.data)
        self.assertTemplateUsed('oneliner.html')
        self.assert200(response)

    def test_multi_curse_count(self):
        """ """
        response = self.app.get('/curse?count=10')
        self.assertEqual(10,   len(re.findall(b'curse_oneliner', response.data)))
        self.assert200(response)

    def test_multi_curse_nondigit_route(self):
        """ """
        response = self.app.get('/curse?count=duck')
        self.assertEqual(0,   len(re.findall(b'curse_oneliner', response.data)))
        self.assert200(response)

    def test_curse_builder_route(self):
        response = self.app.get('/curse_builder')
        self.assertTemplateUsed('generic_builder.html')
        self.assertIn(b'Create a Curse', response.data)
        self.assert200(response)

##############################################################

    def test_event_route(self):
        response = self.app.get('/event?seed=99')
        self.assertIn(b'seed=99', response.data)
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_event_toolow_route(self):
        response = self.app.get('/event?count=0')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_event_toohigh_route(self):
        response = self.app.get('/event?count=101')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_event_nondigit_route(self):
        response = self.app.get('/event?count=duck')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_event_route(self):
        response = self.app.get('/event?count=5')
        self.assertTemplateUsed('oneliner.html')
        self.assertIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_event_builder_route(self):
        response = self.app.get('/event_builder')
        self.assertTemplateUsed('generic_builder.html')
        self.assert200(response)

##############################################################

    def test_motivation_route(self):
        response = self.app.get('/motivation?seed=99')
        self.assertIn(b'seed=99', response.data)
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_motivation_toolow_route(self):
        response = self.app.get('/motivation?count=0')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_motivation_toohigh_route(self):
        response = self.app.get('/motivation?count=101')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_motivation_nondigit_route(self):
        response = self.app.get('/motivation?count=duck')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_motivation_route(self):
        response = self.app.get('/motivation?count=5')
        self.assertTemplateUsed('oneliner.html')
        self.assertIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_motivation_builder_route(self):
        response = self.app.get('/motivation_builder')
        self.assertTemplateUsed('generic_builder.html')
        self.assert200(response)

##############################################################

    def test_phobia_route(self):
        response = self.app.get('/phobia?seed=99')
        self.assertIn(b'seed=99', response.data)
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_phobia_toolow_route(self):
        response = self.app.get('/phobia?count=0')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_phobia_toohigh_route(self):
        response = self.app.get('/phobia?count=101')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_phobia_nondigit_route(self):
        response = self.app.get('/phobia?count=duck')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_phobia_route(self):
        response = self.app.get('/phobia?count=5')
        self.assertTemplateUsed('oneliner.html')
        self.assertIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_phobia_builder_route(self):
        response = self.app.get('/phobia_builder')
        self.assertTemplateUsed('generic_builder.html')
        self.assert200(response)

##############################################################

    def test_gem_route(self):
        response = self.app.get('/gem?seed=99')
        self.assertIn(b'seed=99', response.data)
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_gem_toolow_route(self):
        response = self.app.get('/gem?count=0')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_gem_toohigh_route(self):
        response = self.app.get('/gem?count=101')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_gem_nondigit_route(self):
        response = self.app.get('/gem?count=duck')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_gem_route(self):
        response = self.app.get('/gem?count=5')
        self.assertTemplateUsed('oneliner.html')
        self.assertIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_gem_builder_route(self):
        response = self.app.get('/gem_builder')
        self.assertTemplateUsed('generic_builder.html')
        self.assert200(response)

##############################################################

    def test_mundaneitem_route(self):
        response = self.app.get('/mundaneitem?seed=99')
        self.assertIn(b'seed=99', response.data)
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_mundaneitem_toolow_route(self):
        response = self.app.get('/mundaneitem?count=0')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_mundaneitem_toohigh_route(self):
        response = self.app.get('/mundaneitem?count=101')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_mundaneitem_nondigit_route(self):
        response = self.app.get('/mundaneitem?count=duck')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_mundaneitem_route(self):
        response = self.app.get('/mundaneitem?count=5')
        self.assertTemplateUsed('oneliner.html')
        self.assertIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_mundaneitem_builder_route(self):
        response = self.app.get('/mundaneitem_builder')
        self.assertTemplateUsed('generic_builder.html')
        self.assert200(response)

##############################################################

    def test_legend_route(self):
        response = self.app.get('/legend?seed=99')
        self.assertIn(b'seed=99', response.data)
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_legend_toolow_route(self):
        response = self.app.get('/legend?count=0')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_legend_toohigh_route(self):
        response = self.app.get('/legend?count=101')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_legend_nondigit_route(self):
        response = self.app.get('/legend?count=duck')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_legend_route(self):
        response = self.app.get('/legend?count=5')
        self.assertTemplateUsed('oneliner.html')
        self.assertIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_legend_builder_route(self):
        response = self.app.get('/legend_builder')
        self.assertTemplateUsed('generic_builder.html')
        self.assert200(response)

##############################################################

    def test_cuisine_route(self):
        response = self.app.get('/cuisine?seed=99')
        self.assertIn(b'seed=99', response.data)
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_cuisine_toolow_route(self):
        response = self.app.get('/cuisine?count=0')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_cuisine_toohigh_route(self):
        response = self.app.get('/cuisine?count=101')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_cuisine_nondigit_route(self):
        response = self.app.get('/cuisine?count=duck')
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_multi_cuisine_route(self):
        response = self.app.get('/cuisine?count=5')
        self.assertTemplateUsed('oneliner.html')
        self.assertIn(b'oneliner-list', response.data)
        self.assert200(response)

    def test_cuisine_builder_route(self):
        response = self.app.get('/cuisine_builder')
        self.assertTemplateUsed('generic_builder.html')
        self.assert200(response)
