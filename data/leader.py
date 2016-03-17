

self.redis.lpush('leader_scope', 'country')
self.redis.lpush('leader_scope', 'region')
self.redis.lpush('leader_scope', 'city')
self.redis.lpush('leader_scope', 'organization')

self.redis.lpush('leadercountry_kind', 'absolutemonarchy')
self.redis.lpush('leadercountry_kind', 'authoritarian')
self.redis.lpush('leadercountry_kind', 'commonwealth')
self.redis.lpush('leadercountry_kind', 'communist')
self.redis.lpush('leadercountry_kind', 'constitutional')
self.redis.lpush('leadercountry_kind', 'democracy')
self.redis.lpush('leadercountry_kind', 'dictatorship')
self.redis.lpush('leadercountry_kind', 'ecclesiastical')
self.redis.lpush('leadercountry_kind', 'emirate')
self.redis.lpush('leadercountry_kind', 'federation')
self.redis.lpush('leadercountry_kind', 'monarchy')
self.redis.lpush('leadercountry_kind', 'oligarchy')
self.redis.lpush('leadercountry_kind', 'parliamentary')
self.redis.lpush('leadercountry_kind', 'republic')
self.redis.lpush('leadercountry_kind', 'theocracy')
self.redis.lpush('leadercountry_kind', 'totalitarian')

self.redis.lpush('leaderregion_kind', 'barony')
self.redis.lpush('leaderregion_kind', 'duchy')
self.redis.lpush('leaderregion_kind', 'governship')


self.redis.lpush('leadercity_kind', 'councilmanager')
self.redis.lpush('leadercity_kind', 'mayorcouncil')
self.redis.lpush('leadercity_kind', 'commission')
self.redis.lpush('leadercity_kind', 'townmeeting')
self.redis.lpush('leadercity_kind', 'magistrate')

self.redis.lpush('leaderorganization_kind', 'guild')
self.redis.lpush('leaderorganization_kind', 'gang')
self.redis.lpush('leaderorganization_kind', 'union')

self.redis.lpush('leadergovernship_leader', 'governor')
HSET  leadergovernship_leader_description governor { "male":"Governor",     "female":"Governor"     }

self.redis.lpush('leaderabsolutemonarchy_leader', 'king')
HSET  leaderabsolutemonarchy_leader_description king { "male":"King",    "female":"Queen"     }
self.redis.lpush('leaderabsolutemonarchy_leader', 'emperor')
HSET  leaderabsolutemonarchy_leader_description emperor { "male":"Emperor", "female":"Empress"   }
self.redis.lpush('leaderabsolutemonarchy_leader', 'raja')
HSET  leaderabsolutemonarchy_leader_description raja { "male":"Raja",    "female":"Rani"      }
self.redis.lpush('leaderabsolutemonarchy_leader', 'sultan')
HSET  leaderabsolutemonarchy_leader_description sultan { "male":"Sultan",  "female":"Sultana"   }
self.redis.lpush('leaderabsolutemonarchy_leader', 'shah')
HSET  leaderabsolutemonarchy_leader_description shah { "male":"Shah",    "female":"Shahbanu"  }
self.redis.lpush('leaderabsolutemonarchy_leader', 'prince')
HSET  leaderabsolutemonarchy_leader_description prince { "male":"Prince",  "female":"Princess"  }

self.redis.lpush('leaderbarony_leader', 'baron')
HSET  leaderbarony_leader_description baron { "male":"Baron",      "female":"Baroness"      }

