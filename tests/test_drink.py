#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators.Drink import Drink
import unittest
import fixtures
import fakeredis
from config import TestConfiguration

class TestDrink(unittest.TestCase):

    def setUp(self):
        """ Set up the required fixtures """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        fixtures.drink.import_fixtures(self)
        fixtures.npc.import_fixtures(self)
        fixtures.region.import_fixtures(self)
        fixtures.leader.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        self.redis.lpush('npc_race','gnome')

    def tearDown(self):
        self.redis.flushall()

    def test_random_drink(self):
        """ """
        drink = Drink(self.redis)
        print(drink.text)
        self.assertEqual('You sip an amber broth that is unique to New Lombardy. It has a overpowering flavor of spice, and feels sticky on the tongue.', drink.text)
    def test_drink_template(self):
        """ """
        drink = Drink(self.redis, {
            'type' : 'ale',
            'flavor' : 'sour',
            'template' :  'template {{params.flavor}} {{params.type}}'
        })

        self.assertEqual('Template sour ale', drink.text)
        self.assertEqual('Template sour ale', "%s" % drink)


    def test_drink_text(self):
        """  """
        drink = Drink(self.redis, {
            'text': 'something'
            })

        self.assertEqual('Something', drink.text)
        self.assertEqual('Something', "%s" % drink)

