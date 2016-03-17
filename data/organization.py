
# Joban\'s gang is a[n] ________, criminal organization
ZADD organization_age 25   {"name":"young",         "score":25   }
ZADD organization_age 50   {"name":"juvenile",      "score":50   }
ZADD organization_age 75   {"name":"mature",        "score":75   }
ZADD organization_age 100  {"name":"ancient",       "score":100  }

# The Joban gang is an ancient, ________ organization
ZADD organization_legal  10 {"name":"criminal",     "score":10   }
ZADD organization_legal  30 {"name":"dubious",      "score":30   }
ZADD organization_legal  40 {"name":"shady",        "score":40   }
ZADD organization_legal  50 {"name":"honorable",    "score":50   }
ZADD organization_legal 100 {"name":"legitimate",   "score":100   }


# The Joban gang is an ancient, honorable ________________
self.redis.lpush('organization_kind', 'association')
self.redis.lpush('organization_kind', 'cartel')
self.redis.lpush('organization_kind', 'circle')
self.redis.lpush('organization_kind', 'club')
self.redis.lpush('organization_kind', 'council')
self.redis.lpush('organization_kind', 'family')
self.redis.lpush('organization_kind', 'firm')
self.redis.lpush('organization_kind', 'fraternity')
self.redis.lpush('organization_kind', 'gang')
self.redis.lpush('organization_kind', 'guild')
self.redis.lpush('organization_kind', 'mafia')
self.redis.lpush('organization_kind', 'militia')
self.redis.lpush('organization_kind', 'network')
self.redis.lpush('organization_kind', 'order')
self.redis.lpush('organization_kind', 'organization')
self.redis.lpush('organization_kind', 'society')
self.redis.lpush('organization_kind', 'tribe')
self.redis.lpush('organization_kind', 'union')
self.redis.lpush('organization_kind', 'crime ring')

# The Joban gang is an ancient, honorable organization with a ________ reputation
ZADD organization_violence  10 {"name":"murderous",      "score":10   }
ZADD organization_violence  20 {"name":"brutal",        "score":20   }
ZADD organization_violence  30 {"name":"violent",       "score":30   }
ZADD organization_violence  40 {"name":"coercive",      "score":40   }
ZADD organization_violence  50 {"name":"rough",         "score":40   }
ZADD organization_violence  60 {"name":"strict",        "score":60   }
ZADD organization_violence  80 {"name":"mild",          "score":80   }
ZADD organization_violence  90 {"name":"calm",          "score":90   }
ZADD organization_violence 100 {"name":"passive",       "score":100  }




# Members of Joban\'s gang are _________ by recent events
ZADD organization_morale 25   {"name":"demoralized",         "score":25   }
ZADD organization_morale 50   {"name":"unnerved",            "score":50   }
ZADD organization_morale 75   {"name":"comforted",           "score":75   }
ZADD organization_morale 100  {"name":"encouraged",          "score":100  }

# The Yakuza\'s is a[n] _________ power in their district.
self.redis.lpush('organization_powertype', 'charismatic')
self.redis.lpush('organization_powertype', 'political')
self.redis.lpush('organization_powertype', 'religious')
self.redis.lpush('organization_powertype', 'criminal')
self.redis.lpush('organization_powertype', 'cooperative')
self.redis.lpush('organization_powertype', 'academic')
self.redis.lpush('organization_powertype', 'military')
self.redis.lpush('organization_powertype', 'cultural')
self.redis.lpush('organization_powertype', 'economic')
self.redis.lpush('organization_powertype', 'philosophical')
self.redis.lpush('organization_powertype', 'physical')
self.redis.lpush('organization_powertype', 'mercenary')
self.redis.lpush('organization_powertype', 'aristocratic ')
self.redis.lpush('organization_powertype', 'athletic')
self.redis.lpush('organization_powertype', 'investment')
self.redis.lpush('organization_powertype', 'gambling')


# Leadership within the  Yakuza is  ______________.
ZADD organization_leadership  30 { "name":"weak",       "score":30  }
ZADD organization_leadership  60 { "name":"middling",   "score":60  }
ZADD organization_leadership 100 { "name":"strong",     "score":100 }

# The Yakuza are _______________ structured.
ZADD organization_structure  30 { "name":"loosely",    "score":30  }
ZADD organization_structure  60 { "name":"barely",     "score":60  }
ZADD organization_structure 100 { "name":"rigidly",    "score":100 }