self.redis.lpush('leaderauthoritarian_leader', 'boss')
HSET  leaderauthoritarian_leader_description boss { "male":"Boss",         "female":"Boss"         }
self.redis.lpush('leaderauthoritarian_leader', 'captain')
HSET  leaderauthoritarian_leader_description captain { "male":"Captain",      "female":"Captain"      }
self.redis.lpush('leaderauthoritarian_leader', 'chairman')
HSET  leaderauthoritarian_leader_description chairman { "male":"Chairman",     "female":"Chairman"     }
self.redis.lpush('leaderauthoritarian_leader', 'chief')
HSET  leaderauthoritarian_leader_description chief { "male":"Chief",        "female":"Chief"        }
self.redis.lpush('leaderauthoritarian_leader', 'commander')
HSET  leaderauthoritarian_leader_description commander { "male":"Commander",    "female":"Commander"    }
self.redis.lpush('leaderauthoritarian_leader', 'czar')
HSET  leaderauthoritarian_leader_description czar { "male":"Czar",         "female":"Czar"         }
self.redis.lpush('leaderauthoritarian_leader', 'despot')
HSET  leaderauthoritarian_leader_description despot { "male":"Despot",       "female":"Despot"       }
self.redis.lpush('leaderauthoritarian_leader', 'general')
HSET  leaderauthoritarian_leader_description general { "male":"General",      "female":"General"      }
self.redis.lpush('leaderauthoritarian_leader', 'inquisitor')
HSET  leaderauthoritarian_leader_description inquisitor { "male":"Inquisitor",   "female":"Inquisitor"   }
self.redis.lpush('leaderauthoritarian_leader', 'leader')
HSET  leaderauthoritarian_leader_description leader { "male":"Leader",       "female":"Leader"       }
self.redis.lpush('leaderauthoritarian_leader', 'lord')
HSET  leaderauthoritarian_leader_description lord { "male":"Lord",         "female":"Lord"         }
self.redis.lpush('leaderauthoritarian_leader', 'master')
HSET  leaderauthoritarian_leader_description master { "male":"Master",       "female":"Master"       }
self.redis.lpush('leaderauthoritarian_leader', 'overlord')
HSET  leaderauthoritarian_leader_description overlord { "male":"Overlord",     "female":"Overlord"     }
self.redis.lpush('leaderauthoritarian_leader', 'overseer')
HSET  leaderauthoritarian_leader_description overseer { "male":"Overseer",     "female":"Overseer"     }
self.redis.lpush('leaderauthoritarian_leader', 'premier')
HSET  leaderauthoritarian_leader_description premier { "male":"Premier",      "female":"Premier"      }
self.redis.lpush('leaderauthoritarian_leader', 'sovereign')
HSET  leaderauthoritarian_leader_description sovereign { "male":"Sovereign",    "female":"Sovereign"    }
self.redis.lpush('leaderauthoritarian_leader', 'steward')
HSET  leaderauthoritarian_leader_description steward { "male":"Steward",      "female":"Steward"      }
self.redis.lpush('leaderauthoritarian_leader', 'supervisor')
HSET  leaderauthoritarian_leader_description supervisor { "male":"Supervisor",   "female":"Supervisor"   }
self.redis.lpush('leaderauthoritarian_leader', 'tyrant')
HSET  leaderauthoritarian_leader_description tyrant { "male":"Tyrant",       "female":"Tyrant"       }
self.redis.lpush('leaderauthoritarian_leader', 'vizier')
HSET  leaderauthoritarian_leader_description vizier { "male":"Vizier",       "female":"Vizier"       }
self.redis.lpush('leaderauthoritarian_leader', 'warlord')
HSET  leaderauthoritarian_leader_description warlord { "male":"Warlord",      "female":"Warlord"      }


self.redis.lpush('leadercommonwealth_leader', 'primeminister')
HSET  leadercommonwealth_leader_description primeminister { "male":"Prime Minister",   "female":"Prime Minister"   }
self.redis.lpush('leadercommonwealth_leader', 'chancellor')
HSET  leadercommonwealth_leader_description chancellor { "male":"Chancellor",   "female":"Chancellor"   }
self.redis.lpush('leadercommonwealth_leader', 'steward')
HSET  leadercommonwealth_leader_description steward { "male":"Steward",      "female":"Steward"      }


self.redis.lpush('leadercommunist_leader', 'primeminister')
HSET  leadercommunist_leader_description primeminister { "male":"Prime Minister",   "female":"Prime Minister"   }
self.redis.lpush('leadercommunist_leader', 'president')
HSET  leadercommunist_leader_description president { "male":"President",   "female":"President"   }
self.redis.lpush('leadercommunist_leader', 'chancellor')
HSET  leadercommunist_leader_description chancellor { "male":"Chancellor",   "female":"Chancellor"   }


self.redis.lpush('leaderconstitutional_leader', 'primeminister')
HSET  leaderconstitutional_leader_description primeminister { "male":"Prime Minister",   "female":"Prime Minister"   }
self.redis.lpush('leaderconstitutional_leader', 'governor')
HSET  leaderconstitutional_leader_description governor { "male":"Governor",      "female":"Governor"      }
self.redis.lpush('leaderconstitutional_leader', 'president')
HSET  leaderconstitutional_leader_description president { "male":"President",   "female":"President"   }


self.redis.lpush('leaderdemocracy_leader', 'primeminister')
HSET  leaderdemocracy_leader_description primeminister { "male":"Prime Minister",   "female":"Prime Minister"   }
self.redis.lpush('leaderdemocracy_leader', 'governor')
HSET  leaderdemocracy_leader_description governor { "male":"Governor",      "female":"Governor"      }
self.redis.lpush('leaderdemocracy_leader', 'president')
HSET  leaderdemocracy_leader_description president { "male":"President",   "female":"President"   }


