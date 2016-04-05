#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""

    self.redis.hset('deity_primarycolor_description', 'aquamarine', '{"name":"aquamarine", "hex":"7FFFD4" }')
    self.redis.hset('deity_secondarycolor_description', 'aquamarine', '{"name":"aquamarine", "hex":"7FFFD4" }')
    self.redis.hset('deity_vow_description', 'humility',
                    '{"name":"Humility",         "description":"abstain from extolling your own virtues"}')
    self.redis.hset('govtcountry_govttype_description', 'theocracy',
                    '{ "name":"theocracy", "description":"a deity is recognized as the supreme civil ruler, but the '+
                    'deity\'s laws are interpreted by ecclesiastical authorities"  }')
    self.redis.lpush('deity_favored_stat', 'piety')
    self.redis.lpush('deity_favored_stat', 'skill')
    self.redis.lpush('deity_favored_weapon', 'bows')
    self.redis.lpush('deity_form', 'talking jackal')
    self.redis.lpush('deity_holysymbol', 'axe')
    self.redis.lpush('deity_holysymbol_type', 'rocking')
    self.redis.lpush('deity_primarycolor', 'aquamarine')
    self.redis.lpush('deity_secondarycolor', 'aquamarine')
    self.redis.lpush('deity_vow', 'humility')
    self.redis.lpush('deity_worship', 'supplication')
    self.redis.lpush('portfolio_level', 1)
    self.redis.lpush('portfolio_level', 16)
    self.redis.lpush('portfolio_level', 2)
    self.redis.lpush('portfolio_level', 3)
    self.redis.lpush('portfolio_level', 4)
    self.redis.zadd('deity_age', '{"name":"original",  "score":100   }', 100)
    self.redis.zadd('deity_followercount', '{"name":"countless",  "score":100   }', 100)
    self.redis.zadd('deity_followerzeal', '{"name":"overzealous",  "score":100   }', 100)
    self.redis.zadd('deity_health', '{"name":"more popular than ever",     "score":100 }', 100)
    self.redis.zadd('deity_importance', '{"name":"over deity",          "score":100, "points":21 }', 100)
    self.redis.zadd('deity_importance', '{"name":"over deity",          "score":100, "points":21 }', 100)
    self.redis.zadd('deity_jealousy', '{"name":"jealous",  "score":100   }', 100)
    self.redis.zadd('deity_organized', '{"name":"rigidly",         "score":100 }', 100)
    self.redis.zadd('deity_secrecy', '{"name":"pompous",       "score":100   }', 100)
    self.redis.zadd('deity_unity', '{"name":"unified",     "score":100 }', 100)
    self.redis.zadd('portfolio_domain', '{"name":"adventure",                       "score":1 }', 1)
    self.redis.zadd('portfolio_domain', '{"name":"cold",                       "score":4 }', 4)
    self.redis.zadd('portfolio_domain', '{"name":"good",                       "score":16 }', 16)
    self.redis.zadd('portfolio_domain', '{"name":"song",                       "score":2 }', 2)
    self.redis.zadd('portfolio_domain', '{"name":"zeal",                       "score":3 }', 3)
