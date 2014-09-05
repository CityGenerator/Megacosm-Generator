#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import megacosm
import unittest2 as unittest
from flask.ext.testing import TestCase
from flask import Flask


class MegacosmFlaskTestCast(TestCase):

#

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

################################################################

    def test_builder_form_data(self):
        megacosm.app.server.lpush('unittestgenerator_list', 'a', 'b', 'c')
        megacosm.app.server.set('unittestgenerator_list_chance', 30)
        megacosm.app.server.zadd('unittestgenerator_range', '{"name":"test1"}', 50)
        megacosm.app.server.zadd('unittestgenerator_range', '{"name":"test2"}', 100)
        megacosm.app.server.hset('unittestgenerator_list_description', 'foo', '{"name":"test1"}')
        megacosm.app.server.hset('unittestgenerator_list-description', 'bar', '{"name":"test2"}')
        self.assertEquals(megacosm.builder_form_data('unittestgenerator'), ({'list': ['c', 'b', 'a']},
                          {'list_chance': '30'}, {'range': [{u'name': u'test1'}, {u'name': u'test2'}]}))

        megacosm.app.server.zadd('unittestgenerator_range', '{"name":"test2"', 100)

        with self.assertRaisesRegexp(ValueError, 'failed to parse unittestgenerator_range field {"name":"test2"') as \
            context:
            megacosm.builder_form_data('unittestgenerator')

#    paramlist={}
#    paramstring={}
#    paramset={}
#    for key in server.keys(generator+'_*'):
#        fieldname=key.replace(generator+'_','')
#        if server.type(key) == 'list' :
#            paramlist[fieldname]=server.lrange(key,0,-1)
#        elif server.type(key) == 'string' :
#            paramstring[fieldname]=server.get(key)
#        elif server.type(key) == 'zset' :
#            result= server.zrangebyscore(key,1,100)
#            paramset[fieldname]=[]
#            for field in result:
#                try:
#                    paramset[fieldname].append( json.loads(field))
#                except ValueError as e:
#                    raise Exception ("failed to parse",key,"field", field)
#    return paramlist,paramstring,paramset

################################################################

    def test_isvalidscore(self):
        self.assertTrue(megacosm.isvalidscore('100'))
        self.assertTrue(megacosm.isvalidscore('50'))
        self.assertTrue(megacosm.isvalidscore('0'))
        self.assertFalse(megacosm.isvalidscore('-10'))
        self.assertFalse(megacosm.isvalidscore('1010'))
        self.assertFalse(megacosm.isvalidscore('Fred'))

################################################################

    def test_select_article(self):
        self.assertEquals('a dog', megacosm.select_article('dog'))
        self.assertEquals('an apple', megacosm.select_article('apple'))
        self.assertEquals('an hour', megacosm.select_article('hour'))

################################################################

    def test_select_pluralize(self):
        self.assertEquals('dogs', megacosm.select_pluralize('dog', 0))
        self.assertEquals('dog', megacosm.select_pluralize('dog', 1))
        self.assertEquals('dogs', megacosm.select_pluralize('dog', 2))
        self.assertEquals('classes', megacosm.select_pluralize('class', 0))
        self.assertEquals('class', megacosm.select_pluralize('class', 1))
        self.assertEquals('classes', megacosm.select_pluralize('class', 2))

################################################################

    def test_select_conjunction(self):
        self.assertEquals('a', megacosm.select_conjunction(['a']))
        self.assertEquals('a and b', megacosm.select_conjunction(['a', 'b']))
        self.assertEquals('a, b, and c', megacosm.select_conjunction(['a', 'b', 'c']))
        self.assertEquals('a, b, c, and d', megacosm.select_conjunction(['a', 'b', 'c', 'd']))

################################################################

    def test_select_plural_verb(self):
        self.assertEquals('were', megacosm.select_plural_verb('was', 0))
        self.assertEquals('was', megacosm.select_plural_verb('was', 1))
        self.assertEquals('were', megacosm.select_plural_verb('was', 2))

