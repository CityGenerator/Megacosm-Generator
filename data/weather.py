# Right now it is ___________,
ZADD weather_temp  10  { "name":"unbearably cold",  "score":10      }
ZADD weather_temp  20  { "name":"freezing",         "score":20      }
ZADD weather_temp  30  { "name":"cold",             "score":30      }
ZADD weather_temp  40  { "name":"chilly",           "score":40      }
ZADD weather_temp  50  { "name":"cool",             "score":50      }
ZADD weather_temp  60  { "name":"mild",             "score":60      }
ZADD weather_temp  70  { "name":"pleasant",         "score":70      }
ZADD weather_temp  80  { "name":"warm",             "score":80      }
ZADD weather_temp  90  { "name":"hot",              "score":90      }
ZADD weather_temp 100  { "name":"unbearably hot",   "score":100     }

# Right now it is mild, with ______ winds.
ZADD weather_wind  10  { "name":"calm",             "score":10      }
ZADD weather_wind  20  { "name":"light",            "score":20      }
ZADD weather_wind  30  { "name":"gentle",           "score":30      }
ZADD weather_wind  40  { "name":"breezy",           "score":40      }
ZADD weather_wind  50  { "name":"moderate",         "score":50      }
ZADD weather_wind  60  { "name":"fresh",            "score":60      }
ZADD weather_wind  70  { "name":"strong",           "score":70      }
ZADD weather_wind  80  { "name":"gale-force",       "score":80      }
ZADD weather_wind  90  { "name":"storm-force",      "score":90      }
ZADD weather_wind 100  { "name":"hurricane-force",  "score":100     }

# it is ____ drizzling at the moment.
SET  weather_precipitation_chance 20
ZADD weather_precipitation  20  { "name":"lightly",    "score":20      }
ZADD weather_precipitation  60  { "name":"moderately", "score":60      }
ZADD weather_precipitation  90  { "name":"densely",    "score":90      }
ZADD weather_precipitation 100  { "name":"heavily",    "score":100     }

# It is heavily ______ at the moment.
self.redis.lpush('weather_precipitation_type', 'drizzling')
self.redis.lpush('weather_precipitation_type', 'raining')
self.redis.lpush('weather_precipitation_type', 'freeze-drizzling')
self.redis.lpush('weather_precipitation_type', 'freeze-raining')
self.redis.lpush('weather_precipitation_type', 'snowing')
self.redis.lpush('weather_precipitation_type', 'sleeting')
self.redis.lpush('weather_precipitation_type', 'hailing')
self.redis.lpush('weather_precipitation_type', 'graupeling')

# There are ______ clouds in the sky above
SET   weather_cloud_chance 30

self.redis.lpush('weather_cloud', 'cirrus')
self.redis.lpush('weather_cloud', 'cirrostratus')
self.redis.lpush('weather_cloud', 'cirrocumulus')
self.redis.lpush('weather_cloud', 'altostratus')
self.redis.lpush('weather_cloud', 'altocumulus')
self.redis.lpush('weather_cloud', 'stratus')
self.redis.lpush('weather_cloud', 'stratocumulus')
self.redis.lpush('weather_cloud', 'nimbostratus')
self.redis.lpush('weather_cloud', 'cumulus')
self.redis.lpush('weather_cloud', 'cumulus congestus')
self.redis.lpush('weather_cloud', 'cumulonimbus')
self.redis.lpush('weather_cloud', 'wall')
self.redis.lpush('weather_cloud', 'shelf')
self.redis.lpush('weather_cloud', 'fractus')
self.redis.lpush('weather_cloud', 'mammatus')
self.redis.lpush('weather_cloud', 'contrail')




# A __________ is approaching,
SET   weather_storm_chance 30
self.redis.lpush('weather_storm', 'ice storm')
self.redis.lpush('weather_storm', 'blizzard')
self.redis.lpush('weather_storm', 'snow storm')
self.redis.lpush('weather_storm', 'wind storm')
self.redis.lpush('weather_storm', 'gale')
self.redis.lpush('weather_storm', 'thunderstorm')
self.redis.lpush('weather_storm', 'cyclone')
self.redis.lpush('weather_storm', 'hailstorm')
self.redis.lpush('weather_storm', 'downburst')
self.redis.lpush('weather_storm', 'dust storm')
self.redis.lpush('weather_storm', 'hurricane')
self.redis.lpush('weather_storm', 'lightning storm')
self.redis.lpush('weather_storm', 'thunder snow storm')
self.redis.lpush('weather_storm', 'thunderstorm')
self.redis.lpush('weather_storm', 'tropical storm')
self.redis.lpush('weather_storm', 'winter storm')

# and will hit at ________

self.redis.lpush('weather_time', 'at daybreak')
self.redis.lpush('weather_time', 'mid-morning')
self.redis.lpush('weather_time', 'around noon')
self.redis.lpush('weather_time', 'in the afternoon')
self.redis.lpush('weather_time', 'mid-day')
self.redis.lpush('weather_time', 'in the early evening')
self.redis.lpush('weather_time', 'before nightfall')
self.redis.lpush('weather_time', 'after nightfall')
self.redis.lpush('weather_time', 'at midnight')
self.redis.lpush('weather_time', 'in the dead of night')
self.redis.lpush('weather_time', 'before dawn')


self.redis.lpush('weather_template', 'Right now it is {{params.temp["name"]}} outside, with {{params.wind["name"]}} winds.{%if params.precipitation%} It is {{params.precipitation["name"] }} {{params.precipitation_type}} at the moment.{%endif%}{%if params.cloud%} There are {{ params.cloud }} clouds in the sky above.{%endif%}{%if params.storm%} {{ params.storm |article |capitalize}} is approaching, and will hit {{params.time}}.{%endif%}')
