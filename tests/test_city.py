#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import City, Region
import unittest2 as unittest
from mock import Mock, patch, MagicMock
import redis
from config import TestConfiguration


class TestCity(unittest.TestCase):

    def setUp(self):
        """  """
        # TODO see if testconfiguration can put a prefix on redis keys to prevent overlap
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)
        self.city = City(self.redis)

    def Teardown(self):
        """  """
        self.city = None

    def test_random_city(self):
        """  """
        self.assertNotEqual('', self.city.name)
        self.assertEquals(self.city.name['full'], "%s" % self.city)

    def test_city_region(self):
        """  """
        city = City(self.redis, {'region': Mock(Region)})
        self.assertNotEqual('', city.name)

    def test_has_subrace(self):
        """  """
        self.assertEquals(False, self.city.has_subraces('foo'))
        self.assertEquals(True, self.city.has_subraces('elf'))

    @patch('megacosm.generators.city.random')
    def test_want_subraces(self, mockrand):
        """  """
        mockrand.randint.return_value = 1
        self.assertEquals(True, self.city.want_subraces('elf'))
        mockrand.randint.return_value = 100
        self.assertEquals(False, self.city.want_subraces('elf'))

    def test_calculate_population(self):
        """  """
        self.city.population_estimate = None
        self.city.population_density = None
        self.city.size = {'minpop': 99, 'maxpop': 100, 'min_density': 50, 'max_density': 51}

        self.city.calculate_population()
        self.assertLessEqual(self.city.population_estimate, self.city.size['maxpop'])
        self.assertGreaterEqual(self.city.population_estimate, self.city.size['minpop'])

        self.assertLessEqual(self.city.population_density, self.city.size['max_density'])
        self.assertGreaterEqual(self.city.population_density, self.city.size['min_density'])

    @patch('megacosm.generators.city.random')
    def test_calculate_racial_breakdown(self, mockrand):
        """  """
        mockrand.randint.side_effect = [11, 30, 30, 30, 30]
        mockredis = Mock(redis)
        mockredis.lrange = MagicMock(return_value=['orc', 'ogre', 'molekin', 'human', 'harpy', 'halfling', 'elf'
                                                   'goblin', 'gnome', 'dwarf', 'coatikin', 'bugbear', 'catfolk'])
        self.city.redis = mockredis
        self.city.calculate_racial_breakdown()
        self.assertLess(0, len(self.city.races))
        self.assertDictEqual({'molekin': 29, 'other': 11, 'orc': 30, 'ogre': 30}, self.city.races)

    @patch('megacosm.generators.city.random')
    def test_calculate_racial_breakdown_lowrolls(self, mockrand):
        mockrand.randint.side_effect = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        mockredis = Mock(redis)
        mockredis.lrange = MagicMock(return_value=['orc', 'ogre', 'molekin'])
        self.city.redis = mockredis
        self.city.calculate_racial_breakdown()
        self.assertLess(0, len(self.city.races))
        self.assertDictEqual({'molekin': 3, 'other': 94, 'orc': 1, 'ogre': 2}, self.city.races)

    @patch('megacosm.generators.city.random')
    def test_calculate_subraces(self, mockrand):
        mockrand.randint.side_effect = [29, 2, 39, 4, 5, 6, 7, 8, 9]
        mockredis = Mock(redis)
        mockredis.lrange = MagicMock(return_value=['halfelf', 'wildelf', 'woodelf', 'darkelf'])
        self.city.redis = mockredis
        subraces = self.city.calculate_which_subraces('elf', 40)
        self.assertDictEqual({'halfelf': 29, 'wildelf': 2, 'woodelf': 9}, subraces)

    @patch('megacosm.generators.city.random')
    def test_calculate_subraces_lowrolls(self, mockrand):
        mockrand.randint.side_effect = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        mockredis = Mock(redis)
        mockredis.lrange = MagicMock(return_value=['halfelf', 'wildelf', 'woodelf', 'darkelf'])
        self.city.redis = mockredis
        subraces = self.city.calculate_which_subraces('elf', 40)
        self.assertDictEqual({'halfelf': 34, 'darkelf': 3, 'wildelf': 1, 'woodelf': 2}, subraces)

    @patch('megacosm.generators.city.random')
    def test_select_subraces(self, mockrand):
        """ verify """
        mockrand.randint.side_effect = [100, 100, 100, 100, 100, 100, 100, 1, 11, 11, 100, 100, 100, 100]
        self.city.races = {'orc': 3, 'elf': 40, 'molekin': 3, 'human': 23, 'harpy': 3, 'halfling': 3,
                           'goblin': 3, 'gnome': 3, 'ogre': 3, 'dwarf': 3, 'catfolk': 3, 'other': 10}
        self.city.select_subraces()
        self.assertDictEqual({'orc': 3, 'ogre': 3, 'molekin': 3, 'human': 23, 'harpy': 3, 'halfling': 3,
                              'goblin': 3, 'gnome': 3, 'elf': {'shadowelf': 18, 'snowelf': 11, 'waterelf': 11},
                              'dwarf': 3, 'catfolk': 3, 'other': 10},
                             self.city.races)

    @patch('megacosm.generators.city.random')
    def test_get_race_breakdown(self, mockrand):
        """ verify """
        self.city.races = {'orc': 3, 'ogre': 3, 'molekin': 3, 'human': 23, 'harpy': 3, 'halfling': 3,
                           'goblin': 3, 'gnome': 3, 'elf': {'shadowelf': 18, 'snowelf': 11, 'waterelf': 11},
                           'dwarf': 3, 'catfolk': 3, 'other': 10}
        breakdown = self.city.get_race_breakdown()
        self.assertDictEqual({'Catfolk': 3, 'Dwarf': 3, 'Gnome': 3, 'Goblin': 3, 'Halfling': 3, 'Harpy': 3,
                              'Human': 23, 'Molekin': 3, 'Ogre': 3, 'Orc': 3, 'Shadow Elf': 18, 'Snow Elf': 11,
                              'Water Elf': 11, 'Other': 10},
                             breakdown)

    def test_get_scale(self):
        mockredis = Mock(redis)
        citydata = [
            '{"maxpop": "100", "max_density": "400", "name": "settlement", "min_density": "10", "minpop": "25"}',
            '{"maxpop": "500", "max_density": "2000", "name": "hamlet", "min_density": "20", "minpop": "101"}',
            '{"maxpop": "600", "max_density": "2400", "name": "small village", "min_density": "30", "minpop": "501"}'
            ]

        mockredis.zrange = MagicMock(return_value=citydata)
        self.city.redis = mockredis
        scale = self.city.get_scale()
        self.assertEqual([{u'name': u'settlement'}, {u'name': u'hamlet'}, {u'name': u'small village'}], scale)
