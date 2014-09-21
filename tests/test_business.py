#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Business, NPC
import unittest2 as unittest
import redis
from mock import Mock
from config import TestConfiguration
import json


class TestBusiness(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_business(self):
        """  """
        business = Business(self.redis)
        self.assertNotEqual('', business.name)
        self.assertNotEqual('', "%s" % business)

    def test_senses(self):
        """  """
        business = Business(self.redis, {'smell': 'stank', 'sight': 'ugly blinds', 'sound': 'cries for help'})
        self.assertNotEqual('', "%s" % business)

    def test_business_params(self):
        """  """
        dummyuser = Mock(NPC)
        business = Business(self.redis,
                            {'owner': dummyuser, 'patroncount': 3, 'trailer': 'a place', 'maxfloors': 2, 'floor': 1})
        self.assertNotEqual('', "%s" % business)

    def test_business_data(self):

        stats = ['status', 'size', 'popularity', 'reputation', 'price', 'age', 'neighborhood']
        for stat in stats:
            results = self.redis.zrangebyscore('business_'+stat, 0, 100, withscores=True)
            for (result, score) in results:
                resultobj = json.loads(result)
                self.assertEquals(score, resultobj['score'])
