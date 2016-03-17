

self.redis.zadd('region_size', '{"name":"tiny",     "mincities":1,   "maxcities":2,       "score":5     }', '5')
self.redis.zadd('region_size', '{"name":"small",    "mincities":2,   "maxcities":5,       "score":30    }', '30')
self.redis.zadd('region_size', '{"name":"medium",   "mincities":2,   "maxcities":10,      "score":70    }', '70')
self.redis.zadd('region_size', '{"name":"large",    "mincities":5,   "maxcities":20,      "score":100   }', '100')


#People think the government of Bogoland is _____________________,

self.redis.zadd('region_corruption', '{ "name":"the epitome of corruption",     "score":5    }', '5')
self.redis.zadd('region_corruption', '{ "name":"corrupt and nefarious",     "score":10    }', '10')
self.redis.zadd('region_corruption', '{ "name":"willing to look the other way for the right price",     "score":15    }', '15')
self.redis.zadd('region_corruption', '{ "name":"crooked",         "score":20    }', '20')
self.redis.zadd('region_corruption', '{ "name":"on the take",     "score":25    }', '25')
self.redis.zadd('region_corruption', '{ "name":"underhanded",     "score":30    }', '30')
self.redis.zadd('region_corruption', '{ "name":"unethical",       "score":35    }', '35')
self.redis.zadd('region_corruption', '{ "name":"disreputable",    "score":40    }', '40')
self.redis.zadd('region_corruption', '{ "name":"equitable",       "score":45    }', '45')
self.redis.zadd('region_corruption', '{ "name":"reasonable",      "score":50    }', '50')
self.redis.zadd('region_corruption', '{ "name":"fair",            "score":55    }', '55')
self.redis.zadd('region_corruption', '{ "name":"honest",          "score":60    }', '60')
self.redis.zadd('region_corruption', '{ "name":"principled",      "score":65    }', '65')
self.redis.zadd('region_corruption', '{ "name":"decent",          "score":70    }', '70')
self.redis.zadd('region_corruption', '{ "name":"resolute",        "score":75    }', '75')
self.redis.zadd('region_corruption', '{ "name":"honorable",       "score":80    }', '80')
self.redis.zadd('region_corruption', '{ "name":"trustworthy",     "score":85    }', '85')
self.redis.zadd('region_corruption', '{ "name":"upright",         "score":90    }', '90')
self.redis.zadd('region_corruption', '{ "name":"virtuous",        "score":95    }', '95')
self.redis.zadd('region_corruption', '{ "name":"incorruptible",   "score":100    }', '100')

# citizens _________ of the country\'s leadership
self.redis.zadd('region_countryapproval', '{ "name":"despise",        "score":5     }', '5')
self.redis.zadd('region_countryapproval', '{ "name":"hate",           "score":10    }', '10')
self.redis.zadd('region_countryapproval', '{ "name":"fear",           "score":15    }', '15')
self.redis.zadd('region_countryapproval', '{ "name":"ridicule",       "score":20    }', '20')
self.redis.zadd('region_countryapproval', '{ "name":"mock",           "score":25    }', '25')
self.redis.zadd('region_countryapproval', '{ "name":"respect",        "score":30    }', '30')
self.redis.zadd('region_countryapproval', '{ "name":"praise",         "score":80    }', '80')
self.redis.zadd('region_countryapproval', '{ "name":"honor",          "score":90    }', '90')
self.redis.zadd('region_countryapproval', '{ "name":"love",           "score":95    }', '95')
self.redis.zadd('region_countryapproval', '{ "name":"revere",         "score":100   }', '100')


