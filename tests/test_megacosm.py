#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import megacosm
from flask.ext.testing import TestCase
import fakeredis
import fixtures
from flask import Flask


class MegacosmFlaskTestCast(TestCase):

    def create_app(self):
        """ """
        app = megacosm.create_app('config.TestConfiguration')
        megacosm.app.debug = False
        megacosm.app.server=fakeredis.FakeRedis()
        return app

    def setUp(self):
        self.app = megacosm.app.test_client()
        self.redis=megacosm.app.server
        fixtures.bond.import_fixtures(self)
        fixtures.business.import_fixtures(self)
        fixtures.city.import_fixtures(self)
        fixtures.continent.import_fixtures(self)
        fixtures.country.import_fixtures(self)
        fixtures.cuisine.import_fixtures(self)
        fixtures.currency.import_fixtures(self)
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
        fixtures.moon.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        fixtures.npc.import_fixtures(self)
        fixtures.organization.import_fixtures(self)
        fixtures.planet.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.region.import_fixtures(self)
        fixtures.sect.import_fixtures(self)
        fixtures.star.import_fixtures(self)
        fixtures.starsystem.import_fixtures(self)
        fixtures.street.import_fixtures(self)

#        self.redis.hset('armor_ability_description', 'shock', '{"name":"shock",        "description":"has a chance of stunning an attacker" }')
#        self.redis.hset('armor_category_description', 'leatherarmor', '{"name":"leather armor",     "materialpart":"chest" }')
#        self.redis.hset('armor_decoration_description', 'flames', '{"name":"flames",   "description":"streaks of red and yellow which glisten like flames"  }')
#        self.redis.hset('armor_effect_description', 'muffled', '{"name":"muffled",          "description":"allows the wearer to move more quietly than otherwise possible" }')
#        self.redis.hset('armor_flaw_description', 'dent', '{"name":"dent", "description":"" }')
#        self.redis.hset('armor_material_description', 'coldiron', '{"name":"cold iron",       "description":"beautiful cold steel"    }')
#        self.redis.hset('armor_visualcause_description', 'orc', '{"name":"orc",      "description":"exposed to orcs"         }')
#        self.redis.hset('armor_visualeffect_description', 'sparkles', '{"name":"sparkles",    "description":"emits a faint sparkle"                   }')
#        self.redis.hset('curse_kind_description', 'bezerker', '{"name":"bezerker", "description":"causes intermittent, uncontrollable rage in the victim"  }')
#        self.redis.hset('gem_kind_description', 'emerald', '{ "name":"emerald", "color":["green"] }')
#        self.redis.hset('roguedungeonroom_kind_description', 'audiencechamber', '{ "name":"audience chamber",   "description":""   }')
#
#        self.redis.lpush('armor_ability', 'shock')
#        self.redis.lpush('armor_category', 'leatherarmor')
#        self.redis.lpush('armor_decoration', 'flames')
#        self.redis.lpush('armor_effect', 'muffled')
#        self.redis.lpush('armor_flaw', 'dent')
#        self.redis.lpush('armor_material', 'coldiron')
#        self.redis.lpush('armor_name_template', '{{ params.effect_description["name"] }} {{ params.category_description["name"]}}{%if params.ability_description%} of {{params.ability_description["name"]}}{%endif%}')
#        self.redis.lpush('armor_visualcause', 'orc')
#        self.redis.lpush('armor_visualeffect', 'sparkles')
#        self.redis.lpush('artwork_cloth_item', 'glove')
#        self.redis.lpush('artwork_cloth_material', 'silk')
#        self.redis.lpush('artwork_item_decoration', 'bear')
#        self.redis.lpush('artwork_item', 'harp')
#        self.redis.lpush('artwork_item_material', 'ivory')
#        self.redis.lpush('artwork_jewelry', 'ring')
#        self.redis.lpush('artwork_metal', 'bronze')
#        self.redis.lpush('artwork_template', "a necklace of {{params.gem.size}} {{params.gem.kind_description['name']|pluralize(2)}}")
#        self.redis.lpush('artwork_weapon', 'dagger')
#        self.redis.lpush('curse_kind', 'bezerker')
#        self.redis.lpush('curse_removal', 'performing an epic task')
#        self.redis.lpush('curse_template', "The {{params.kind_description['name']|title}} Curse {{params.kind_description['description']}}, and can only be undone by {{params.removal}}. Untreated, the effects of the curse {{params.duration['name']}}.")
#
#        self.redis.lpush('gem_kind', 'emerald')
#        self.redis.lpush('gem_template', 'A Gem Template')
#        self.redis.lpush('magicitem_creator_template', '{{npc.race | article}} named {{npc.name["full"]}}')
#        self.redis.lpush('magicitem_kind', 'armor')
#        self.redis.lpush('magicitem_location', 'buried in a nest')
#        self.redis.lpush('magicitem_vibe', 'gives you feelings of power')
#        self.redis.lpush('magicitem_vibe_when', 'looking at')
#        self.redis.lpush('misfire_template', '{{params.target}} grow a pair of small horns (2 in each) on the forehead, which contrasts with skin color.  A remove curse may remove them.')
#        self.redis.lpush('motivationacceptance_text', 'to impress someone')
#        self.redis.lpush('motivation_kind', 'acceptance')
#        self.redis.lpush('mundaneitem_kind', 'wool tunic')
#        self.redis.lpush('naturalresource_crop_name', 'crop')
#        self.redis.lpush('naturalresource_crop_name_type', 'wild')
#        self.redis.lpush('naturalresource_crop_product', 'cocoa beans')
#        self.redis.lpush('naturalresource_kind', 'crop')
#        self.redis.lpush('resource_kind', 'naturalresource')
#        self.redis.lpush('resource_template', '"{{params.place.name["full"]}} is known for its {{params.name_type}} {{params.name}} which {{params.method}} {{params.product}}. This resource is {{params.ubiquity["name"]}} to the region. Many consider the {{params.product}} {{params.utility["name"]}}, and are regardless seen as a {{params.value["name"]}} resource. Competition in the {{params.product}} market is {{params.competition["name"]}}, and the {{params.name}} resource as a whole are {{params.management["name"]}} managed."')
#        self.redis.lpush('roguedungeonroom_kind', 'audiencechamber')
#        self.redis.lpush('roguedungeon_theme', 'fortress')
#        self.redis.lpush('skin_skincolor','alabaster')
#        self.redis.lpush('skin_skinkind', 'thick')
#        self.redis.lpush('starposition', '{"name": "companion2",    "x":-150,    "y":-4,  "z":4  }' )
#        self.redis.lpush('starposition', '{"name": "companion",    "x":-150,    "y":4,  "z":4  }' )
#        self.redis.lpush('wanted_by', 'Regional Authorities')
#        self.redis.lpush('wanted_condition', 'proof of death')
#        self.redis.lpush('wanted_crime', 'Desecration')
#        self.redis.lpush('wanted_headline', 'Notice:')
#        self.redis.lpush('wanted_lastseen', 'underground')
#        self.redis.lpush('wanted_reward', '10 gold')
#        self.redis.lpush('wanted_title', '"Loathsome"')
#        self.redis.lpush('wanted_warning', 'has killed before')
#        self.redis.lpush('weather_cloud', 'cumulus')
#        self.redis.lpush('weather_storm', 'downburst')
#        self.redis.lpush('weather_time', 'in the early evening')
#        self.redis.set('magicitem_curse_chance', '40')
#        self.redis.set('skin_covertemplate', '{{params.skinkind}}, {{params.skincolor}} skin')
#        self.redis.zadd('curse_duration','{"name":"last a lifetime",       "score":100 }', 100)
#        self.redis.zadd('gem_amount',  '{ "name":"a single",  "min":1, "max":100, "score":100  }',100.0)
#        self.redis.zadd('gem_quality',  '{ "name":"chipped", "score":100  }',100.0)
#        self.redis.zadd('gem_saturation',  '{ "name":"blanched", "score":100  }',100.0)
#        self.redis.zadd('gem_value',  '{ "name":"costly", "score":100  }',100.0)
#        self.redis.zadd('magicitem_age', '{"name":"over a century ago",    "score":100 }', 100)
#        self.redis.zadd('magicitem_quality', '{"name":"excellent","score":100 }', 100)
#        self.redis.zadd('magicitem_repair', '{"name":"in pristine condition",     "score":100 }', 100)
#        self.redis.zadd('magicitem_strength', '{"name":"powerful",     "score":100  }', 100)
#        self.redis.zadd('magicitem_value', '{"name":"artifact",              "score": 100  }', 100)
#        self.redis.zadd('mundaneitem_quality', '{"name":"excellent","score":100 }', 100)
#        self.redis.zadd('mundaneitem_repair', '{"name":"in pristine condition",     "score":100 }', 100)
#        #Details for Kobolds
# 
#
#        self.redis.zadd('resource_competition', '{  "name":"fierce",             "score":100      }', 100)
#        self.redis.zadd('resource_depletion', '{  "name":"bountiful",           "score":100      }', 100)
#        self.redis.zadd('resource_exportregion', '{  "name":"across the continent",           "score":100      }', 100)
#        self.redis.zadd('resource_management', '{  "name":"well",           "score":100      }', 100)
#        self.redis.zadd('resource_ubiquity', '{  "name":"not specific",       "score":100       }', 100)
#        self.redis.zadd('resource_utility', '{  "name":"useful",          "score":100      }', 100)
#        self.redis.zadd('resource_value', '{  "name":"valuable",          "score":100      }', 100)
#        self.redis.zadd('roguedungeon_build', '{"name":"dungeon and caves",    "score": 100  }', 100)
#        self.redis.zadd('roguedungeon_refinement', '{"name":"dungeon",                             "score": 100  }', 100)
#        self.redis.zadd('roguedungeon_room_count', '{"name":"lots",       "minsize":25, "maxsize":50,  "score": 100  }', 100)
#        self.redis.zadd('roguedungeon_room_size', '{"name":"gigantic", "minsize":3,  "maxsize":20,   "score": 100  }', 100)
#        self.redis.zadd('roguedungeon_size', '{"name":"gigantic", "minsize":60, "maxsize":60,   "score": 100  }', 100)
#        self.redis.zadd('weather_precipitation', '{ "name":"heavily",    "score":100     }', 100)
#        self.redis.zadd('weather_temp', '{ "name":"unbearably hot",   "score":100     }', 100)
#        self.redis.zadd('weather_wind', '{ "name":"hurricane-force",  "score":100     }', 100)

    def tearDown(self):
        megacosm.app.server.flushall()
        self.app = None

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

