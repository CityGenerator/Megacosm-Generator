# Right now it is ___________,
self.redis.zadd('weather_temp', '{ "name":"unbearably cold",  "score":10      }', '10')
self.redis.zadd('weather_temp', '{ "name":"freezing",         "score":20      }', '20')
self.redis.zadd('weather_temp', '{ "name":"cold",             "score":30      }', '30')
self.redis.zadd('weather_temp', '{ "name":"chilly",           "score":40      }', '40')
self.redis.zadd('weather_temp', '{ "name":"cool",             "score":50      }', '50')
self.redis.zadd('weather_temp', '{ "name":"mild",             "score":60      }', '60')
self.redis.zadd('weather_temp', '{ "name":"pleasant",         "score":70      }', '70')
self.redis.zadd('weather_temp', '{ "name":"warm",             "score":80      }', '80')
self.redis.zadd('weather_temp', '{ "name":"hot",              "score":90      }', '90')
self.redis.zadd('weather_temp', '{ "name":"unbearably hot",   "score":100     }', '100')

# Right now it is mild, with ______ winds.
self.redis.zadd('weather_wind', '{ "name":"calm",             "score":10      }', '10')
self.redis.zadd('weather_wind', '{ "name":"light",            "score":20      }', '20')
self.redis.zadd('weather_wind', '{ "name":"gentle",           "score":30      }', '30')
self.redis.zadd('weather_wind', '{ "name":"breezy",           "score":40      }', '40')
self.redis.zadd('weather_wind', '{ "name":"moderate",         "score":50      }', '50')
self.redis.zadd('weather_wind', '{ "name":"fresh",            "score":60      }', '60')
self.redis.zadd('weather_wind', '{ "name":"strong",           "score":70      }', '70')
self.redis.zadd('weather_wind', '{ "name":"gale-force",       "score":80      }', '80')
self.redis.zadd('weather_wind', '{ "name":"storm-force",      "score":90      }', '90')
self.redis.zadd('weather_wind', '{ "name":"hurricane-force",  "score":100     }', '100')

# it is ____ drizzling at the moment.
SET  weather_precipitation_chance 20
self.redis.zadd('weather_precipitation', '{ "name":"lightly",    "score":20      }', '20')
self.redis.zadd('weather_precipitation', '{ "name":"moderately", "score":60      }', '60')
self.redis.zadd('weather_precipitation', '{ "name":"densely",    "score":90      }', '90')
self.redis.zadd('weather_precipitation', '{ "name":"heavily",    "score":100     }', '100')

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
