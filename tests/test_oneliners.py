#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import megacosm
from flask.ext.testing import TestCase
from megacosm import oneliners
import re

class MegacosmFlaskTestCast(TestCase):

    def create_app(self):
        """ """
        app = megacosm.create_app('config.TestConfiguration')
        return app

    def setUp(self):
        self.app = megacosm.app.test_client()

    def tearDown(self):
        self.app = None
        megacosm.app.server.delete('unittestgenerator_list')
        megacosm.app.server.delete('unittestgenerator_list_chance')
        megacosm.app.server.delete('unittestgenerator_range')
        megacosm.app.server.delete('unittestgenerator_list_description')


    def test_valid_count(self):
        self.assertFalse( oneliners.valid_count('1'))
        self.assertTrue( oneliners.valid_count('7'))
        self.assertFalse( oneliners.valid_count('1000'))
        self.assertFalse( oneliners.valid_count('-1000'))
        self.assertFalse( oneliners.valid_count('Waffles'))

#################################################################

    def test_artwork_route(self):
        response = self.app.get('/artwork?seed=99')
        self.assertIn('seed=99', response.data)
        self.assertTemplateUsed('oneliner.html')
        self.assertNotIn('oneliner-list', response.data)
        self.assert200(response)
#
#    def test_multi_artwork_toolow_route(self):
#        response = self.app.get('/artwork?count=0')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_artwork_toohigh_route(self):
#        response = self.app.get('/artwork?count=101')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_artwork_nondigit_route(self):
#        response = self.app.get('/artwork?count=duck')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_artwork_route(self):
#        response = self.app.get('/artwork?count=5')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_artwork_builder_route(self):
#        response = self.app.get('/artwork_builder')
#        self.assertTemplateUsed('generic_builder.html')
#        self.assert200(response)
#
################################################################

    def test_bond_route(self):
        response = self.app.get('/bond')
        self.assertTemplateUsed('oneliner.html')
        self.assertIn('The Ties that Bind Us..', response.data)
        self.assertNotIn('oneliner-list', response.data)
        self.assert200(response)

    def test_bond_route_count(self):
        ''' Test the route count and ensure the right number appear'''
        response = self.app.get('/bond?count=90')
        self.assertEqual(90,   len(     re.findall('bond_oneliner', response.data)))
        self.assert200(response)

    def test_bond_route_count_bad(self):
        ''' Test the route count for a bad value'''
        response = self.app.get('/bond?count=crackers')
        self.assertEqual(0,   len(     re.findall('bond_oneliner', response.data)))
        self.assert200(response)



    def test_bond_builder_route(self):
        response = self.app.get('/bond_builder')
        self.assertTemplateUsed('bond_builder.html')
        self.assertIn('Create a Bond', response.data)

        self.assert200(response)