###############################################################

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

##############################################################

    def test_index_route(self):
        response = self.app.get('/')
        self.assertTemplateUsed('index.html')
        self.assert200(response)

##############################################################

    def test_bond_route(self):
        self.redis.lpush('npc_race','kobold')
        response = self.app.get('/bond')
        self.assert200(response)

    def test_bond_builder_route(self):
        response = self.app.get('/bond_builder')
        self.assert200(response)

#############################################################

    def test_business_route(self):
        self.redis.lpush('npc_race','kobold')
        response = self.app.get('/business')
        self.assert200(response)

    def test_business_builder_route(self):
        response = self.app.get('/business_builder')
        self.assert200(response)
###############################################################

    def test_city_route(self):
        self.redis.lpush('npc_race','kobold')
        response = self.app.get('/city')
        self.assert200(response)

    def test_city_builder_route(self):
        response = self.app.get('/city_builder')
        self.assert200(response)

###############################################################

    def test_continent_route(self):
        response = self.app.get('/continent')
        self.assert200(response)

    def test_continent_builder_route(self):
        response = self.app.get('/continent_builder')
        self.assert200(response)

###############################################################

    def test_country_route(self):
        response = self.app.get('/country')
        self.assert200(response)

    def test_country_builder_route(self):
        response = self.app.get('/country_builder')
        self.assert200(response)

