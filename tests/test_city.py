#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import City, Region
import unittest2 as unittest
from mock import Mock, patch, MagicMock
import fakeredis
from config import TestConfiguration


class TestCity(unittest.TestCase):

    def setUp(self):
        """  """
        # TODO see if testconfiguration can put a prefix on redis keys to prevent overlap
        self.redis = fakeredis.FakeRedis()

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
        self.redis.hset('gnome_name_first','post', 100)
        self.redis.hset('gnome_name_last','pre', 100)
        self.redis.zadd('gnome_name_order','{ "name":"first" }',50)
        self.redis.zadd('gnome_name_order','{ "name":"last"}',100)

        #Details for Kobolds
        self.redis.set( 'kobold_details', '{"name": "Kobold",     "size": "small",   "description": "their small stature and cowardice"}') 
        self.redis.lpush('kobold_covering','skin') 
        self.redis.zadd('kobold_name_order','{ "name":"first" }',50) 
        self.redis.hset('kobold_name_first','root', 100) 
        self.redis.lpush('kobold_name_first_root', 'Kole') 
 
        self.redis.zadd('kobold_name_order','{ "name":"last" }',100) 
        self.redis.hset('kobold_name_last','root', 0) 
        self.redis.lpush('kobold_name_last_root', 'Sok') 
 
        self.redis.set('kobold_subrace_chance',100) 
        self.redis.lpush('kobold_subrace', 'aquatic') 
 
        self.redis.hset('kobold_subrace_description', 'aquatic', '{"subrace": "Aquatic Kobold",   "description": "" }') 

        self.redis.zadd('city_size', '{ "name":"capitol",       "minpop":"30001", "maxpop":"80000", "min_density":"240", "max_density":"40000", "min_dist":3,  "max_dist":14 }', 100)
        self.redis.zadd('city_happiness', ' { "name":"estatic",     "score":100   }', 100)
        self.redis.zadd('city_health', ' { "name":"vigorous",       "score":100   }', 100)
        self.redis.zadd('city_age', ' { "name":"ancient",           "score":100    }', 100)
        self.redis.zadd('city_terrain', '{ "name": "jagged",         "score":100   }', 100)
        self.redis.zadd('city_pollution', '{ "name": "squalid",      "score":100  }', 100)
        self.redis.zadd('city_moral', '{ "name": "virtuous",         "score":100   }', 100)
        self.redis.zadd('city_order', '{ "name": "honorable",         "score":100   }', 100)
        self.redis.zadd('city_tolerance', '{ "name": "love",                        "score":100   }', 100)
        self.redis.zadd('city_economy', '{ "name": "lively",                        "score":100   }', 100)
        self.redis.zadd('city_military', '{ "name": "reverent",                     "score":100   }', 100)
        self.redis.zadd('city_magic', '{ "name": "growing",                         "score":100   }', 100)
        self.redis.zadd('city_education', '{ "name": "wonderful",                   "score":100   }', 100)
        self.redis.zadd('city_authority', '{ "name": "is very authoritarian",       "score":100   }', 100)
        self.redis.zadd('city_crime', '{ "name": "unheard of",                      "score":100   }', 100)

        self.redis.lpush('city_shape', 'octagonal')
        self.redis.lpush('city_gatheringplace', 'adventurersguild')

        self.redis.lpush('name_citytitle', 'Alta')
        self.redis.lpush('name_citypre', 'De')
        self.redis.lpush('name_cityroot', 'Allen')
        self.redis.lpush('name_citypost', 'tle')
        self.redis.lpush('name_citytrailer', 'Gate')

        self.redis.lpush('name_regiontitle', 'Upper')
        self.redis.lpush('name_regiontitle', 'New')
        self.redis.lpush('name_regionpre', 'Af')
        self.redis.lpush('name_regionpre', 'Alb')
        self.redis.lpush('name_regionpre', 'Lom')
        self.redis.lpush('name_regionroot', 'ad')
        self.redis.lpush('name_regionroot', 'am')
        self.redis.lpush('name_regionroot', 'bar')
        self.redis.lpush('name_regionpost', 'a')
        self.redis.lpush('name_regionpost', 'ad')
        self.redis.lpush('name_regionpost', 'ain')
        self.redis.lpush('name_regionpost', 'dy')

        self.redis.lpush('orc_covering','skin')
        self.redis.set('orc_details',  '{"name": "Orc",        "size": "medium",  "description": "under-bite and ferocious demeanor"}')
        self.redis.set('elf_details',  '{"name": "Elf",        "size": "medium",  "description": "care-free spirit and lengthy lifespan"}')
        self.redis.lpush('elf_covering','skin')
        self.redis.set('elf_subrace_chance',100) 
        self.redis.lpush('elf_subrace', 'shadowelf') 
        self.redis.hset('elf_subrace_description', 'shadowelf', '{"subrace": "Shadow Elf",   "description": "" }') 
        self.redis.lpush('elf_subrace', 'snowelf') 
        self.redis.hset('elf_subrace_description', 'snowelf', '{"subrace": "Snow Elf",   "description": "" }') 
        self.redis.lpush('elf_subrace', 'waterelf') 
        self.redis.hset('elf_subrace_description', 'waterelf', '{"subrace": "Water Elf",   "description": "" }') 

    def tearDown(self):
        """  """
        self.redis.flushall()

    def test_random_city(self):
        """  """
        city = City(self.redis)
        self.assertEqual('Alta DeAllentle Gate', city.name['full'])
        self.assertEquals(city.name['full'], str(city))

    def test_city_region(self):
        """  """

        region=Region(self.redis)
        city = City(self.redis, {'region': region})
        self.assertEqual(str(city.region), str(region))
        

    def test_has_subrace(self):
        """  """
        city = City(self.redis)
        self.assertEquals(False, city.has_subraces('foo'))
        self.assertEquals(True, city.has_subraces('kobold'))

    @patch('megacosm.generators.city.random')
    def test_want_subraces(self, mockrand):
        """  """
        city = City(self.redis)
        mockrand.randint.return_value = 1
        self.assertEquals(True, city.want_subraces('kobold'))
        mockrand.randint.return_value = 100
        self.assertEquals(False, city.want_subraces('kobold'))

    def test_calculate_population(self):
        """  """
        city = City(self.redis)
        city.population_estimate = None
        city.population_density = None

        city.calculate_population()
        self.assertLessEqual(city.population_estimate, int(city.size['maxpop']))
        self.assertGreaterEqual(city.population_estimate, int(city.size['minpop']))

        self.assertLessEqual(city.population_density, int(city.size['max_density']))
        self.assertGreaterEqual(city.population_density, int(city.size['min_density']))

    @patch('megacosm.generators.city.random')
    def test_calculate_racial_breakdown(self, mockrand):
        """  """
        city = City(self.redis)
        mockrand.randint.side_effect = [11, 30, 30, 30, 30]
        mockredis = Mock(self.redis)
        mockredis.lrange = MagicMock(return_value=['orc', 'ogre', 'molekin', 'human', 'harpy', 'halfling', 'elf'
                                                   'goblin', 'gnome', 'dwarf', 'coatikin', 'bugbear', 'catfolk'])
        city.redis = mockredis
        city.calculate_racial_breakdown()
        self.assertLess(0, len(city.races))
        self.assertDictEqual({'molekin': 29, 'other': 11, 'orc': 30, 'ogre': 30}, city.races)

    @patch('megacosm.generators.city.random')
    def test_calculate_racial_breakdown_lowrolls(self, mockrand):
        city = City(self.redis)
        mockrand.randint.side_effect = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        mockredis = Mock(self.redis)
        mockredis.lrange = MagicMock(return_value=['orc', 'ogre', 'molekin'])
        city.redis = mockredis
        city.calculate_racial_breakdown()
        self.assertLess(0, len(city.races))
        self.assertDictEqual({'molekin': 3, 'other': 94, 'orc': 1, 'ogre': 2}, city.races)

    @patch('megacosm.generators.city.random')
    def test_calculate_subraces(self, mockrand):
        city = City(self.redis)
        mockrand.randint.side_effect = [29, 2, 39, 4, 5, 6, 7, 8, 9]
        mockredis = Mock(self.redis)
        mockredis.lrange = MagicMock(return_value=['halfelf', 'wildelf', 'woodelf', 'darkelf'])
        city.redis = mockredis
        subraces = city.calculate_which_subraces('elf', 40)
        self.assertDictEqual({'halfelf': 29, 'wildelf': 2, 'woodelf': 9}, subraces)

    @patch('megacosm.generators.city.random')
    def test_calculate_subraces_lowrolls(self, mockrand):
        city = City(self.redis)
        mockrand.randint.side_effect = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        mockredis = Mock(self.redis)
        mockredis.lrange = MagicMock(return_value=['halfelf', 'wildelf', 'woodelf', 'darkelf'])
        city.redis = mockredis
        subraces = city.calculate_which_subraces('elf', 40)
        self.assertDictEqual({'halfelf': 34, 'darkelf': 3, 'wildelf': 1, 'woodelf': 2}, subraces)

    def test_select_subraces(self):
        """ verify subraces"""
        self.redis.lpush('npc_race','orc')
        self.redis.lpush('npc_race','elf')
        self.redis.set('elf_subrace_chance',101) 

        city = City(self.redis)
        city.races = {'orc': 3, 'elf':  {'shadowelf': 18, 'snowelf': 11, 'waterelf': 11}}
        city.select_subraces()
        self.assertDictEqual({'orc': 3, 'elf': {'shadowelf': 18, 'snowelf': 11, 'waterelf': 11} },
                             city.races)

    def test_select_no_subraces(self):
        """ verify subraces"""
        self.redis.lpush('npc_race','orc')
        self.redis.lpush('npc_race','elf')
        self.redis.set('elf_subrace_chance',101) 

        city = City(self.redis)
        city.races = {'orc': 3, 'elf':40}
        city.select_subraces()
        self.assertEqual(3,   city.races['orc'])
        self.assertNotEqual(40,   city.races['elf'])
        total=0
        for elfkey in city.races['elf'].keys():
            self.assertIn(elfkey, ['shadowelf','snowelf','waterelf'])
            self.assertLessEqual(city.races['elf'][elfkey], 40)
            total+=city.races['elf'][elfkey]
        """ Our total subraces should be equal to our original race percentage"""
        self.assertEqual(total, 40)

    @patch('megacosm.generators.city.random')
    def test_get_race_breakdown(self, mockrand):
        """ verify race breakdown"""
        city = City(self.redis)
        self.redis.lpush('npc_race','orc')
        self.redis.lpush('npc_race','elf')
        self.redis.set('elf_subrace_chance',101) 
        city.races = {'orc': 3, 'elf': {'shadowelf': 18, 'snowelf': 11, 'waterelf': 11}, 'other': 10}
        breakdown = city.get_race_breakdown()
        self.assertDictEqual({ 'Orc': 3, 'Shadow Elf': 18, 'Snow Elf': 11, 'Water Elf': 11, 'Other': 10},
                             breakdown)

    def test_get_scale(self):
        mockredis = Mock(self.redis)
        city = City(self.redis)
        citydata = [
            '{"maxpop": "100", "max_density": "400", "name": "settlement", "min_density": "10", "minpop": "25"}',
            '{"maxpop": "500", "max_density": "2000", "name": "hamlet", "min_density": "20", "minpop": "101"}',
            '{"maxpop": "600", "max_density": "2400", "name": "small village", "min_density": "30", "minpop": "501"}'
            ]

        mockredis.zrange = MagicMock(return_value=citydata)
        city.redis = mockredis
        scale = city.get_scale()
        self.assertEqual([{u'name': u'settlement'}, {u'name': u'hamlet'}, {u'name': u'small village'}], scale)