self.redis.lpush('leaderdictatorship_leader', 'boss')
HSET  leaderdictatorship_leader_description boss { "male":"Boss",         "female":"Boss"         }
self.redis.lpush('leaderdictatorship_leader', 'captain')
HSET  leaderdictatorship_leader_description captain { "male":"Captain",      "female":"Captain"      }
self.redis.lpush('leaderdictatorship_leader', 'chairman')
HSET  leaderdictatorship_leader_description chairman { "male":"Chairman",     "female":"Chairman"     }
self.redis.lpush('leaderdictatorship_leader', 'chief')
HSET  leaderdictatorship_leader_description chief { "male":"Chief",        "female":"Chief"        }
self.redis.lpush('leaderdictatorship_leader', 'commander')
HSET  leaderdictatorship_leader_description commander { "male":"Commander",    "female":"Commander"    }
self.redis.lpush('leaderdictatorship_leader', 'czar')
HSET  leaderdictatorship_leader_description czar { "male":"Czar",         "female":"Czar"         }
self.redis.lpush('leaderdictatorship_leader', 'despot')
HSET  leaderdictatorship_leader_description despot { "male":"Despot",       "female":"Despot"       }
self.redis.lpush('leaderdictatorship_leader', 'general')
HSET  leaderdictatorship_leader_description general { "male":"General",      "female":"General"      }
self.redis.lpush('leaderdictatorship_leader', 'governor')
HSET  leaderdictatorship_leader_description governor { "male":"Governor",     "female":"Governor"     }
self.redis.lpush('leaderdictatorship_leader', 'inquisitor')
HSET  leaderdictatorship_leader_description inquisitor { "male":"Inquisitor",   "female":"Inquisitor"   }
self.redis.lpush('leaderdictatorship_leader', 'leader')
HSET  leaderdictatorship_leader_description leader { "male":"Leader",       "female":"Leader"       }
self.redis.lpush('leaderdictatorship_leader', 'lord')
HSET  leaderdictatorship_leader_description lord { "male":"Lord",         "female":"Lord"         }
self.redis.lpush('leaderdictatorship_leader', 'master')
HSET  leaderdictatorship_leader_description master { "male":"Master",       "female":"Master"       }
self.redis.lpush('leaderdictatorship_leader', 'overlord')
HSET  leaderdictatorship_leader_description overlord { "male":"Overlord",     "female":"Overlord"     }
self.redis.lpush('leaderdictatorship_leader', 'overseer')
HSET  leaderdictatorship_leader_description overseer { "male":"Overseer",     "female":"Overseer"     }
self.redis.lpush('leaderdictatorship_leader', 'premier')
HSET  leaderdictatorship_leader_description premier { "male":"Premier",      "female":"Premier"      }
self.redis.lpush('leaderdictatorship_leader', 'sovereign')
HSET  leaderdictatorship_leader_description sovereign { "male":"Sovereign",    "female":"Sovereign"    }
self.redis.lpush('leaderdictatorship_leader', 'steward')
HSET  leaderdictatorship_leader_description steward { "male":"Steward",      "female":"Steward"      }
self.redis.lpush('leaderdictatorship_leader', 'supervisor')
HSET  leaderdictatorship_leader_description supervisor { "male":"Supervisor",   "female":"Supervisor"   }
self.redis.lpush('leaderdictatorship_leader', 'tyrant')
HSET  leaderdictatorship_leader_description tyrant { "male":"Tyrant",       "female":"Tyrant"       }
self.redis.lpush('leaderdictatorship_leader', 'warlord')
HSET  leaderdictatorship_leader_description warlord { "male":"Warlord",      "female":"Warlord"      }

self.redis.lpush('leaderduchy_leader', 'duchy')
HSET  leaderduchy_leader_description duchy { "male":"Duke",      "female":"Duchess"      }

