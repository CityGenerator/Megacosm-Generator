
# street name

# {{tempobj.name.fullname}} is {{tempobj.popularity[\'name\']|article}} {{tempobj.size[\'name\']}} {{tempobj.kind}} that is {{tempobj.age[\'name\']|article}} {{tempobj.important[\'name\']}} route in the location.


self.redis.zadd('street_age', '{ "name":"new",             "score":30    }', '30')
self.redis.zadd('street_age', '{ "name":"established",     "score":40    }', '40')
self.redis.zadd('street_age', '{ "name":"modern",          "score":60    }', '60')
self.redis.zadd('street_age', '{ "name":"old",             "score":80    }', '80')
self.redis.zadd('street_age', '{ "name":"ancient",         "score":100   }', '100')

# Corning street is an unpopular narrow road that is an ancient  _________ route in the region
self.redis.zadd('street_important', '{ "name":"minor",      "score":50    }', '50')
self.redis.zadd('street_important', '{ "name":"major",      "score":90    }', '90')
self.redis.zadd('street_important', '{ "name":"primary",    "score":100   }', '100')

# Corning street is an unpopular narrow road that is an ancient major route in the _______
self.redis.zadd('street_scope', '{ "name":"district",    "score":25    }', '25')
self.redis.zadd('street_scope', '{ "name":"city",        "score":50    }', '50')
self.redis.zadd('street_scope', '{ "name":"region",      "score":75    }', '75')
self.redis.zadd('street_scope', '{ "name":"country",     "score":100   }', '100')

# Corning street is an unpopular ______ road that is an ancient major route in the region
self.redis.zadd('street_size', '{ "name":"narrow",           "score":50    }', '50')
self.redis.zadd('street_size', '{ "name":"broad",            "score":90    }', '90')
self.redis.zadd('street_size', '{ "name":"wide",             "score":100   }', '100')

self.redis.zadd('street_popularity', '{ "name":"unpopular",  "score":50    }', '50')
self.redis.zadd('street_popularity', '{ "name":"common",     "score":70    }', '70')
self.redis.zadd('street_popularity', '{ "name":"popular",    "score":100   }', '100')

# Boson ________ is a[n] popular  ______ that runs ________
self.redis.lpush('street_kind', 'path')
self.redis.lpush('street_kind', 'trail')
self.redis.lpush('street_kind', 'track')
self.redis.lpush('street_kind', 'boardwalk')
self.redis.lpush('street_kind', 'byway')
self.redis.lpush('street_kind', 'avenue')
self.redis.lpush('street_kind', 'passage')
self.redis.lpush('street_kind', 'road')
self.redis.lpush('street_kind', 'street')
self.redis.lpush('street_kind', 'route')
self.redis.lpush('street_kind', 'through-way')

#        <pollution>
self.redis.zadd('street_pollution', '{"name":"pristine",       "score":10  }', '10')
self.redis.zadd('street_pollution', '{"name":"sterile",        "score":20  }', '20')
self.redis.zadd('street_pollution', '{"name":"clean",          "score":30  }', '30')
self.redis.zadd('street_pollution', '{"name":"tidy",           "score":40  }', '40')
self.redis.zadd('street_pollution', '{"name":"disheveled",     "score":60  }', '60')
self.redis.zadd('street_pollution', '{"name":"grungy",         "score":70  }', '70')
self.redis.zadd('street_pollution', '{"name":"polluted",       "score":80  }', '80')
self.redis.zadd('street_pollution', '{"name":"filthy",         "score":90  }', '90')
self.redis.zadd('street_pollution', '{"name":"squalid",        "score":100 }', '100')


