#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators.Currency import Currency
import unittest2 as unittest

import fakeredis
import fixtures
from config import TestConfiguration


class TestCurrency(unittest.TestCase):

    def setUp(self):
        """ Set up the required fixtures """
        self.redis=fakeredis.FakeRedis(decode_responses=True)
        fixtures.currency.import_fixtures(self)

    def tearDown(self):
        """ Clean up any changes from the last run. """
        self.redis.flushall()

    def test_random_currency(self):
        """  """
        currency = Currency(self.redis)
        self.assertEqual('yuafelabbi', currency.name.fullname)
        self.assertEqual('A Yuafelabbi is a hefty, priceless coin that is common in the continent. It is giant (40mm ), square, and made of wood. The coins are covered with unmistakable designs.', str(currency))
    def test_static_values(self):
        """  """
        currency = Currency(self.redis, {'count':3,'text':'a yuafael'})
        self.assertEqual('yuafelabbi', currency.name.fullname)
        self.assertEqual('A yuafael', str(currency))