################################################################

    def test_select_plural_verb(self):
        self.assertEquals('some', megacosm.select_plural_adj('a', 0))
        self.assertEquals('a', megacosm.select_plural_adj('a', 1))
        self.assertEquals('some', megacosm.select_plural_adj('a', 2))

        self.assertEquals('these', megacosm.select_plural_adj('this', 0))
        self.assertEquals('this', megacosm.select_plural_adj('this', 1))
        self.assertEquals('these', megacosm.select_plural_adj('this', 2))

        self.assertEquals('those', megacosm.select_plural_adj('that', 0))
        self.assertEquals('that', megacosm.select_plural_adj('that', 1))
        self.assertEquals('those', megacosm.select_plural_adj('that', 2))

        self.assertEquals('our', megacosm.select_plural_adj('my', 0))
        self.assertEquals('my', megacosm.select_plural_adj('my', 1))
        self.assertEquals('our', megacosm.select_plural_adj('my', 2))

################################################################

    def test_index_route(self):
        response = self.app.get('/')
        self.assertTemplateUsed('index.html')
        self.assert200(response)

###############################################################

    def test_bond_route(self):
        response = self.app.get('/bond')
        self.assert200(response)

    def test_bond_builder_route(self):
        response = self.app.get('/bond_builder')
        self.assert200(response)

################################################################

    def test_business_route(self):
        response = self.app.get('/business')
        self.assert200(response)

    def test_business_builder_route(self):
        response = self.app.get('/business_builder')
        self.assert200(response)

################################################################

    def test_continent_route(self):
        response = self.app.get('/continent')
        self.assert200(response)

    def test_continent_builder_route(self):
        response = self.app.get('/continent_builder')
        self.assert200(response)

################################################################

    def test_country_route(self):
        response = self.app.get('/country')
        self.assert200(response)

    def test_country_builder_route(self):
        response = self.app.get('/country_builder')
        self.assert200(response)

################################################################

    def test_cuisine_route(self):
        response = self.app.get('/cuisine')
        self.assert200(response)

    def test_cuisine_builder_route(self):
        response = self.app.get('/cuisine_builder')
        self.assert200(response)

################################################################

    def test_currency_route(self):
        response = self.app.get('/currency')
        self.assert200(response)

    def test_currency_builder_route(self):
        response = self.app.get('/currency_builder')
        self.assert200(response)

################################################################

    def test_deity_route(self):
        response = self.app.get('/deity')
        self.assert200(response)

    def test_deity_builder_route(self):
        response = self.app.get('/deity_builder')
        self.assert200(response)

################################################################

    def test_event_route(self):
        response = self.app.get('/event')
        self.assert200(response)

    def test_event_builder_route(self):
        response = self.app.get('/event_builder')
        self.assert200(response)

################################################################

    def test_flag_route(self):
        response = self.app.get('/flag')
        self.assert200(response)

    def test_flag_builder_route(self):
        response = self.app.get('/flag_builder')
        self.assert200(response)

################################################################

    def test_gem_route(self):
        response = self.app.get('/gem')
        self.assert200(response)

    def test_gem_builder_route(self):
        response = self.app.get('/gem_builder')
        self.assert200(response)

################################################################

    def test_geomorphdungeon_route(self):
        response = self.app.get('/geomorphdungeon')
        self.assert200(response)

    def test_geomorphdungeon_builder_route(self):
        response = self.app.get('/geomorphdungeon_builder')
        self.assert200(response)

################################################################

    def test_govt_route(self):
        response = self.app.get('/govt')
        self.assert200(response)

    def test_govt_builder_route(self):
        response = self.app.get('/govt_builder')
        self.assert200(response)

################################################################

    def test_jobposting_route(self):
        response = self.app.get('/jobposting')
        self.assert200(response)

    def test_jobposting_builder_route(self):
        response = self.app.get('/jobposting_builder')
        self.assert200(response)

