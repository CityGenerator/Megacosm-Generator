
# Joban\'s gang is a[n] ________, criminal organization
self.redis.zadd('organization_age', '{"name":"young",         "score":25   }', '25')
self.redis.zadd('organization_age', '{"name":"juvenile",      "score":50   }', '50')
self.redis.zadd('organization_age', '{"name":"mature",        "score":75   }', '75')
self.redis.zadd('organization_age', '{"name":"ancient",       "score":100  }', '100')

# The Joban gang is an ancient, ________ organization
self.redis.zadd('organization_legal', '{"name":"criminal",     "score":10   }', '10')
self.redis.zadd('organization_legal', '{"name":"dubious",      "score":30   }', '30')
self.redis.zadd('organization_legal', '{"name":"shady",        "score":40   }', '40')
self.redis.zadd('organization_legal', '{"name":"honorable",    "score":50   }', '50')
self.redis.zadd('organization_legal', '{"name":"legitimate",   "score":100   }', '100')


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
self.redis.zadd('organization_violence', '{"name":"murderous",      "score":10   }', '10')
self.redis.zadd('organization_violence', '{"name":"brutal",        "score":20   }', '20')
self.redis.zadd('organization_violence', '{"name":"violent",       "score":30   }', '30')
self.redis.zadd('organization_violence', '{"name":"coercive",      "score":40   }', '40')
self.redis.zadd('organization_violence', '{"name":"rough",         "score":40   }', '50')
self.redis.zadd('organization_violence', '{"name":"strict",        "score":60   }', '60')
self.redis.zadd('organization_violence', '{"name":"mild",          "score":80   }', '80')
self.redis.zadd('organization_violence', '{"name":"calm",          "score":90   }', '90')
self.redis.zadd('organization_violence', '{"name":"passive",       "score":100  }', '100')




# Members of Joban\'s gang are _________ by recent events
self.redis.zadd('organization_morale', '{"name":"demoralized",         "score":25   }', '25')
self.redis.zadd('organization_morale', '{"name":"unnerved",            "score":50   }', '50')
self.redis.zadd('organization_morale', '{"name":"comforted",           "score":75   }', '75')
self.redis.zadd('organization_morale', '{"name":"encouraged",          "score":100  }', '100')

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
self.redis.zadd('organization_leadership', '{ "name":"weak",       "score":30  }', '30')
self.redis.zadd('organization_leadership', '{ "name":"middling",   "score":60  }', '60')
self.redis.zadd('organization_leadership', '{ "name":"strong",     "score":100 }', '100')

# The Yakuza are _______________ structured.
self.redis.zadd('organization_structure', '{ "name":"loosely",    "score":30  }', '30')
self.redis.zadd('organization_structure', '{ "name":"barely",     "score":60  }', '60')
self.redis.zadd('organization_structure', '{ "name":"rigidly",    "score":100 }', '100')

# Insiders say the Yakuza  ________ internally.
self.redis.zadd('organization_stability', '{ "name":"are falling apart",  "score":20  }', '20')
self.redis.zadd('organization_stability', '{ "name":"are having issues",  "score":40  }', '40')
self.redis.zadd('organization_stability', '{ "name":"have their squabbles", "score":60  }', '60')
self.redis.zadd('organization_stability', '{ "name":"have few issues",    "score":80  }', '80')
self.redis.zadd('organization_stability', '{ "name":"are rock solid",     "score":100 }', '100')

# The leaders of Joban\'s gang _________ 
self.redis.zadd('organization_adaptability', '{"name":"fear change",                      "score":25   }', '25')
self.redis.zadd('organization_adaptability', '{"name":"like to avoid change",             "score":50   }', '50')
self.redis.zadd('organization_adaptability', '{"name":"keep an eye on trends",            "score":75   }', '75')
self.redis.zadd('organization_adaptability', '{"name":"stay ahead of new development",    "score":100  }', '100')