###############################################################

    def test_cuisine_route(self):
        self.redis.lpush('npc_race','kobold')
        response = self.app.get('/cuisine')
        self.assert200(response)

    def test_cuisine_builder_route(self):
        response = self.app.get('/cuisine_builder')
        self.assert200(response)

##############################################################

    def test_currency_route(self):
        self.redis.lpush('npc_race','kobold')
        response = self.app.get('/currency')
        self.assert200(response)

    def test_currency_builder_route(self):
        response = self.app.get('/currency_builder')
        self.assert200(response)

##############################################################

    def test_deity_route(self):
        self.redis.lpush('npc_race','kobold')
        response = self.app.get('/deity')
        self.assert200(response)

    def test_deity_builder_route(self):
        response = self.app.get('/deity_builder')
        self.assert200(response)

###############################################################

    def test_event_route(self):
        self.redis.lpush('npc_race','kobold')
        response = self.app.get('/event')
        self.assert200(response)

    def test_event_builder_route(self):
        response = self.app.get('/event_builder')
        self.assert200(response)

###############################################################

    def test_flag_route(self):
        response = self.app.get('/flag')
        self.assert200(response)

    def test_flag_builder_route(self):
        response = self.app.get('/flag_builder')
        self.assert200(response)

###############################################################

    def test_gem_route(self):
        response = self.app.get('/gem')
        self.assert200(response)

    def test_gem_builder_route(self):
        response = self.app.get('/gem_builder')
        self.assert200(response)

