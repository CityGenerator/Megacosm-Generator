#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."
#

import megacosm
from flask_testing import TestCase
import fakeredis
from fixtures import bond, business, city, continent, country, cuisine, currency, curse, deity, drink, dungeon, event
from fixtures import flag, flaw, gem, generator, geomorphdungeon, govt, grafitti, jobposting, leader, legend, magicitem
from fixtures import misfire, moon, mundaneitem, npc, organization, motivation, planet, phobia, region, resource
from fixtures import roguedungeon, rumor, sect, star, starsystem, street, wanted, weather


class MegacosmFlaskTestCast(TestCase):

    def create_app(self):
        """ """
        app = megacosm.create_app('config.TestConfiguration')
        app.debug = True
        return app

    def setUp(self):
        megacosm.app.config['REDIS'] = fakeredis.FakeRedis(decode_responses=True)
        self.app = megacosm.app.test_client()
        self.redis = megacosm.app.config['REDIS']

        bond.import_fixtures(self)
        business.import_fixtures(self)
        city.import_fixtures(self)
        continent.import_fixtures(self)
        country.import_fixtures(self)
        cuisine.import_fixtures(self)
        currency.import_fixtures(self)
        curse.import_fixtures(self)
        deity.import_fixtures(self)
        dungeon.import_fixtures(self)
        event.import_fixtures(self)
        flag.import_fixtures(self)
        gem.import_fixtures(self)
        geomorphdungeon.import_fixtures(self)
        govt.import_fixtures(self)
        jobposting.import_fixtures(self)
        leader.import_fixtures(self)
        legend.import_fixtures(self)
        misfire.import_fixtures(self)
        magicitem.import_fixtures(self)
        moon.import_fixtures(self)
        motivation.import_fixtures(self)
        mundaneitem.import_fixtures(self)
        npc.import_fixtures(self)
        organization.import_fixtures(self)
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
        weather.import_fixtures(self)
        wanted.import_fixtures(self)
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


