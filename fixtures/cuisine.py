#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""

    self.redis.lpush('cuisine_dish', 'dog')
    self.redis.lpush('cuisine_flavor', 'orange')
    self.redis.lpush('cuisine_mealtype', 'salad')
    self.redis.lpush('cuisine_method', 'scalded')
    self.redis.lpush('cuisine_sauce', 'chile')
    self.redis.lpush('cuisine_saucetype', 'gravy')
    self.redis.lpush('cuisine_served', 'luke warm')
    self.redis.lpush('cuisine_template',
                     '{%if params.method%}{{params.method}} {%endif%}{%if params.flavor%}{{params.flavor}} '+
                     '{%endif%}{{params.dish}}{%if params.mealtype%} {{params.mealtype}}{%endif%}'+
                     '{%if params.sauce%} in {{params.sauce}} {{params.saucetype}}{%endif%}{%if params.served%}, '+
                     'served {{params.served}}{%endif%} This dish is {{params.rarity["name"]}} to the '+
                     '{{params.region.name["full"]}}. Travelers consider the dish {{params.spice["name"]}} and '+
                     '{{params.presentation["name"]}} to the eye. Portions are usually {{params.size["name"]}}.')
    self.redis.zadd('cuisine_presentation', '{"name":"beautiful",      "score":100  }', 100)
    self.redis.zadd('cuisine_rarity', '{"name":"unique",      "score":100  }', 100)
    self.redis.zadd('cuisine_size', '{"name":"large",          "score":100   }', 100)
    self.redis.zadd('cuisine_spice', '{"name":"spicy",     "score":100  }', 100)
