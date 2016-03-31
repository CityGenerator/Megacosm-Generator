#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.lpush('weather_cloud', 'cumulus')
    self.redis.lpush('weather_storm', 'downburst')
    self.redis.lpush('weather_time', 'in the early evening')
    self.redis.lpush('weather_precipitation_type', 'sleeting')
    self.redis.zadd('weather_precipitation', '{ "name":"heavily",    "score":100     }', 100)
    self.redis.zadd('weather_temp', '{ "name":"unbearably hot",   "score":100     }', 100)
    self.redis.zadd('weather_wind', '{ "name":"hurricane-force",  "score":100     }', 100)

    self.redis.lpush('weather_template',
                     'Right now it is {{params.temp["name"]}} outside, with {{params.wind["name"]}} winds.'+
                     '{%if params.precipitation%} It is {{params.precipitation["name"] }} '+
                     '{{params.precipitation_type}} at the moment.{%endif%}{%if params.cloud%} There are '+
                     '{{ params.cloud }} clouds in the sky above.{%endif%}{%if params.storm%} {{ params.storm '+
                     '|article |capitalize}} is approaching, and will hit {{params.time}}.{%endif%}')