# When rules are broken, the Yakuza _________ punishment.
self.redis.zadd('organization_regulation', '{ "name":"never enforced",     "score":20  }', '20')
self.redis.zadd('organization_regulation', '{ "name":"rarely enforced",    "score":40  }', '40')
self.redis.zadd('organization_regulation', '{ "name":"usually enforced",   "score":60  }', '60')
self.redis.zadd('organization_regulation', '{ "name":"often enforced",     "score":80  }', '80')
self.redis.zadd('organization_regulation', '{ "name":"strictly enforced",  "score":100 }', '100')

# The rules for members of the Bloodhound Firm are __________- defined
self.redis.zadd('organization_rules', '{ "name":"loosely",    "score":25  }', '25')
self.redis.zadd('organization_rules', '{ "name":"barely",     "score":50  }', '50')
self.redis.zadd('organization_rules', '{ "name":"strictly",   "score":75  }', '75')
self.redis.zadd('organization_rules', '{ "name":"rigidly",    "score":100 }', '100')




# The Yakuza handles failure with _________.
self.redis.zadd('organization_failure', '{ "name":"a slow death",                  "score":20  }', '20')
self.redis.zadd('organization_failure', '{ "name":"a quick death",                 "score":40  }', '40')
self.redis.zadd('organization_failure', '{ "name":"a painful lesson",              "score":60  }', '60')
self.redis.zadd('organization_failure', '{ "name":"strict punishment",             "score":80  }', '80')
self.redis.zadd('organization_failure', '{ "name":"better guidance and training",  "score":100 }', '100')


# Members are expected to work  ______________.
self.redis.zadd('organization_teamwork', '{ "name":"as individuals acting alone",     "score":30  }', '30')
self.redis.zadd('organization_teamwork', '{ "name":"together to accomplish goals",    "score":60  }', '60')
self.redis.zadd('organization_teamwork', '{ "name":"as a well oiled machine",         "score":100 }', '100')


# The Yakuza are _______ to the average citizen
self.redis.zadd('organization_visibility', '{ "name":"unknown",               "score":10  }', '10')
self.redis.zadd('organization_visibility', '{ "name":"a myth",                "score":20  }', '20')
self.redis.zadd('organization_visibility', '{ "name":"simply rumors",         "score":30  }', '30')
self.redis.zadd('organization_visibility', '{ "name":"rarely known",          "score":70  }', '70')
self.redis.zadd('organization_visibility', '{ "name":"occasionally known",    "score":80  }', '80')
self.redis.zadd('organization_visibility', '{ "name":"sometimes known",       "score":90  }', '90')
self.redis.zadd('organization_visibility', '{ "name":"well known",            "score":100 }', '100')

# The Gogo Gang\'s influence expands across their __________.
self.redis.zadd('organization_size', '{ "name":"street",      "score":10  }', '10')
self.redis.zadd('organization_size', '{ "name":"district",    "score":20  }', '20')
self.redis.zadd('organization_size', '{ "name":"city",        "score":70  }', '70')
self.redis.zadd('organization_size', '{ "name":"region",      "score":80  }', '80')
self.redis.zadd('organization_size', '{ "name":"country",     "score":90  }', '90')
self.redis.zadd('organization_size', '{ "name":"continent",   "score":95  }', '95')
self.redis.zadd('organization_size', '{ "name":"world",       "score":100 }', '100')

# Anyone wishing to join Joban\'s gang will find it a[n] task.
self.redis.zadd('organization_entry', '{"name":"trivial",         "score":25   }', '25')
self.redis.zadd('organization_entry', '{"name":"easy",            "score":50   }', '50')
self.redis.zadd('organization_entry', '{"name":"tough",           "score":75   }', '75')
self.redis.zadd('organization_entry', '{"name":"impossible",      "score":100  }', '100')


###########################################
# TODO how do we deal with Sects? merge?


# Members of Joban\'s gang can be identified ________
self.redis.lpush('organization_identification', 'only by another member')
self.redis.lpush('organization_identification', 'by a specific insignia')
self.redis.lpush('organization_identification', 'by a specific article of clothing')
self.redis.lpush('organization_identification', 'by a tattoo')
self.redis.lpush('organization_identification', 'by a shared accent')
self.redis.lpush('organization_identification', 'with difficulty')