###############################################################

    def test_geomorphdungeon_route(self):
        response = self.app.get('/geomorphdungeon')
        self.assert200(response)

    def test_geomorphdungeon_builder_route(self):
        response = self.app.get('/geomorphdungeon_builder')
        self.assert200(response)

###############################################################

    def test_govt_route(self):
        response = self.app.get('/govt')
        self.assert200(response)

    def test_govt_builder_route(self):
        response = self.app.get('/govt_builder')
        self.assert200(response)

################################################################

    def test_jobposting_route(self):
        self.redis.lpush('npc_race','kobold')
        response = self.app.get('/jobposting')
        self.assert200(response)

    def test_jobposting_builder_route(self):
        response = self.app.get('/jobposting_builder')
        self.assert200(response)

#################################################################
#
#    def test_leader_route(self):
#        response = self.app.get('/leader')
#        self.assert200(response)
#
#    def test_leader_builder_route(self):
#        response = self.app.get('/leader_builder')
#        self.assert200(response)
#
#################################################################
#
    def test_legend_route(self):
        self.redis.lpush('npc_race','kobold')
        response = self.app.get('/legend')
        self.assert200(response)

    def test_legend_builder_route(self):
        response = self.app.get('/legend_builder')
        self.assert200(response)

################################################################
#
#    def test_magicitem_route(self):
#        response = self.app.get('/magicitem')
#        self.assert200(response)
#
#    def test_magicitem_builder_route(self):
#        response = self.app.get('/magicitem_builder')
#        self.assert200(response)
#
################################################################

    def test_misfire_route(self):
        self.redis.lpush('npc_race','kobold')
        response = self.app.get('/misfire')
        self.assert200(response)

    def test_misfire_builder_route(self):
        response = self.app.get('/misfire_builder')
        self.assert200(response)

################################################################
#
#    def test_moon_route(self):
#        response = self.app.get('/moon')
#        self.assert200(response)
#
#    def test_moon_builder_route(self):
#        response = self.app.get('/moon_builder')
#        self.assert200(response)
#
#################################################################
#
#    def test_motivation_route(self):
#        response = self.app.get('/motivation')
#        self.assert200(response)
#
#    def test_motivation_builder_route(self):
#        response = self.app.get('/motivation_builder')
#        self.assert200(response)
#
################################################################
#
#    def test_organization_route(self):
#        self.redis.lpush('npc_race','kobold')
#        response = self.app.get('/organization')
#        self.assert200(response)
#
#    def test_organization_builder_route(self):
#        self.redis.lpush('npc_race','kobold')
#        response = self.app.get('/organization_builder')
#        self.assert200(response)
#
################################################################
#
#    def test_phobia_route(self):
#        response = self.app.get('/phobia')
#        self.assert200(response)
#
#    def test_phobia_builder_route(self):
#        response = self.app.get('/phobia_builder')
#        self.assert200(response)
#
#################################################################
#
#    def test_mundaneitem_route(self):
#        response = self.app.get('/mundaneitem')
#        self.assert200(response)
#
#    def test_mundaneitem_builder_route(self):
#        response = self.app.get('/mundaneitem_builder')
#        self.assert200(response)
#
################################################################