#################################################################
#
#    def test_resource_route(self):
#        response = self.app.get('/resource?seed=99')
#        self.assertIn('seed=99', response.data)
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_resource_toolow_route(self):
#        response = self.app.get('/resource?count=0')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_resource_toohigh_route(self):
#        response = self.app.get('/resource?count=101')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_resource_nondigit_route(self):
#        response = self.app.get('/resource?count=duck')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_resource_route(self):
#        response = self.app.get('/resource?count=5')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_resource_builder_route(self):
#        response = self.app.get('/resource_builder')
#        self.assertTemplateUsed('generic_builder.html')
#        self.assert200(response)
#
#################################################################
#
#    def test_rumor_route(self):
#        response = self.app.get('/rumor?seed=99')
#        self.assertIn('seed=99', response.data)
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_rumor_toolow_route(self):
#        response = self.app.get('/rumor?count=0')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_rumor_toohigh_route(self):
#        response = self.app.get('/rumor?count=101')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_rumor_nondigit_route(self):
#        response = self.app.get('/rumor?count=duck')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_rumor_route(self):
#        response = self.app.get('/rumor?count=5')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_rumor_builder_route(self):
#        response = self.app.get('/rumor_builder')
#        self.assertTemplateUsed('generic_builder.html')
#        self.assert200(response)
#
#################################################################
#
#    def test_misfire_route(self):
#        response = self.app.get('/misfire?seed=99')
#        self.assertIn('seed=99', response.data)
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_misfire_toolow_route(self):
#        response = self.app.get('/misfire?count=0')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_misfire_toohigh_route(self):
#        response = self.app.get('/misfire?count=101')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_misfire_nondigit_route(self):
#        response = self.app.get('/misfire?count=duck')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_misfire_route(self):
#        response = self.app.get('/misfire?count=5')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_misfire_builder_route(self):
#        response = self.app.get('/misfire_builder')
#        self.assertTemplateUsed('generic_builder.html')
#        self.assert200(response)
#
#################################################################
#
#    def test_flaw_route(self):
#        response = self.app.get('/flaw?seed=99')
#        self.assertIn('seed=99', response.data)
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_flaw_toolow_route(self):
#        response = self.app.get('/flaw?count=0')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_flaw_toohigh_route(self):
#        response = self.app.get('/flaw?count=101')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_flaw_nondigit_route(self):
#        response = self.app.get('/flaw?count=duck')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_flaw_route(self):
#        response = self.app.get('/flaw?count=5')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_flaw_builder_route(self):
#        response = self.app.get('/flaw_builder')
#        self.assertTemplateUsed('generic_builder.html')
#        self.assert200(response)
#
#################################################################
#
#    def test_currency_route(self):
#        response = self.app.get('/currency?seed=99')
#        self.assertIn('seed=99', response.data)
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_currency_toolow_route(self):
#        response = self.app.get('/currency?count=0')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_currency_toohigh_route(self):
#        response = self.app.get('/currency?count=101')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_currency_nondigit_route(self):
#        response = self.app.get('/currency?count=duck')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_currency_route(self):
#        response = self.app.get('/currency?count=5')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_currency_builder_route(self):
#        response = self.app.get('/currency_builder')
#        self.assertTemplateUsed('generic_builder.html')
#        self.assert200(response)
#
#################################################################
#
#    def test_jobposting_route(self):
#        response = self.app.get('/jobposting?seed=99')
#        self.assertIn('seed=99', response.data)
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_jobposting_toolow_route(self):
#        response = self.app.get('/jobposting?count=0')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_jobposting_toohigh_route(self):
#        response = self.app.get('/jobposting?count=101')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_jobposting_nondigit_route(self):
#        response = self.app.get('/jobposting?count=duck')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_jobposting_route(self):
#        response = self.app.get('/jobposting?count=5')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_jobposting_builder_route(self):
#        response = self.app.get('/jobposting_builder')
#        self.assertTemplateUsed('generic_builder.html')
#        self.assert200(response)
#
#################################################################
#
#    def test_event_route(self):
#        response = self.app.get('/event?seed=99')
#        self.assertIn('seed=99', response.data)
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_event_toolow_route(self):
#        response = self.app.get('/event?count=0')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_event_toohigh_route(self):
#        response = self.app.get('/event?count=101')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_event_nondigit_route(self):
#        response = self.app.get('/event?count=duck')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_event_route(self):
#        response = self.app.get('/event?count=5')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_event_builder_route(self):
#        response = self.app.get('/event_builder')
#        self.assertTemplateUsed('generic_builder.html')
#        self.assert200(response)
#
#################################################################
#
#    def test_motivation_route(self):
#        response = self.app.get('/motivation?seed=99')
#        self.assertIn('seed=99', response.data)
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_motivation_toolow_route(self):
#        response = self.app.get('/motivation?count=0')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_motivation_toohigh_route(self):
#        response = self.app.get('/motivation?count=101')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_motivation_nondigit_route(self):
#        response = self.app.get('/motivation?count=duck')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_motivation_route(self):
#        response = self.app.get('/motivation?count=5')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_motivation_builder_route(self):
#        response = self.app.get('/motivation_builder')
#        self.assertTemplateUsed('generic_builder.html')
#        self.assert200(response)
#
#################################################################
#
#    def test_phobia_route(self):
#        response = self.app.get('/phobia?seed=99')
#        self.assertIn('seed=99', response.data)
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_phobia_toolow_route(self):
#        response = self.app.get('/phobia?count=0')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_phobia_toohigh_route(self):
#        response = self.app.get('/phobia?count=101')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_phobia_nondigit_route(self):
#        response = self.app.get('/phobia?count=duck')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_phobia_route(self):
#        response = self.app.get('/phobia?count=5')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_phobia_builder_route(self):
#        response = self.app.get('/phobia_builder')
#        self.assertTemplateUsed('generic_builder.html')
#        self.assert200(response)
#
#################################################################
#
#    def test_gem_route(self):
#        response = self.app.get('/gem?seed=99')
#        self.assertIn('seed=99', response.data)
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_gem_toolow_route(self):
#        response = self.app.get('/gem?count=0')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_gem_toohigh_route(self):
#        response = self.app.get('/gem?count=101')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_gem_nondigit_route(self):
#        response = self.app.get('/gem?count=duck')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_gem_route(self):
#        response = self.app.get('/gem?count=5')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_gem_builder_route(self):
#        response = self.app.get('/gem_builder')
#        self.assertTemplateUsed('generic_builder.html')
#        self.assert200(response)
#
#################################################################
#
#    def test_mundaneitem_route(self):
#        response = self.app.get('/mundaneitem?seed=99')
#        self.assertIn('seed=99', response.data)
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_mundaneitem_toolow_route(self):
#        response = self.app.get('/mundaneitem?count=0')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_mundaneitem_toohigh_route(self):
#        response = self.app.get('/mundaneitem?count=101')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_mundaneitem_nondigit_route(self):
#        response = self.app.get('/mundaneitem?count=duck')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_mundaneitem_route(self):
#        response = self.app.get('/mundaneitem?count=5')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_mundaneitem_builder_route(self):
#        response = self.app.get('/mundaneitem_builder')
#        self.assertTemplateUsed('generic_builder.html')
#        self.assert200(response)
#
#################################################################
#
#    def test_legend_route(self):
#        response = self.app.get('/legend?seed=99')
#        self.assertIn('seed=99', response.data)
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_legend_toolow_route(self):
#        response = self.app.get('/legend?count=0')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_legend_toohigh_route(self):
#        response = self.app.get('/legend?count=101')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_legend_nondigit_route(self):
#        response = self.app.get('/legend?count=duck')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_legend_route(self):
#        response = self.app.get('/legend?count=5')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_legend_builder_route(self):
#        response = self.app.get('/legend_builder')
#        self.assertTemplateUsed('generic_builder.html')
#        self.assert200(response)
#
#################################################################
#
#    def test_cuisine_route(self):
#        response = self.app.get('/cuisine?seed=99')
#        self.assertIn('seed=99', response.data)
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_cuisine_toolow_route(self):
#        response = self.app.get('/cuisine?count=0')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_cuisine_toohigh_route(self):
#        response = self.app.get('/cuisine?count=101')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_cuisine_nondigit_route(self):
#        response = self.app.get('/cuisine?count=duck')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_cuisine_route(self):
#        response = self.app.get('/cuisine?count=5')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_cuisine_builder_route(self):
#        response = self.app.get('/cuisine_builder')
#        self.assertTemplateUsed('generic_builder.html')
#        self.assert200(response)
#
#################################################################
#
#    def test_phobia_route(self):
#        response = self.app.get('/phobia?seed=99')
#        self.assertIn('seed=99', response.data)
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_phobia_toolow_route(self):
#        response = self.app.get('/phobia?count=0')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_phobia_toohigh_route(self):
#        response = self.app.get('/phobia?count=101')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_phobia_nondigit_route(self):
#        response = self.app.get('/phobia?count=duck')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertNotIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_multi_phobia_route(self):
#        response = self.app.get('/phobia?count=5')
#        self.assertTemplateUsed('oneliner.html')
#        self.assertIn('oneliner-list', response.data)
#        self.assert200(response)
#
#    def test_phobia_builder_route(self):
#        response = self.app.get('/phobia_builder')
#        self.assertTemplateUsed('generic_builder.html')
#        self.assert200(response)