self.redis.lpush('leaderecclesiastical_leader', 'primeminister')
HSET  leaderecclesiastical_leader_description primeminister { "male":"Prime Minister",   "female":"Prime Minister"   }
self.redis.lpush('leaderecclesiastical_leader', 'pontifex')
HSET  leaderecclesiastical_leader_description pontifex { "male":"Pontifex",   "female":"Pontifex"   }
self.redis.lpush('leaderecclesiastical_leader', 'saint')
HSET  leaderecclesiastical_leader_description saint { "male":"Saint",   "female":"Saint"   }
self.redis.lpush('leaderecclesiastical_leader', 'chief')
HSET  leaderecclesiastical_leader_description chief { "male":"Chief",   "female":"Chief"   }
self.redis.lpush('leaderecclesiastical_leader', 'father')
HSET  leaderecclesiastical_leader_description father { "male":"Father", "female":"Mother"   }
self.redis.lpush('leaderecclesiastical_leader', 'bishop')
HSET  leaderecclesiastical_leader_description bishop { "male":"Bishop",   "female":"Bishop"   }
self.redis.lpush('leaderecclesiastical_leader', 'archbishop')
HSET  leaderecclesiastical_leader_description archbishop { "male":"Archbishop",   "female":"Archbishop"   }
self.redis.lpush('leaderecclesiastical_leader', 'elder')
HSET  leaderecclesiastical_leader_description elder { "male":"Elder",   "female":"Elder"   }
self.redis.lpush('leaderecclesiastical_leader', 'president')
HSET  leaderecclesiastical_leader_description president { "male":"President",   "female":"President"   }
self.redis.lpush('leaderecclesiastical_leader', 'brother')
HSET  leaderecclesiastical_leader_description brother { "male":"Brother",  "female":"Sister"   }
self.redis.lpush('leaderecclesiastical_leader', 'guru')
HSET  leaderecclesiastical_leader_description guru { "male":"Guru",   "female":"Guru"   }
self.redis.lpush('leaderecclesiastical_leader', 'lordchancellor')
HSET  leaderecclesiastical_leader_description lordchancellor { "male":"Lord Chancellor",   "female":"Lady Chancellor"   }
self.redis.lpush('leaderecclesiastical_leader', 'lord')
HSET  leaderecclesiastical_leader_description lord { "male":"Lord", "female":"Lady"  }
self.redis.lpush('leaderecclesiastical_leader', 'chancellor')
HSET  leaderecclesiastical_leader_description chancellor { "male":"Chancellor",   "female":"Chancellor"   }
self.redis.lpush('leaderecclesiastical_leader', 'steward')
HSET  leaderecclesiastical_leader_description steward { "male":"Steward",      "female":"Steward"      }
self.redis.lpush('leaderecclesiastical_leader', 'cardinal')
HSET  leaderecclesiastical_leader_description cardinal { "male":"Cardinal",   "female":"Cardinal"   }
self.redis.lpush('leaderecclesiastical_leader', 'caliph')
HSET  leaderecclesiastical_leader_description caliph { "male":"Caliph",   "female":"Caliph"   }


self.redis.lpush('leaderemirate_leader', 'primeminister')
HSET  leaderemirate_leader_description primeminister { "male":"Prime Minister",   "female":"Prime Minister"   }
self.redis.lpush('leaderemirate_leader', 'saint')
HSET  leaderemirate_leader_description saint { "male":"Saint",   "female":"Saint"   }
self.redis.lpush('leaderemirate_leader', 'chief')
HSET  leaderemirate_leader_description chief { "male":"Chief",   "female":"Chief"   }
self.redis.lpush('leaderemirate_leader', 'father')
HSET  leaderemirate_leader_description father { "male":"Father", "female":"Mother"   }
self.redis.lpush('leaderemirate_leader', 'bishop')
HSET  leaderemirate_leader_description bishop { "male":"Bishop",   "female":"Bishop"   }
self.redis.lpush('leaderemirate_leader', 'archbishop')
HSET  leaderemirate_leader_description archbishop { "male":"Archbishop",   "female":"Archbishop"   }
self.redis.lpush('leaderemirate_leader', 'elder')
HSET  leaderemirate_leader_description elder { "male":"Elder",   "female":"Elder"   }
self.redis.lpush('leaderemirate_leader', 'president')
HSET  leaderemirate_leader_description president { "male":"President",   "female":"President"   }
self.redis.lpush('leaderemirate_leader', 'brother')
HSET  leaderemirate_leader_description brother { "male":"Brother",  "female":"Sister"   }
self.redis.lpush('leaderemirate_leader', 'guru')
HSET  leaderemirate_leader_description guru { "male":"Guru",   "female":"Guru"   }
self.redis.lpush('leaderemirate_leader', 'steward')
HSET  leaderemirate_leader_description steward { "male":"Steward",      "female":"Steward"      }
self.redis.lpush('leaderemirate_leader', 'lordchancellor')
HSET  leaderemirate_leader_description lordchancellor { "male":"Lord Chancellor",   "female":"Lady Chancellor"   }
self.redis.lpush('leaderemirate_leader', 'lord')
HSET  leaderemirate_leader_description lord { "male":"Lord", "female":"Lady"  }
self.redis.lpush('leaderemirate_leader', 'chancellor')
HSET  leaderemirate_leader_description chancellor { "male":"Chancellor",   "female":"Chancellor"   }
self.redis.lpush('leaderemirate_leader', 'cardinal')
HSET  leaderemirate_leader_description cardinal { "male":"Cardinal",   "female":"Cardinal"   }
self.redis.lpush('leaderemirate_leader', 'caliph')
HSET  leaderemirate_leader_description caliph { "male":"Caliph",   "female":"Caliph"   }