# Insiders say the Yakuza  ________ internally.
ZADD organization_stability  20 { "name":"are falling apart",  "score":20  }
ZADD organization_stability  40 { "name":"are having issues",  "score":40  }
ZADD organization_stability  60 { "name":"have their squabbles", "score":60  }
ZADD organization_stability  80 { "name":"have few issues",    "score":80  }
ZADD organization_stability 100 { "name":"are rock solid",     "score":100 }

# The leaders of Joban\'s gang _________ 
ZADD organization_adaptability 25   {"name":"fear change",                      "score":25   }
ZADD organization_adaptability 50   {"name":"like to avoid change",             "score":50   }
ZADD organization_adaptability 75   {"name":"keep an eye on trends",            "score":75   }
ZADD organization_adaptability 100  {"name":"stay ahead of new development",    "score":100  }

# When rules are broken, the Yakuza _________ punishment.
ZADD organization_regulation  20 { "name":"never enforced",     "score":20  }
ZADD organization_regulation  40 { "name":"rarely enforced",    "score":40  }
ZADD organization_regulation  60 { "name":"usually enforced",   "score":60  }
ZADD organization_regulation  80 { "name":"often enforced",     "score":80  }
ZADD organization_regulation 100 { "name":"strictly enforced",  "score":100 }

# The rules for members of the Bloodhound Firm are __________- defined
ZADD organization_rules  25 { "name":"loosely",    "score":25  }
ZADD organization_rules  50 { "name":"barely",     "score":50  }
ZADD organization_rules  75 { "name":"strictly",   "score":75  }
ZADD organization_rules 100 { "name":"rigidly",    "score":100 }




# The Yakuza handles failure with _________.
ZADD organization_failure  20 { "name":"a slow death",                  "score":20  }
ZADD organization_failure  40 { "name":"a quick death",                 "score":40  }
ZADD organization_failure  60 { "name":"a painful lesson",              "score":60  }
ZADD organization_failure  80 { "name":"strict punishment",             "score":80  }
ZADD organization_failure 100 { "name":"better guidance and training",  "score":100 }


# Members are expected to work  ______________.
ZADD organization_teamwork  30 { "name":"as individuals acting alone",     "score":30  }
ZADD organization_teamwork  60 { "name":"together to accomplish goals",    "score":60  }
ZADD organization_teamwork 100 { "name":"as a well oiled machine",         "score":100 }


# The Yakuza are _______ to the average citizen
ZADD organization_visibility  10 { "name":"unknown",               "score":10  }
ZADD organization_visibility  20 { "name":"a myth",                "score":20  }
ZADD organization_visibility  30 { "name":"simply rumors",         "score":30  }
ZADD organization_visibility  70 { "name":"rarely known",          "score":70  }
ZADD organization_visibility  80 { "name":"occasionally known",    "score":80  }
ZADD organization_visibility  90 { "name":"sometimes known",       "score":90  }
ZADD organization_visibility 100 { "name":"well known",            "score":100 }

# The Gogo Gang\'s influence expands across their __________.
ZADD organization_size  10 { "name":"street",      "score":10  }
ZADD organization_size  20 { "name":"district",    "score":20  }
ZADD organization_size  70 { "name":"city",        "score":70  }
ZADD organization_size  80 { "name":"region",      "score":80  }
ZADD organization_size  90 { "name":"country",     "score":90  }
ZADD organization_size  95 { "name":"continent",   "score":95  }
ZADD organization_size 100 { "name":"world",       "score":100 }

# Anyone wishing to join Joban\'s gang will find it a[n] task.
ZADD organization_entry 25   {"name":"trivial",         "score":25   }
ZADD organization_entry 50   {"name":"easy",            "score":50   }
ZADD organization_entry 75   {"name":"tough",           "score":75   }
ZADD organization_entry 100  {"name":"impossible",      "score":100  }


###########################################
# TODO how do we deal with Sects? merge?


# Members of Joban\'s gang can be identified ________
self.redis.lpush('organization_identification', 'only by another member')
self.redis.lpush('organization_identification', 'by a specific insignia')
self.redis.lpush('organization_identification', 'by a specific article of clothing')
self.redis.lpush('organization_identification', 'by a tattoo')
self.redis.lpush('organization_identification', 'by a shared accent')
self.redis.lpush('organization_identification', 'with difficulty')