#    def test_npc_route(self):
#        self.redis.lpush('npc_race','kobold')
#
#        response = self.app.get('/npc')
#        self.assert200(response)
#
#    def test_npc_builder_route(self):
#        self.redis.lpush('npc_race','kobold')
#
#        response = self.app.get('/npc_builder')
#        self.assert200(response)

################################################################
#
#    def test_planet_route(self):
#        response = self.app.get('/planet')
#        self.assert200(response)
#
#    def test_planet_builder_route(self):
#        response = self.app.get('/planet_builder')
#        self.assert200(response)
#
#################################################################
#
#    def test_region_route(self):
#        response = self.app.get('/region')
#        self.assert200(response)
#
#    def test_region_builder_route(self):
#        response = self.app.get('/region_builder')
#        self.assert200(response)
#
#################################################################
#
#    def test_resource_route(self):
#        response = self.app.get('/resource')
#        self.assert200(response)
#
#    def test_resource_builder_route(self):
#        response = self.app.get('/resource_builder')
#        self.assert200(response)
#
#################################################################
#
#    def test_roguedungeon_route(self):
#        response = self.app.get('/roguedungeon')
#        self.assert200(response)
#
#    def test_roguedungeon_builder_route(self):
#        response = self.app.get('/roguedungeon_builder')
#        self.assert200(response)
#
#################################################################
#
#    def test_rumor_route(self):
#        response = self.app.get('/rumor')
#        self.assert200(response)
#
#    def test_rumor_builder_route(self):
#        response = self.app.get('/rumor_builder')
#        self.assert200(response)
#
#################################################################
#
#    def test_sect_route(self):
#        response = self.app.get('/sect')
#        self.assert200(response)
#
#    def test_sect_builder_route(self):
#        response = self.app.get('/sect_builder')
#        self.assert200(response)
#
#################################################################
#
#    def test_star_route(self):
#        response = self.app.get('/star')
#        self.assert200(response)
#
#    def test_star_builder_route(self):
#        response = self.app.get('/star_builder')
#        self.assert200(response)
#
#################################################################
#
#    def test_street_route(self):
#        response = self.app.get('/street')
#        self.assert200(response)
#
#    def test_street_builder_route(self):
#        response = self.app.get('/street_builder')
#        self.assert200(response)
#
#################################################################
#
#    def test_wanted_route(self):
#        response = self.app.get('/wanted')
#        self.assert200(response)
#
#    def test_wanted_builder_route(self):
#        response = self.app.get('/wanted_builder')
#        self.assert200(response)
#
#################################################################
#
#    def test_weather_route(self):
#        response = self.app.get('/weather')
#        self.assert200(response)
#
#    def test_weather_builder_route(self):
#        response = self.app.get('/weather_builder')
#        self.assert200(response)
#################################################################
#
#    def test_404_route(self):
#        response = self.app.get('/brokenroute')
#        self.assert404(response)
#
#################################################################
#    def test_feature_filter_npc(self):
#        response = self.app.get('/npc?npc_endurance_roll=100&npc_medical_condition=0')
#        self.assert200(response)
#
#    def test_feature_filter_business(self):
#        response = self.app.get('/business?business_kind=bus_adventurersguild')
#        self.assert200(response)
#        response = self.app.get('/business?business_kind=nothingcorrect')
#        self.assert200(response)
#        response = self.app.get('/business?business_kind=@@@')
#        self.assert200(response)
#        response = self.app.get('/business?business_kindof=bogus')
#        self.assert200(response)
#
#