self.redis.lpush('leaderfederation_leader', 'commander')
HSET  leaderfederation_leader_description commander { "male":"Commander",    "female":"Commander"    }
self.redis.lpush('leaderfederation_leader', 'general')
HSET  leaderfederation_leader_description general { "male":"General",      "female":"General"      }
self.redis.lpush('leaderfederation_leader', 'governor')
HSET  leaderfederation_leader_description governor { "male":"Governor",      "female":"Governor"      }
self.redis.lpush('leaderfederation_leader', 'primeminister')
HSET  leaderfederation_leader_description primeminister { "male":"Prime Minister",   "female":"Prime Minister"   }
self.redis.lpush('leaderfederation_leader', 'president')
HSET  leaderfederation_leader_description president { "male":"President",   "female":"President"   }
self.redis.lpush('leaderfederation_leader', 'steward')
HSET  leaderfederation_leader_description steward { "male":"Steward",      "female":"Steward"      }

self.redis.lpush('leadergang_leader', 'gangleader')
HSET  leadergang_leader_description gangleader { "male":"GangLeader",    "female":"Gang Leader"     }
self.redis.lpush('leadergang_leader', 'kingpin')
HSET  leadergang_leader_description kingpin { "male":"Kingpin",    "female":"Kingpin"     }

self.redis.lpush('leaderguild_leader', 'guildmaster')
HSET  leaderguild_leader_description guildmaster { "male":"Guildmaster",    "female":"Guildmaster"     }

self.redis.lpush('leadermonarchy_leader', 'king')
HSET  leadermonarchy_leader_description king { "male":"King",    "female":"Queen"     }
self.redis.lpush('leadermonarchy_leader', 'emperor')
HSET  leadermonarchy_leader_description emperor { "male":"Emperor", "female":"Empress"   }
self.redis.lpush('leadermonarchy_leader', 'raja')
HSET  leadermonarchy_leader_description raja { "male":"Raja",    "female":"Rani"      }
self.redis.lpush('leadermonarchy_leader', 'sultan')
HSET  leadermonarchy_leader_description sultan { "male":"Sultan",  "female":"Sultana"   }
self.redis.lpush('leadermonarchy_leader', 'shah')
HSET  leadermonarchy_leader_description shah { "male":"Shah",    "female":"Shahbanu"  }
self.redis.lpush('leadermonarchy_leader', 'prince')
HSET  leadermonarchy_leader_description prince { "male":"Prince",  "female":"Princess"  }

self.redis.lpush('leaderoligarchy_leader', 'commander')
HSET  leaderoligarchy_leader_description commander { "male":"Commander",    "female":"Commander"    }
self.redis.lpush('leaderoligarchy_leader', 'general')
HSET  leaderoligarchy_leader_description general { "male":"General",      "female":"General"      }
self.redis.lpush('leaderoligarchy_leader', 'governor')
HSET  leaderoligarchy_leader_description governor { "male":"Governor",      "female":"Governor"      }
self.redis.lpush('leaderoligarchy_leader', 'primeminister')
HSET  leaderoligarchy_leader_description primeminister { "male":"Prime Minister",   "female":"Prime Minister"   }
self.redis.lpush('leaderoligarchy_leader', 'president')
HSET  leaderoligarchy_leader_description president { "male":"President",   "female":"President"   }


self.redis.lpush('leaderparliamentary_leader', 'commander')
HSET  leaderparliamentary_leader_description commander { "male":"Commander",    "female":"Commander"    }
self.redis.lpush('leaderparliamentary_leader', 'general')
HSET  leaderparliamentary_leader_description general { "male":"General",      "female":"General"      }
self.redis.lpush('leaderparliamentary_leader', 'governor')
HSET  leaderparliamentary_leader_description governor { "male":"Governor",      "female":"Governor"      }
self.redis.lpush('leaderparliamentary_leader', 'primeminister')
HSET  leaderparliamentary_leader_description primeminister { "male":"Prime Minister",   "female":"Prime Minister"   }
self.redis.lpush('leaderparliamentary_leader', 'steward')
HSET  leaderparliamentary_leader_description steward { "male":"Steward",      "female":"Steward"      }
self.redis.lpush('leaderparliamentary_leader', 'president')
HSET  leaderparliamentary_leader_description president { "male":"President",   "female":"President"   }