#        <terrain>
self.redis.zadd('street_terrain', '{"name":"flat",         "score":10  }', '10')
self.redis.zadd('street_terrain', '{"name":"even",         "score":20  }', '20')
self.redis.zadd('street_terrain', '{"name":"rolling",      "score":30  }', '30')
self.redis.zadd('street_terrain', '{"name":"hilly",        "score":40  }', '40')
self.redis.zadd('street_terrain', '{"name":"uneven",       "score":60  }', '60')
self.redis.zadd('street_terrain', '{"name":"rough",        "score":70  }', '70')
self.redis.zadd('street_terrain', '{"name":"rugged",       "score":80  }', '80')
self.redis.zadd('street_terrain', '{"name":"broken",       "score":90  }', '90')
self.redis.zadd('street_terrain', '{"name":"jagged",      "score":100 }', '100')
#
#
#        <moral>
self.redis.zadd('street_moral', '{"name":"untrustworthy",                                    "score":4  }', '4')
self.redis.zadd('street_moral', '{"name":"mean",                                    "score":8  }', '8')
self.redis.zadd('street_moral', '{"name":"venomous",                                    "score":12  }', '12')
self.redis.zadd('street_moral', '{"name":"corrupt",                                    "score":16  }', '16')
self.redis.zadd('street_moral', '{"name":"repugnant",                                    "score":20  }', '20')
self.redis.zadd('street_moral', '{"name":"unpleasant",                                    "score":24  }', '24')
self.redis.zadd('street_moral', '{"name":"opportunistic",                                    "score":28  }', '28')
self.redis.zadd('street_moral', '{"name":"villainous",                                    "score":32  }', '32')
self.redis.zadd('street_moral', '{"name":"nefarious",                                    "score":36  }', '36')
self.redis.zadd('street_moral', '{"name":"cold",                                    "score":40  }', '40')
self.redis.zadd('street_moral', '{"name":"unconcerned",                                    "score":45  }', '45')
self.redis.zadd('street_moral', '{"name":"undecided",                                    "score":50  }', '50')
self.redis.zadd('street_moral', '{"name":"uncommitted",                                    "score":55  }', '55')
self.redis.zadd('street_moral', '{"name":"indifferent",                                    "score":60  }', '60')
self.redis.zadd('street_moral', '{"name":"indifferent",                                    "score":65  }', '65')
self.redis.zadd('street_moral', '{"name":"well meaning",                                    "score":70  }', '70')
self.redis.zadd('street_moral', '{"name":"trustworthy",                                    "score":75  }', '75')
self.redis.zadd('street_moral', '{"name":"nice",                                    "score":80  }', '80')
self.redis.zadd('street_moral', '{"name":"ethical",                                    "score":85  }', '85')
self.redis.zadd('street_moral', '{"name":"honest",                                    "score":90  }', '90')
self.redis.zadd('street_moral', '{"name":"praise-worthy",                                    "score":95  }', '95')
self.redis.zadd('street_moral', '{"name":"virtuous",                                    "score":100  }', '100')
#
#
#
#        <order>
self.redis.zadd('street_order', '{"name":"unreliable",                                         "score":5  }', '5')
self.redis.zadd('street_order', '{"name":"irresponsible",                                         "score":10  }', '10')
self.redis.zadd('street_order', '{"name":"questionable",                                         "score":15  }', '15')
self.redis.zadd('street_order', '{"name":"unpredictable",                                         "score":20  }', '20')
self.redis.zadd('street_order', '{"name":"deranged",                                         "score":25  }', '25')
self.redis.zadd('street_order', '{"name":"incoherent",                                         "score":30  }', '30')
self.redis.zadd('street_order', '{"name":"vague",                                         "score":35  }', '35')
self.redis.zadd('street_order', '{"name":"bystanding",                                         "score":40  }', '40')
self.redis.zadd('street_order', '{"name":"detached",                                         "score":45  }', '45')
self.redis.zadd('street_order', '{"name":"non-participating",                                         "score":50  }', '50')
self.redis.zadd('street_order', '{"name":"non-conformist",                                         "score":55  }', '55')
self.redis.zadd('street_order', '{"name":"unflappable",                                         "score":60  }', '60')
self.redis.zadd('street_order', '{"name":"reliable",                                         "score":65  }', '65')
self.redis.zadd('street_order', '{"name":"dependable",                                         "score":70  }', '70')
self.redis.zadd('street_order', '{"name":"sure",                                         "score":75  }', '75')
self.redis.zadd('street_order', '{"name":"legitimized",                                         "score":80  }', '80')
self.redis.zadd('street_order', '{"name":"organized",                                         "score":85  }', '85')
self.redis.zadd('street_order', '{"name":"dutiful",                                         "score":90  }', '90')
self.redis.zadd('street_order', '{"name":"honorable",                                         "score":100  }', '100')
#
#
#        <tolerance>
self.redis.zadd('street_tolerance', '{"name":"despise",                                         "score":20  }', '20')
self.redis.zadd('street_tolerance', '{"name":"hate",                                         "score":30  }', '30')
self.redis.zadd('street_tolerance', '{"name":"are critical of",                                         "score":40  }', '40')
self.redis.zadd('street_tolerance', '{"name":"ignore",                                         "score":50  }', '50')
self.redis.zadd('street_tolerance', '{"name":"are neutral towards",                                         "score":60  }', '60')
self.redis.zadd('street_tolerance', '{"name":"are accepting of",                                         "score":70  }', '70')
self.redis.zadd('street_tolerance', '{"name":"accept",                                         "score":80  }', '80')
self.redis.zadd('street_tolerance', '{"name":"love",                                         "score":100  }', '100')
#
#        <economy>
self.redis.zadd('street_economy', '{"name":"crumbling",                                         "score":6  }', '6')
self.redis.zadd('street_economy', '{"name":"failing",                                         "score":12  }', '12')
self.redis.zadd('street_economy', '{"name":"uncertain",                                         "score":18  }', '18')
self.redis.zadd('street_economy', '{"name":"shaky",                                         "score":24  }', '24')
self.redis.zadd('street_economy', '{"name":"weak",                                         "score":30  }', '30')
self.redis.zadd('street_economy', '{"name":"calm",                                         "score":36  }', '36')
self.redis.zadd('street_economy', '{"name":"stable",                                         "score":42  }', '42')
self.redis.zadd('street_economy', '{"name":"insulated",                                         "score":48  }', '48')
self.redis.zadd('street_economy', '{"name":"unwavering",                                         "score":54  }', '54')
self.redis.zadd('street_economy', '{"name":"steady",                                         "score":60  }', '60')
self.redis.zadd('street_economy', '{"name":"steadfast",                                         "score":66  }', '66')
self.redis.zadd('street_economy', '{"name":"good",                                         "score":72  }', '72')
self.redis.zadd('street_economy', '{"name":"healthy",                                         "score":78  }', '78')
self.redis.zadd('street_economy', '{"name":"flourishing",                                         "score":84  }', '84')
self.redis.zadd('street_economy', '{"name":"growing",                                         "score":90  }', '90')
self.redis.zadd('street_economy', '{"name":"vibrant",                                         "score":96  }', '96')
self.redis.zadd('street_economy', '{"name":"lively",                                         "score":100  }', '100')
#
#        <crime>
self.redis.zadd('street_crime', '{"name":"rampant",                                        "score":10  }', '10')
self.redis.zadd('street_crime', '{"name":"common",                                         "score":30  }', '30')
self.redis.zadd('street_crime', '{"name":"occasional",                                     "score":50  }', '50')
self.redis.zadd('street_crime', '{"name":"unusual",                                        "score":70  }', '70')
self.redis.zadd('street_crime', '{"name":"rare",                                           "score":90  }', '90')
self.redis.zadd('street_crime', '{"name":"unheard of",                                     "score":100  }', '100')