# The region\'s Government is often described as ____________________
self.redis.zadd('region_efficiency', '{ "name":"the pinnacle of inefficiency",       "score":5     }', '5')
self.redis.zadd('region_efficiency', '{ "name":"incapable of even simple tasks",     "score":10    }', '10')
self.redis.zadd('region_efficiency', '{ "name":"clearly incompetent",                "score":15    }', '15')
self.redis.zadd('region_efficiency', '{ "name":"horribly inefficient",               "score":20    }', '20')
self.redis.zadd('region_efficiency', '{ "name":"sloppy and disorganized",            "score":25    }', '25')
self.redis.zadd('region_efficiency', '{ "name":"inept and inadequate",               "score":30    }', '30')
self.redis.zadd('region_efficiency', '{ "name":"slipshod",                           "score":35    }', '35')
self.redis.zadd('region_efficiency', '{ "name":"minimally competent",                "score":40    }', '40')
self.redis.zadd('region_efficiency', '{ "name":"somewhat capable",                    "score":45    }', '45')
self.redis.zadd('region_efficiency', '{ "name":"adequate",                           "score":50    }', '50')
self.redis.zadd('region_efficiency', '{ "name":"satisfactory",                       "score":55    }', '55')
self.redis.zadd('region_efficiency', '{ "name":"mostly sufficient",                  "score":60    }', '60')
self.redis.zadd('region_efficiency', '{ "name":"surprisingly decent",                "score":65    }', '65')
self.redis.zadd('region_efficiency', '{ "name":"effective overall",                  "score":70    }', '70')
self.redis.zadd('region_efficiency', '{ "name":"on the ball",                        "score":75    }', '75')
self.redis.zadd('region_efficiency', '{ "name":"efficient",                          "score":80    }', '80')
self.redis.zadd('region_efficiency', '{ "name":"shrewd",                             "score":85    }', '85')
self.redis.zadd('region_efficiency', '{ "name":"surprisingly skillful",              "score":90    }', '90')
self.redis.zadd('region_efficiency', '{ "name":"magnificently organized",            "score":95    }', '95')
self.redis.zadd('region_efficiency', '{ "name":"ruthlessly effective",               "score":100   }', '100')


# The political influence of __region__ in the country is __INFLUENCE__ 
self.redis.zadd('region_influence', '{ "name":"negligible",            "score":5     }', '5')
self.redis.zadd('region_influence', '{ "name":"dwindling rapidly",     "score":10    }', '10')
self.redis.zadd('region_influence', '{ "name":"wilting",               "score":15    }', '15')
self.redis.zadd('region_influence', '{ "name":"wasting away",          "score":20    }', '20')
self.redis.zadd('region_influence', '{ "name":"shrinking",             "score":25    }', '25')
self.redis.zadd('region_influence', '{ "name":"declining",             "score":30    }', '30')
self.redis.zadd('region_influence', '{ "name":"receding",              "score":35    }', '35')
self.redis.zadd('region_influence', '{ "name":"consistent",            "score":40    }', '40')
self.redis.zadd('region_influence', '{ "name":"steady",                "score":45    }', '45')
self.redis.zadd('region_influence', '{ "name":"lasting",               "score":50    }', '50')
self.redis.zadd('region_influence', '{ "name":"enduring",              "score":55    }', '55')
self.redis.zadd('region_influence', '{ "name":"steadfast",             "score":60    }', '60')
self.redis.zadd('region_influence', '{ "name":"unwavering",            "score":65    }', '65')
self.redis.zadd('region_influence', '{ "name":"broadening",            "score":70    }', '70')
self.redis.zadd('region_influence', '{ "name":"improving",             "score":75    }', '75')
self.redis.zadd('region_influence', '{ "name":"spreading",             "score":80    }', '80')
self.redis.zadd('region_influence', '{ "name":"growing",               "score":85    }', '85')
self.redis.zadd('region_influence', '{ "name":"maturing",              "score":90    }', '90')
self.redis.zadd('region_influence', '{ "name":"flourishing",           "score":95    }', '95')
self.redis.zadd('region_influence', '{ "name":"thriving",              "score":100   }', '100')

# In times of crisis, the population ___________.
self.redis.zadd('region_unity', '{ "name":"turns against itself",                               "score":10    }', '10')
self.redis.zadd('region_unity', '{ "name":"is eager to point fingers",                          "score":20    }', '20')
self.redis.zadd('region_unity', '{ "name":"gives up their freedom in exchange for security",    "score":30    }', '30')
self.redis.zadd('region_unity', '{ "name":"flees for the hills",                                "score":40    }', '40')
self.redis.zadd('region_unity', '{ "name":"cowers in fear",                                     "score":50    }', '50')
self.redis.zadd('region_unity', '{ "name":"squabbles amongst themselves",                       "score":60    }', '60')
self.redis.zadd('region_unity', '{ "name":"stages ineffective protests",                        "score":70    }', '70')
self.redis.zadd('region_unity', '{ "name":"overcomes their differences",                        "score":80    }', '80')
self.redis.zadd('region_unity', '{ "name":"comes together and fights as one",                   "score":90    }', '90')
self.redis.zadd('region_unity', '{ "name":"rallies behind its leaders",                         "score":100   }', '100')

