#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Govt, Country, City
import unittest2 as unittest

import fakeredis
from config import TestConfiguration


class TestGovt(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis()

        self.redis.zadd('govt_age', '{ "name":"far longer than should be allowed",      "score":100      }', 100)
        self.redis.zadd('govt_reputation', '{ "name":"revered",                         "score":100      }', 100)
        self.redis.zadd('govt_opposition', '{ "name":"violent",                         "score":100      }', 100)
        self.redis.zadd('govt_corruption', '{ "name":"incorruptible",                   "score":100      }', 100)
        self.redis.zadd('govt_approval', '{ "name":"revered",                           "score":100      }', 100)
        self.redis.zadd('govt_efficiency', '{ "name":"ruthlessly effective",            "score":100      }', 100)
        self.redis.zadd('govt_influence', '{ "name":"thriving",                         "score":100      }', 100)
        self.redis.zadd('govt_unity', '{ "name":"rallies behind its leaders",           "score":100      }', 100)
        self.redis.zadd('govt_theology', '{ "name":"is used to control the populace",   "score":100      }', 100)
        self.redis.lpush('govt_kind', 'country')
        self.redis.hset('govtcountry_govttype_description', 'absolutemonarchy', '{ "name":"absolute monarchy",            "description":"the monarch rules unhindered"  }')
        self.redis.lpush('govtcountry_govttype', 'absolutemonarchy')
        self.redis.lpush('govt_influencereason', 'food shortages in the region')
        self.redis.zadd('country_regiondetails', '{"name":"over a dozen",       "score":100, "mincount":12,  "maxcount":36  }', 100)
        self.redis.lpush('govt_kind', 'city')
        self.redis.hset('govtcity_govttype_description', 'councilmanager', '{ "name":"council/manager", "description":"things are run by a council, which selects a manager for administrative tasks"}')
        self.redis.lpush('govtcity_govttype', 'councilmanager')

        self.redis.lpush('name_countrytitle', 'Southern')
        self.redis.lpush('name_countrypre', 'Azer')
        self.redis.lpush('name_countryroot', 'do')
        self.redis.lpush('name_countrypost', 'bia')
        self.redis.lpush('name_countrytrailer', 'Province')
        self.redis.lpush('name_citytitle', 'Port')
        self.redis.lpush('name_cityroot', 'Arthur')
        self.redis.lpush('name_citypost', 'hall')
        self.redis.lpush('name_citytrailer', 'Rock')
        self.redis.zadd('city_size', '{ "name":"capitol",       "minpop":"30001", "maxpop":"80000", "min_density":"240", "max_density":"40000", "min_dist":3,  "max_dist":14 }', 100)
        self.redis.zadd('city_happiness', '{ "name":"estatic",     "score":100   }', 100)
        self.redis.zadd('city_health', '{ "name":"vigorous",       "score":100   }', 100)
        self.redis.zadd('city_age', '{ "name":"ancient",           "score":100    }', 100)
        self.redis.zadd('city_terrain', '{ "name": "jagged",         "score":100   }', 100)
        self.redis.zadd('city_pollution', '{ "name": "squalid",      "score":100  }', 100)
        self.redis.zadd('city_moral', '{ "name": "virtuous",         "score":100   }', 100)
        self.redis.zadd('city_order', '{ "name": "honorable",         "score":100   }', 100)
        self.redis.zadd('city_tolerance', '{ "name": "love",                        "score":100   }', 100)
        self.redis.zadd('city_economy', '{ "name": "lively",                        "score":100   }', 100)
        self.redis.zadd('city_military', '{ "name": "reverent",                     "score":100   }', 100)
        self.redis.zadd('city_magic', '{ "name": "growing",                         "score":100   }', 100)
        self.redis.zadd('city_education', '{ "name": "wonderful",                   "score":100   }', 100)
        self.redis.zadd('city_authority', '{ "name": "is very authoritarian",       "score":100   }', 100)
        self.redis.zadd('city_crime', '{ "name": "unheard of",                      "score":100   }', 100)
        self.redis.lpush('city_gatheringplace', 'adventurersguild')
        self.redis.lpush('npc_race','gnome')
        self.redis.lpush('gnome_covering','skin')
        self.redis.set('gnome_details',  '{"name": "Gnome",      "size": "small",   "description": "having engineering and intellectual expertise" }')
        self.redis.set('skin_covertemplate', '{{params.skinkind}}, {{params.skincolor}} skin')
        self.redis.lpush('skin_skincolor','alabaster')
        self.redis.lpush('skin_skinkind', 'thick')
        self.redis.lpush('phobia_template', "You are afraid.")
        self.redis.lpush('motivation_kind', 'acceptance')
        self.redis.lpush('motivationacceptance_text', 'to impress someone')
        self.redis.lpush('gnome_name_first_post', 'Tom')
        self.redis.lpush('gnome_name_last_pre', 'Gyro')
        self.redis.hset('gnome_name_first','post', 100)
        self.redis.hset('gnome_name_last','pre', 100)
        self.redis.zadd('gnome_name_order','{ "name":"first" }',50)
        self.redis.zadd('gnome_name_order','{ "name":"last"}',100)
        self.redis.zadd('npc_sex', '{"name":"male",       "pronoun":"he", "possessive":"his",  "third-person":"him", "spouse":"wife",    "score":100  }', 100)

    def tearDown(self):
        self.redis.flushall()

    def test_random_govt(self):
        """  """
        govt = Govt(self.redis)
        self.assertEqual('far longer than should be allowed', govt.age['name'])
    def test_static_body(self):
        """  """
        country=Country(self.redis)
        govt = Govt(self.redis,{'body':country})
        self.assertIn('Southern Azerdobia Province', str(govt.body))
        self.assertEqual(type(govt.body), Country)

    def test_static_body_country(self):
        """  """
        govt = Govt(self.redis,{'kind':'country'})
        self.assertIn('Southern Azerdobia Province', str(govt.body))
        self.assertEqual(type(govt.body), Country)


    def test_static_body_tacos(self):
        """  What happens if you pass in an unsupported kind? it defaults to country."""
        govt = Govt(self.redis,{'kind':'tacos'})
        self.assertIn('Southern Azerdobia Province', str(govt.body))
        self.assertEqual(type(govt.body), Country)


    def test_static_body_city(self):
        """  """
        self.redis.lpush('govt_kind', 'city')
        self.redis.hset('govtcity_govttype_description', 'councilmanager', '{ "name":"council/manager", "description":"things are run by a council, which selects a manager for administrative tasks"}')
        self.redis.lpush('govtcity_govttype', 'councilmanager')

        govt = Govt(self.redis,{'kind':'city'})
        self.assertIn('Port Arthurhall Rock', str(govt.body))
        self.assertEqual(type(govt.body), City)

