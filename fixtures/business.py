#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.lpush('bus_adventurersguild_manager', 'adventurer')
    self.redis.lpush('bus_adventurersguild_trailer', 'hall')
    self.redis.lpush('business_condition', 'cluttered')
    self.redis.lpush('business_direction', 'west')
    self.redis.lpush('business_kind', 'bus_adventurersguild')
    self.redis.lpush('businessname_formalname_template', '{{params.adjective}} {{params.noun}} {{params.trailer}}')
    self.redis.lpush('businessname_fullname_template', '{{params.adjective}} {{params.noun}} {{params.trailer}}')
    self.redis.lpush('businessname_shortname_template', '{{params.adjective}} {{params.noun}}')
    self.redis.lpush('business_rooftype', 'slate')
    self.redis.lpush('business_shade', 'bright')
    self.redis.lpush('business_storefront', 'mud')
    self.redis.lpush('business_trouble', 'slumping sales')
    self.redis.lpush('business_windows', 'clean')
    self.redis.lpush('businessname_adjective', 'Angry')
    self.redis.lpush('businessname_noun', 'Axe')
    self.redis.set('bus_adventurersguild_district', 'professional')
    self.redis.set('bus_adventurersguild_kindname', 'adventurers guild')
    self.redis.set('bus_adventurersguild_maxfloors', '2')
    self.redis.set('bus_adventurersguild_perbuilding', '30')
    self.redis.zadd('business_age', {'{  "name":"old"          , "score":100  }': 100})
    self.redis.zadd('business_neighborhood', {'{ "name":"expensive",    "score":100 }': 100})
    self.redis.zadd('business_neighborhood', {'{ "name":"new",          "score":100  }': 100})
    self.redis.zadd('business_popularity', {'{  "name":"is constantly crowded"            , "score":100 }': 100})
    self.redis.zadd('business_price', {'{  "name":"very high"          , "score":100  }': 100})
    self.redis.zadd('business_reputation', {'{  "name":"being a pillar of the community"  , "score":100 }': 100})
    self.redis.zadd('business_size', {'{  "name":"vast"           , "score":100 }': 100})
    self.redis.zadd('business_status', {'{  "name":"booming",            "score":100 }': 100})
