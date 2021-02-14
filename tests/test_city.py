#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators import City, Region
import unittest2 as unittest
from mock import Mock, patch, MagicMock
import fakeredis
from config import TestConfiguration
import fixtures

class TestCity(unittest.TestCase):

    def setUp(self):
        """ Set up the required fixtures """
        """  """
        # TODO see if testconfiguration can put a prefix on redis keys to prevent overlap
        self.redis = fakeredis.FakeRedis()
        fixtures.business.import_fixtures(self)
        fixtures.npc.import_fixtures(self)
        fixtures.region.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.city.import_fixtures(self)
        fixtures.organization.import_fixtures(self)
        fixtures.leader.import_fixtures(self)
        fixtures.country.import_fixtures(self)



    def tearDown(self):
        """ Clean up any changes from the last run. """
        """  """
        self.redis.flushall()

    def test_random_city(self):
        """  """
        self.redis.lpush('npc_race','gnome')
        city = City(self.redis)
        self.assertEqual('Alta DeAllentle Gate', city.name.fullname)
        self.assertEquals(city.name.fullname, str(city))

    def test_city_region(self):
        """  """
        self.redis.lpush('npc_race','gnome')
        region=Region(self.redis)
        city = City(self.redis, {'region': region})
        self.assertEqual(str(city.region), str(region))
        

    def test_has_subrace(self):
        """  """
        self.redis.lpush('npc_race','kobold')
        city = City(self.redis)
        self.assertEquals(False, city.has_subraces('foo'))
        self.assertEquals(True, city.has_subraces('kobold'))

    @patch('megacosm.generators.city.random')
    def test_want_subraces(self, mockrand):
        """  """
        self.redis.lpush('npc_race','kobold')
        city = City(self.redis)
        mockrand.randint.return_value = 1
        self.assertEquals(True, city.want_subraces('kobold'))
        mockrand.randint.return_value = 100
        self.assertEquals(False, city.want_subraces('kobold'))

    def test_calculate_population(self):
        """  """
        self.redis.lpush('npc_race','gnome')
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
        self.redis.lpush('npc_race','gnome')
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
        self.redis.lpush('npc_race','gnome')
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
        self.redis.lpush('npc_race','gnome')
        city = City(self.redis)
        mockrand.randint.side_effect = [29, 2, 39, 4, 5, 6, 7, 8, 9]
        mockredis = Mock(self.redis)
        mockredis.lrange = MagicMock(return_value=['halfelf', 'wildelf', 'woodelf', 'darkelf'])
        city.redis = mockredis
        subraces = city.calculate_which_subraces('elf', 40)
        self.assertDictEqual({'halfelf': 29, 'wildelf': 2, 'woodelf': 9}, subraces)

    @patch('megacosm.generators.city.random')
    def test_calculate_subraces_lowrolls(self, mockrand):
        self.redis.lpush('npc_race','gnome')
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
        self.redis.lpush('npc_race','gnome')
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
        self.redis.lpush('npc_race','gnome')
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