self.redis.lpush('leaderrepublic_leader', 'commander')
HSET  leaderrepublic_leader_description commander { "male":"Commander",    "female":"Commander"    }
self.redis.lpush('leaderrepublic_leader', 'general')
HSET  leaderrepublic_leader_description general { "male":"General",      "female":"General"      }
self.redis.lpush('leaderrepublic_leader', 'governor')
HSET  leaderrepublic_leader_description governor { "male":"Governor",      "female":"Governor"      }
self.redis.lpush('leaderrepublic_leader', 'primeminister')
HSET  leaderrepublic_leader_description primeminister { "male":"Prime Minister",   "female":"Prime Minister"   }
self.redis.lpush('leaderrepublic_leader', 'president')
HSET  leaderrepublic_leader_description president { "male":"President",   "female":"President"   }


self.redis.lpush('leadertheocracy_leader', 'primeminister')
HSET  leadertheocracy_leader_description primeminister { "male":"Prime Minister",   "female":"Prime Minister"   }
self.redis.lpush('leadertheocracy_leader', 'saint')
HSET  leadertheocracy_leader_description saint { "male":"Saint",   "female":"Saint"   }
self.redis.lpush('leadertheocracy_leader', 'chief')
HSET  leadertheocracy_leader_description chief { "male":"Chief",   "female":"Chief"   }
self.redis.lpush('leadertheocracy_leader', 'father')
HSET  leadertheocracy_leader_description father { "male":"Father", "female":"Mother"   }
self.redis.lpush('leadertheocracy_leader', 'bishop')
HSET  leadertheocracy_leader_description bishop { "male":"Bishop",   "female":"Bishop"   }
self.redis.lpush('leadertheocracy_leader', 'archbishop')
HSET  leadertheocracy_leader_description archbishop { "male":"Archbishop",   "female":"Archbishop"   }
self.redis.lpush('leadertheocracy_leader', 'elder')
HSET  leadertheocracy_leader_description elder { "male":"Elder",   "female":"Elder"   }
self.redis.lpush('leadertheocracy_leader', 'president')
HSET  leadertheocracy_leader_description president { "male":"President",   "female":"President"   }
self.redis.lpush('leadertheocracy_leader', 'brother')
HSET  leadertheocracy_leader_description brother { "male":"Brother",  "female":"Sister"   }
self.redis.lpush('leadertheocracy_leader', 'guru')
HSET  leadertheocracy_leader_description guru { "male":"Guru",   "female":"Guru"   }
self.redis.lpush('leadertheocracy_leader', 'lordchancellor')
HSET  leadertheocracy_leader_description lordchancellor { "male":"Lord Chancellor",   "female":"Lady Chancellor"   }
self.redis.lpush('leadertheocracy_leader', 'steward')
HSET  leadertheocracy_leader_description steward { "male":"Steward",      "female":"Steward"      }
self.redis.lpush('leadertheocracy_leader', 'lord')
HSET  leadertheocracy_leader_description lord { "male":"Lord", "female":"Lady"  }
self.redis.lpush('leadertheocracy_leader', 'chancellor')
HSET  leadertheocracy_leader_description chancellor { "male":"Chancellor",   "female":"Chancellor"   }
self.redis.lpush('leadertheocracy_leader', 'cardinal')
HSET  leadertheocracy_leader_description cardinal { "male":"Cardinal",   "female":"Cardinal"   }
self.redis.lpush('leadertheocracy_leader', 'caliph')
HSET  leadertheocracy_leader_description caliph { "male":"Caliph",   "female":"Caliph"   }