#muddy filthy
#
self.redis.zadd('street_repair', '{ "name":"broken",              "score":10   }', '10')
self.redis.zadd('street_repair', '{ "name":"rough",               "score":20   }', '20')
self.redis.zadd('street_repair', '{ "name":"crude",               "score":30   }', '30')
self.redis.zadd('street_repair', '{ "name":"irregular",           "score":40   }', '40')
self.redis.zadd('street_repair', '{ "name":"bumpy",               "score":50   }', '50')
self.redis.zadd('street_repair', '{ "name":"even",                "score":60   }', '60')
self.redis.zadd('street_repair', '{ "name":"smooth",              "score":70   }', '70')
self.redis.zadd('street_repair', '{ "name":"well-maintained",     "score":80   }', '80')
self.redis.zadd('street_repair', '{ "name":"pristine",            "score":100   }', '100')


self.redis.lpush('street_material', 'dirt')
self.redis.lpush('street_material', 'gravel')
self.redis.lpush('street_material', 'cobblestone')
self.redis.lpush('street_material', 'pavingstone')
self.redis.lpush('street_material', 'flagstone')





#        <trailer>in a grid pattern
#        <trailer>in a ray pattern
#        <trailer>in a contour-forming pattern
#        <trailer>in an irregular pattern
#        <trailer>in a random mesh pattern
#        <trailer>in an organic pattern
#        <trailer>in a fragmented parallel pattern
#        <trailer>in a looped pattern
#        <trailer>in a warped parallel pattern
#        <trailer>in a linear pattern
#        <trailer>in a wheel and spoke pattern
#
#    <popdensity>
#        <option          max:"20" type:"sparsely"   />
#        <option min:"21" max:"40" type:"lightly"    />
#        <option min:"41" max:"60" type:"nominally"  />
#        <option min:"61" max:"80" type:"moderately" />
#        <option min:"81"          type:"densely"    />