################################################################

    def test_leader_route(self):
        response = self.app.get('/leader')
        self.assert200(response)

    def test_leader_builder_route(self):
        response = self.app.get('/leader_builder')
        self.assert200(response)

################################################################

    def test_legend_route(self):
        response = self.app.get('/legend')
        self.assert200(response)

    def test_legend_builder_route(self):
        response = self.app.get('/legend_builder')
        self.assert200(response)

################################################################

    def test_magicitem_route(self):
        response = self.app.get('/magicitem')
        self.assert200(response)

    def test_magicitem_builder_route(self):
        response = self.app.get('/magicitem_builder')
        self.assert200(response)

################################################################

    def test_misfire_route(self):
        response = self.app.get('/misfire')
        self.assert200(response)

    def test_misfire_builder_route(self):
        response = self.app.get('/misfire_builder')
        self.assert200(response)

################################################################

    def test_moon_route(self):
        response = self.app.get('/moon')
        self.assert200(response)

    def test_moon_builder_route(self):
        response = self.app.get('/moon_builder')
        self.assert200(response)

################################################################

    def test_motivation_route(self):
        response = self.app.get('/motivation')
        self.assert200(response)

    def test_motivation_builder_route(self):
        response = self.app.get('/motivation_builder')
        self.assert200(response)

################################################################

    def test_mundaneitem_route(self):
        response = self.app.get('/mundaneitem')
        self.assert200(response)

    def test_mundaneitem_builder_route(self):
        response = self.app.get('/mundaneitem_builder')
        self.assert200(response)

################################################################

    def test_npc_route(self):
        response = self.app.get('/npc')
        self.assert200(response)

    def test_npc_builder_route(self):
        response = self.app.get('/npc_builder')
        self.assert200(response)

################################################################

    def test_planet_route(self):
        response = self.app.get('/planet')
        self.assert200(response)

    def test_planet_builder_route(self):
        response = self.app.get('/planet_builder')
        self.assert200(response)

################################################################

    def test_region_route(self):
        response = self.app.get('/region')
        self.assert200(response)

    def test_region_builder_route(self):
        response = self.app.get('/region_builder')
        self.assert200(response)

################################################################

    def test_resource_route(self):
        response = self.app.get('/resource')
        self.assert200(response)

    def test_resource_builder_route(self):
        response = self.app.get('/resource_builder')
        self.assert200(response)

################################################################

    def test_roguedungeon_route(self):
        response = self.app.get('/roguedungeon')
        self.assert200(response)

    def test_roguedungeon_builder_route(self):
        response = self.app.get('/roguedungeon_builder')
        self.assert200(response)

################################################################

    def test_rumor_route(self):
        response = self.app.get('/rumor')
        self.assert200(response)

    def test_rumor_builder_route(self):
        response = self.app.get('/rumor_builder')
        self.assert200(response)

################################################################

    def test_sect_route(self):
        response = self.app.get('/sect')
        self.assert200(response)

    def test_sect_builder_route(self):
        response = self.app.get('/sect_builder')
        self.assert200(response)

################################################################

    def test_star_route(self):
        response = self.app.get('/star')
        self.assert200(response)

    def test_star_builder_route(self):
        response = self.app.get('/star_builder')
        self.assert200(response)

################################################################

    def test_street_route(self):
        response = self.app.get('/street')
        self.assert200(response)

    def test_street_builder_route(self):
        response = self.app.get('/street_builder')
        self.assert200(response)

################################################################

    def test_wanted_route(self):
        response = self.app.get('/wanted')
        self.assert200(response)

    def test_wanted_builder_route(self):
        response = self.app.get('/wanted_builder')
        self.assert200(response)

################################################################

    def test_weather_route(self):
        response = self.app.get('/weather')
        self.assert200(response)

    def test_weather_builder_route(self):
        response = self.app.get('/weather_builder')
        self.assert200(response)