self.redis.lpush('leadertotalitarian_leader', 'boss')
HSET  leadertotalitarian_leader_description boss { "male":"Boss",         "female":"Boss"         }
self.redis.lpush('leadertotalitarian_leader', 'captain')
HSET  leadertotalitarian_leader_description captain { "male":"Captain",      "female":"Captain"      }
self.redis.lpush('leadertotalitarian_leader', 'chairman')
HSET  leadertotalitarian_leader_description chairman { "male":"Chairman",     "female":"Chairman"     }
self.redis.lpush('leadertotalitarian_leader', 'chief')
HSET  leadertotalitarian_leader_description chief { "male":"Chief",        "female":"Chief"        }
self.redis.lpush('leadertotalitarian_leader', 'commander')
HSET  leadertotalitarian_leader_description commander { "male":"Commander",    "female":"Commander"    }
self.redis.lpush('leadertotalitarian_leader', 'czar')
HSET  leadertotalitarian_leader_description czar { "male":"Czar",         "female":"Czar"         }
self.redis.lpush('leadertotalitarian_leader', 'despot')
HSET  leadertotalitarian_leader_description despot { "male":"Despot",       "female":"Despot"       }
self.redis.lpush('leadertotalitarian_leader', 'general')
HSET  leadertotalitarian_leader_description general { "male":"General",      "female":"General"      }
self.redis.lpush('leadertotalitarian_leader', 'governor')
HSET  leadertotalitarian_leader_description governor { "male":"Governor",     "female":"Governor"     }
self.redis.lpush('leadertotalitarian_leader', 'inquisitor')
HSET  leadertotalitarian_leader_description inquisitor { "male":"Inquisitor",   "female":"Inquisitor"   }
self.redis.lpush('leadertotalitarian_leader', 'leader')
HSET  leadertotalitarian_leader_description leader { "male":"Leader",       "female":"Leader"       }
self.redis.lpush('leadertotalitarian_leader', 'lord')
HSET  leadertotalitarian_leader_description lord { "male":"Lord",         "female":"Lord"         }
self.redis.lpush('leadertotalitarian_leader', 'master')
HSET  leadertotalitarian_leader_description master { "male":"Master",       "female":"Master"       }
self.redis.lpush('leadertotalitarian_leader', 'overlord')
HSET  leadertotalitarian_leader_description overlord { "male":"Overlord",     "female":"Overlord"     }
self.redis.lpush('leadertotalitarian_leader', 'overseer')
HSET  leadertotalitarian_leader_description overseer { "male":"Overseer",     "female":"Overseer"     }
self.redis.lpush('leadertotalitarian_leader', 'premier')
HSET  leadertotalitarian_leader_description premier { "male":"Premier",      "female":"Premier"      }
self.redis.lpush('leadertotalitarian_leader', 'sovereign')
HSET  leadertotalitarian_leader_description sovereign { "male":"Sovereign",    "female":"Sovereign"    }
self.redis.lpush('leadertotalitarian_leader', 'steward')
HSET  leadertotalitarian_leader_description steward { "male":"Steward",      "female":"Steward"      }
self.redis.lpush('leadertotalitarian_leader', 'supervisor')
HSET  leadertotalitarian_leader_description supervisor { "male":"Supervisor",   "female":"Supervisor"   }
self.redis.lpush('leadertotalitarian_leader', 'tyrant')
HSET  leadertotalitarian_leader_description tyrant { "male":"Tyrant",       "female":"Tyrant"       }
self.redis.lpush('leadertotalitarian_leader', 'warlord')
HSET  leadertotalitarian_leader_description warlord { "male":"Warlord",      "female":"Warlord"      }

self.redis.lpush('leadercouncilmanager_leader', 'councilman')
HSET  leadercouncilmanager_leader_description councilman { "male":"Councilman",      "female":"Councilwoman"      }
self.redis.lpush('leadercouncilmanager_leader', 'manager')
HSET  leadercouncilmanager_leader_description manager { "male":"Manager",      "female":"Manager"      }

self.redis.lpush('leadermayorcouncil_leader', 'councilman')
HSET  leadermayorcouncil_leader_description councilman { "male":"Councilman",      "female":"Councilwoman"      }
self.redis.lpush('leadermayorcouncil_leader', 'mayor')
HSET  leadermayorcouncil_leader_description mayor { "male":"Mayor",      "female":"Mayor"      }

self.redis.lpush('leadercommission_leader', 'commissioner')
HSET  leadercommission_leader_description commissioner { "male":"Commissioner",      "female":"Commissioner"      }

self.redis.lpush('leadertownmeeting_leader', 'elder')
HSET  leadertownmeeting_leader_description elder { "male":"Elder",      "female":"Elder"      }

self.redis.lpush('leadermagistrate_leader', 'magistrate')
HSET  leadermagistrate_leader_description magistrate { "male":"Magistrate",      "female":"Magistrate"      }

