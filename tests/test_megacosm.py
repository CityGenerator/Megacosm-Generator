#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."
#

import megacosm
from flask_testing import TestCase
import fakeredis
import fixtures


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
        fixtures.gem.import_fixtures(self)
        fixtures.geomorphdungeon.import_fixtures(self)
        fixtures.govt.import_fixtures(self)
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
        self.redis.lpush('npc_race','kobold')

    def tearDown(self):
        self.redis.flushall()
        self.app = None

################################################################

    def test_builder_form_data(self):
        self.redis.lpush('unittestgenerator_list', 'a', 'b', 'c')
        self.redis.set('unittestgenerator_list_chance', 30)
        self.redis.zadd('unittestgenerator_range', {'{"name":"test1"}': 50})
        self.redis.zadd('unittestgenerator_range', {'{"name":"test2"}': 100})
        self.redis.hset('unittestgenerator_list_description', 'foo', '{"name":"test1"}')
        self.redis.hset('unittestgenerator_list-description', 'bar', '{"name":"test2"}')
        self.assertEquals(megacosm.builder_form_data('unittestgenerator'), ({'list': ['c', 'b', 'a']},
                          {'list_chance': '30'}, {'range': [{u'name': u'test1'}, {u'name': u'test2'}]}))

        self.redis.zadd('unittestgenerator_range', {'{"name":"test2"': 100})

        with self.assertRaisesRegexp(ValueError, 'failed to parse unittestgenerator_range field {"name":"test2"'):
            megacosm.builder_form_data('unittestgenerator')

    def test_isvalidscore(self):
        self.assertTrue(megacosm.isvalidscore('100'))
        self.assertTrue(megacosm.isvalidscore('50'))
        self.assertTrue(megacosm.isvalidscore('0'))
        self.assertFalse(megacosm.isvalidscore('-10'))
        self.assertFalse(megacosm.isvalidscore('1010'))
        self.assertFalse(megacosm.isvalidscore('Fred'))
################################################################

    def test_select_uppercase(self):
        self.assertEquals('DOG', megacosm.select_uppercase('dog'))
        self.assertEquals('APPLE?', megacosm.select_uppercase('Apple?'))
        self.assertEquals('HOUR.!', megacosm.select_uppercase('HOUR.!'))

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

    def test_select_plural_adj(self):
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

################################################################


    def test_business_route(self):
        response = self.app.get('/business')
        self.assert200(response)

    def test_business_builder_route(self):
        response = self.app.get('/business_builder')
        self.assert200(response)
################################################################

    def test_city_route(self):
        response = self.app.get('/city')
        self.assert200(response)

    def test_city_builder_route(self):
        response = self.app.get('/city_builder')
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

    def test_deity_route(self):
        response = self.app.get('/deity')
        self.assert200(response)

    def test_deity_builder_route(self):
        response = self.app.get('/deity_builder')
        self.assert200(response)

################################################################

    def test_flag_route(self):
        response = self.app.get('/flag')
        self.assert200(response)

    def test_flag_builder_route(self):
        response = self.app.get('/flag_builder')
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

################################################################

    def test_leader_route(self):
        response = self.app.get('/leader')
        self.assert200(response)

    def test_leader_builder_route(self):
        response = self.app.get('/leader_builder')
        self.assert200(response)

################################################################

    def test_magicitem_route(self):
        response = self.app.get('/magicitem')
        self.assert200(response)

    def test_magicitem_builder_route(self):
        response = self.app.get('/magicitem_builder')
        self.assert200(response)

###############################################################

    def test_moon_route(self):
        response = self.app.get('/moon')
        self.assert200(response)

    def test_moon_builder_route(self):
        response = self.app.get('/moon_builder')
        self.assert200(response)

################################################################

    def test_organization_route(self):
        response = self.app.get('/organization')
        self.assert200(response)

    def test_organization_builder_route(self):
        response = self.app.get('/organization_builder')
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

    def test_roguedungeon_route(self):
        response = self.app.get('/roguedungeon')
        self.assert200(response)

    def test_roguedungeon_builder_route(self):
        response = self.app.get('/roguedungeon_builder')
        self.assert200(response)

################################################################

    def test_sect_route(self):
        response = self.app.get('/sect')
        self.assert200(response)

    def test_sect_builder_route(self):
        response = self.app.get('/sect_builder')
        self.assert200(response)

#################################################################

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
################################################################

    def test_404_route(self):
        response = self.app.get('/brokenroute')
        self.assert404(response)

################################################################
    def test_feature_filter_npc(self):
        response = self.app.get('/npc?npc_endurance_roll=100&npc_medical_condition=0')
        self.assert200(response)

    def test_feature_filter_business(self):
        response = self.app.get('/business?business_kind=bus_adventurersguild')
        self.assert200(response)
        response = self.app.get('/business?business_kind=nothingcorrect')
        self.assert200(response)
        response = self.app.get('/business?business_kind=@@@')
        self.assert200(response)
        response = self.app.get('/business?business_kindof=bogus')
        self.assert200(response)