# Socially, Bogoland is _______________

self.redis.zadd('region_social', '{"name":"libertarian",         "score":5     }', '5')
self.redis.zadd('region_social', '{"name":"populist",            "score":10    }', '10')
self.redis.zadd('region_social', '{"name":"individualistic",     "score":30    }', '30')
self.redis.zadd('region_social', '{"name":"balanced",            "score":40    }', '40')
self.redis.zadd('region_social', '{"name":"rigid",               "score":60    }', '60')
self.redis.zadd('region_social', '{"name":"harsh",               "score":80    }', '80')
self.redis.zadd('region_social', '{"name":"disciplinarian",      "score":95    }', '95')
self.redis.zadd('region_social', '{"name":"authoritarian",       "score":100   }', '100')

# and _______________

self.redis.zadd('region_economic', '{"name":"liberal",          "score":10    }', '10')
self.redis.zadd('region_economic', '{"name":"progressive",      "score":20    }', '20')
self.redis.zadd('region_economic', '{"name":"lenient",          "score":30    }', '30')
self.redis.zadd('region_economic', '{"name":"permissive",       "score":40    }', '40')
self.redis.zadd('region_economic', '{"name":"understanding",    "score":60    }', '60')
self.redis.zadd('region_economic', '{"name":"strict",           "score":70    }', '70')
self.redis.zadd('region_economic', '{"name":"limited",          "score":80    }', '80')
self.redis.zadd('region_economic', '{"name":"intolerant",       "score":90    }', '90')
self.redis.zadd('region_economic', '{"name":"conservative",     "score":100   }', '100')

#  Religion in Willis ________.
self.redis.zadd('region_theology', '{ "name":"is strictly forbidden on pain of death",                                 "score":5    }', '5')
self.redis.zadd('region_theology', '{ "name":"is forbidden",                                                          "score":10    }', '10')
self.redis.zadd('region_theology', '{ "name":"will get you in trouble",                                               "score":15    }', '15')
self.redis.zadd('region_theology', '{ "name":"is unwelcome",                                                          "score":20    }', '20')
self.redis.zadd('region_theology', '{ "name":"is unregulated",                                                        "score":25    }', '25')
self.redis.zadd('region_theology', '{ "name":"is taxed heavily",                                                      "score":30    }', '30')
self.redis.zadd('region_theology', '{ "name":"is tightly regulated by the government",                                "score":35    }', '35')
self.redis.zadd('region_theology', '{ "name":"is viewed as a nuisance",                                               "score":40    }', '40')
self.redis.zadd('region_theology', '{ "name":"is practiced behind closed doors",                                      "score":45    }', '45')
self.redis.zadd('region_theology', '{ "name":"is left to the people",                                                 "score":50    }', '50')
self.redis.zadd('region_theology', '{ "name":"is common place",                                                       "score":55    }', '55')
self.redis.zadd('region_theology', '{ "name":"is unregulated and diverse, making it a melting pot of many faiths",    "score":60    }', '60')
self.redis.zadd('region_theology', '{ "name":"enjoys many legal benefits",                                            "score":65    }', '65')
self.redis.zadd('region_theology', '{ "name":"is widespread",                                                         "score":70    }', '70')
self.redis.zadd('region_theology', '{ "name":"is sanctioned by the government",                                       "score":75    }', '75')
self.redis.zadd('region_theology', '{ "name":"is limited to a single deity",                                          "score":80    }', '80')
self.redis.zadd('region_theology', '{ "name":"plays a central role in the lawmaking process",                         "score":85    }', '85')
self.redis.zadd('region_theology', '{ "name":"controlled by the government",                                          "score":90    }', '90')
self.redis.zadd('region_theology', '{ "name":"is sacred, and the words of the gods are law",                          "score":95    }', '95')
self.redis.zadd('region_theology', '{ "name":"is used to control the populace",                                      "score":100    }', '100')
 
#    <arable>
#        <option type:"poor"     min:\'1\' max:\'33\'>desolate
#        <option type:"neutral"  min:\'34\' max:\'66\'>modest
#        <option type:"rich"     min:\'67\' >fertile