self.redis.lpush('leaderunion_leader', 'president')
HSET  leaderunion_leader_description president { "male":"President",   "female":"President"   }

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#leader_kind city
#
#
#    </govtypes>
#<secondarypower>
#    <plot>openly assists</plot>
#    <plot>openly denounces</plot>
#    <plot>quietly denounces</plot>
#    <plot>quietly assists</plot>
#
#    <power type:"a dragon" subplot_chance:"50">
#        <subplot>wishing to enslave the city</subplot>
#        <subplot>watching out for the common man</subplot>
#        <subplot>despising the current leader</subplot>
#        <subplot>agreeing with the current leader</subplot>
#    </power>
#    <power type:"a wizard" subplot_chance:"50">
#        <subplot>attempting to attain immortality</subplot>
#        <subplot>watching out for the common man</subplot>
#        <subplot>despising the current leader</subplot>
#        <subplot>agreeing with the current leader</subplot>
#    </power>
#    <power type:"a merchant guild" subplot_chance:"50">
#        <subplot>attempting to buy influence</subplot>
#        <subplot>attempting to sell influence</subplot>
#        <subplot>pushing for war with trade adversary</subplot>
#        <subplot>pushing to open trade with adversary</subplot>
#    </power>
#    <power type:"an elected representative" subplot_chance:"50">
#        <subplot>using position for personal gain</subplot>
#        <subplot>amassing power</subplot>
#    </power>
#    <power type:"an advisor" subplot_chance:"50">
#        <subplot>pulling strings for personal gain</subplot>
#        <subplot>blackmailing the government</subplot>
#        <subplot>working for enemies</subplot>
#    </power>
#    <power type:"a prophet" subplot_chance:"50">
#        <subplot>attempting to lead religious revolution</subplot>
#        <subplot>denying legitimacy of leading power</subplot>
#        <subplot>calling for genocide of a minority</subplot>
#    </power>
#    <power type:"a thieves guild" subplot_chance:"50">
#        <subplot>moving to assert black market dominance</subplot>
#        <subplot>backing leading power for leniency</subplot>
#    </power>
#    <power type:"traveler" subplot_chance:"50">
#        <subplot>looking to bring justice</subplot>
#        <subplot>looking to overthrow the government</subplot>
#    </power>
#    <power type:"an ex-blacksmith" subplot_chance:"50">
#        <subplot>plotting to overthrow the corrupt leadership for personal gain</subplot>
#        <subplot>being blackmailed by a guild</subplot>
#        <subplot>pulling strings with a trade adversary</subplot>
#    </power>
#    <power type:"a barbarian" subplot_chance:"50">
#        <subplot>plotting to start war with another nation</subplot>
#        <subplot>being manipulated by the denizens of the city whore house</subplot>
#        <subplot>wishing to rule with a violent, iron fist</subplot>
#    </power>
#    <power type:"a recluse" subplot_chance:"50">
#        <subplot>pulling strings for personal gain</subplot>
#        <subplot>a fiend in disguise</subplot>
#        <subplot>an angel in disguise</subplot>
#        <subplot>a dragon in disguise</subplot>
#        <subplot>a god in disguise</subplot>
#        <subplot>a fiend that secretly looks out for the good of the common man</subplot>
#        <subplot>an angel that seeks to enslave the common man</subplot>
#    </power>
#</secondarypower>
#</data>
#        <right>
#            <option>by forgery</option>
#            <option>by divine will</option>
#            <option>by consensus</option>
#            <option>by constitution</option>
#            <option>by hereditary succession</option>
#            <option>by election</option>
#            <option>by appointment</option>
#            <option>by force</option>
#            <option>by revolution</option>
#            <option>by foreign imposition</option>
#        </right>
#
#
#        <length> <!-- The King has been in power-->
#            <option>for mere hours</option>
#            <option>for mere days</option>
#            <option>for a few months</option>
#            <option>for years</option>
#            <option>for several years</option>
#            <option>for many years</option>
#            <option>for decades</option>
#            <option>for several decades</option>
#            <option>far longer than should be allowed</option>
#        </length>
#        <maintained><!-- and that power is maintained __________ -->
#            <option >through the tip of a sword</option>
#            <option >through random violence</option>
#            <option >through the ignorance of the plebeian society</option>
#            <option >through vague threats and a constant state of fear</option>
#            <option >through financial oppression</option>
#            <option >by secret police raiding homes in the dead of night</option>
#            <option >by strict laws and corrupt guards</option>
#            <option >by strict laws and incorruptible guards</option>
#            <option >by draconian laws and underpaid guards</option>
#            <option >through spying and assassination</option>
#            <option >through a fair and just legal system</option>
#            <option >through the writ of law</option>
#            <option >through a knowledgeable and just populace</option>
#            <option >through vague promises and a constant state of hope</option>
#            <option >through sheer willpower</option>
#            <option >through the acclaim of the nobles</option>
#            <option >by unwavering supporters</option>
#            <option >through the support of merchant groups</option>
#        </maintained>
#
#        <influencereason>
#            <option >riots in the region</option>
#            <option >food shortages in the region</option>
#            <option >racial tensions</option>
#            <option >a thwarted assassination attempt</option>
#        </influencereason>
#    </feature>
#
