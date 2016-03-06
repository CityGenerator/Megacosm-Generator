#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Resource, Region
import unittest2 as unittest

import fakeredis
from config import TestConfiguration


class TestResource(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()
        self.redis.zadd('resource_competition', '{  "name":"fierce",             "score":100      }', 100)
        self.redis.zadd('resource_depletion', '{  "name":"bountiful",           "score":100      }', 100)
        self.redis.zadd('resource_exportregion', '{  "name":"across the continent",           "score":100      }', 100)
        self.redis.zadd('resource_management', '{  "name":"well",           "score":100      }', 100)
        self.redis.zadd('resource_ubiquity', '{  "name":"not specific",       "score":100       }', 100)
        self.redis.zadd('resource_utility', '{  "name":"useful",          "score":100      }', 100)
        self.redis.zadd('resource_value', '{  "name":"valuable",          "score":100      }', 100)
        self.redis.lpush('naturalresource_crop_name', 'crop')
        self.redis.lpush('naturalresource_crop_name_type', 'wild')
        self.redis.lpush('naturalresource_crop_product', 'cocoa beans')
        self.redis.lpush('naturalresource_kind', 'crop')
        self.redis.lpush('resource_kind', 'naturalresource')
        self.redis.lpush('resource_template', '"{{params.place.name["full"]}} is known for its {{params.name_type}} {{params.name}} which {{params.method}} {{params.product}}. This resource is {{params.ubiquity["name"]}} to the region. Many consider the {{params.product}} {{params.utility["name"]}}, and are regardless seen as a {{params.value["name"]}} resource. Competition in the {{params.product}} market is {{params.competition["name"]}}, and the {{params.name}} resource as a whole are {{params.management["name"]}} managed."')

    def tearDown(self):
        self.redis.flushall()

    def test_random_resource(self):
        """  """
        resource = Resource(self.redis)
        self.assertNotEquals('', resource.text)

    def test_static_text(self):
        """  """
        resource = Resource(self.redis,{'text':'You are a loser.'})
        self.assertEquals('You are a loser.', str(resource))

    def test_static_region(self):
        """  """
        region=Region(self.redis)
        resource = Resource(self.redis,{'place':region})
        self.assertEquals(str(region), str(region))
