#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.hset('govtcountry_govttype_description', 'absolutemonarchy',
                    '{ "name":"absolute monarchy",      "description":"the monarch rules unhindered"  }')
    self.redis.hset('govtcountry_govttype_description', 'authoritarian',
                    '{ "name":"authoritarian government",     "description":"state authority is imposed onto many '+
                    'aspects of citizens\' lives"  }')
    self.redis.hset('govtcountry_govttype_description', 'commonwealth',
                    '{ "name":"commonwealth", "description":"state authority is founded on law and united by a '+
                    'compact of the people for the common good"  }')
    self.redis.hset('govtcountry_govttype_description', 'communist',
                    '{ "name":"communist government",   "description":"the state plans and controls the economy and '+
                    'a single party holds power"  }')
    self.redis.hset('govtcountry_govttype_description', 'constitutional',
                    '{ "name":"constitutional government",    "description":"an authoritative document sets forth '+
                    'the system of fundamental laws and limits of that government"  }')
    self.redis.hset('govtcountry_govttype_description', 'democracy',
                    '{ "name":"democracy", "description":"the supreme power is retained by the people, but is '+
                    'exercised through a system of representation"  }')
    self.redis.hset('govtcountry_govttype_description', 'dictatorship',
                    '{ "name":"dictatorship",           "description":"the ruler or small clique wield absolute power'+
                    ' (not restricted by a constitution or laws)"  }')
    self.redis.hset('govtcountry_govttype_description', 'ecclesiastical',
                    '{ "name":"ecclesiastical government", "description":"the government administrated by a church."}')
    self.redis.hset('govtcountry_govttype_description', 'emirate',
                    '{ "name":"emirate",                "description":"the supreme power is in the hands of an emir, '+
                    'who may be an absolute overlord with constitutionally limited authority"  }')
    self.redis.hset('govtcountry_govttype_description', 'federation',
                    '{ "name":"federation",             "description":"sovereign power is formally divided between a '+
                    'central authority and a number of constituent regions"  }')
    self.redis.hset('govtcountry_govttype_description', 'monarchy',
                    '{ "name":"monarchy",               "description":"the supreme power is lodged in the hands of a '+
                    'monarch who reigns with constitutionally limited authority"  }')
    self.redis.hset('govtcountry_govttype_description', 'oligarchy',
                    '{ "name":"oligarchy",              "description":"control is exercised by a small group of '+
                    'individuals whose authority generally is based on wealth or power"  }')
    self.redis.hset('govtcountry_govttype_description', 'parliamentary',
                    '{ "name":"parliamentary government",     "description":"members are nominated to their '+
                    'positions by a parliament and can be dissolved by the parliament if it can no longer function" }')
    self.redis.hset('govtcountry_govttype_description', 'republic',
                    '{ "name":"republic",             "description":"the people\'s elected representatives, not the '+
                    'people themselves, vote on legislation."  }')
    self.redis.hset('govtcountry_govttype_description', 'theocracy',
                    '{ "name":"theocracy",          "description":"a deity is recognized as the supreme civil ruler, '+
                    'but the deity\'s laws are interpreted by ecclesiastical authorities"  }')
    self.redis.hset('govtcountry_govttype_description', 'totalitarian',
                    '{ "name":"totalitarian government", "description":"the government subordinates individuals by '+
                    'controlling all political and economic matters, as well as the attitudes, values, and beliefs" }')

    self.redis.lpush('govtcountry_govttype', 'absolutemonarchy')
    self.redis.lpush('govt_kind', 'country')
    self.redis.zadd('govt_age', '{ "name":"far longer than should be allowed", "score":100   }', 100)
    self.redis.zadd('govt_approval', '{ "name":"revered",                   "score":100      }', 100)
    self.redis.zadd('govt_corruption', '{ "name":"incorruptible",           "score":100      }', 100)
    self.redis.zadd('govt_efficiency', '{ "name":"ruthlessly effective",    "score":100      }', 100)
    self.redis.zadd('govt_influence', '{ "name":"thriving",                 "score":100      }', 100)
    self.redis.zadd('govt_opposition', '{ "name":"violent",                 "score":100      }', 100)
    self.redis.zadd('govt_reputation', '{ "name":"revered",                 "score":100      }', 100)
    self.redis.zadd('govt_theology', '{ "name":"is used to control the populace", "score":100       }', 100)
    self.redis.zadd('govt_unity', '{ "name":"rallies behind its leaders",         "score":100       }', 100)

