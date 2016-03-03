#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Currency
import unittest2 as unittest

import fakeredis
from config import TestConfiguration


class TestCurrency(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis=fakeredis.FakeRedis()
        self.redis.zadd('currency_amount','{ "name":"a large pile of",    "min":100,  "max":3000, "score":100 }',100)
        self.redis.zadd('currency_size','{ "name":"giant (40mm )"    , "score":100 }',100)
        self.redis.zadd('currency_value','{ "name":"priceless",         "score":100  }',100)
        self.redis.zadd('currency_scope','{ "name":"continent",   "score":100  }',100)
        self.redis.zadd('currency_detail','{ "name":"unmistakable" , "score":100  }',100)
        self.redis.zadd('currency_weight','{ "name":"hefty" , "score":100  }',100)
        self.redis.lpush('currency_material','wood')
        self.redis.lpush('currency_shape','square')
        self.redis.lpush('currency_edges','ridges')
        self.redis.lpush('currency_front',"man's face")
        self.redis.lpush('currency_back','dragon')
        self.redis.lpush( 'currency_template', "{{params.name['full']|article|title}} is {{params.weight['name'] | article}}, {{params.value['name']}} coin that is common in the {{params.scope['name']}}. It is {{params.size['name']}}, {{params.shape}}, and made of {{params.material}}. The coins are covered with {{params.detail['name']}} designs.")


        self.redis.lpush('name_currencypre','yua')
        self.redis.lpush('name_currencyroot','fel')
        self.redis.lpush('name_currencypost','abbi')

    def tearDown(self):
        self.redis.flushall()

    def test_random_currency(self):
        """  """
        currency = Currency(self.redis)
        self.assertEqual('yuafelabbi', currency.name['full'])
        self.assertEqual('A Yuafelabbi is a hefty, priceless coin that is common in the continent. It is giant (40mm ), square, and made of wood. The coins are covered with unmistakable designs.', str(currency))
    def test_static_values(self):
        """  """
        currency = Currency(self.redis, {'count':3,'text':'a yuafael'})
        self.assertEqual('yuafelabbi', currency.name['full'])
        self.assertEqual('A yuafael', str(currency))
