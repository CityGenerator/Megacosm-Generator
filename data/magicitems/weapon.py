#

self.redis.lpush('magicitem_kind', 'weapon')

#materialpart:  "the _____ of the ___ is made of steel"
self.redis.lpush('weapon_category', 'sword')
self.redis.hset('weapon_category_description', 'sword', '{"name":"sword",        "materialpart":"blade"    }')
self.redis.lpush('weapon_category', 'dagger')
self.redis.hset('weapon_category_description', 'dagger', '{"name":"dagger",       "materialpart":"blade"    }')
self.redis.lpush('weapon_category', 'axe')
self.redis.hset('weapon_category_description', 'axe', '{"name":"axe",          "materialpart":"head"     }')
self.redis.lpush('weapon_category', 'mace')
self.redis.hset('weapon_category_description', 'mace', '{"name":"mace",         "materialpart":"head"     }')
self.redis.lpush('weapon_category', 'bow')
self.redis.hset('weapon_category_description', 'bow', '{"name":"bow",          "materialpart":"handle"    }')
self.redis.lpush('weapon_category', 'crossbow')
self.redis.hset('weapon_category_description', 'crossbow', '{"name":"crossbow",     "materialpart":"stock"    }')
self.redis.lpush('weapon_category', 'quarterstaff')
self.redis.hset('weapon_category_description', 'quarterstaff', '{"name":"quarterstaff", "materialpart":"shaft"    }')
self.redis.lpush('weapon_category', 'polearm')
self.redis.hset('weapon_category_description', 'polearm', '{"name":"polearm",      "materialpart":"tip"      }')

# the sharp sword of ________ will occasionally slice through anything and __________________________________.
# the sharp sword of the bull will occasionally slice through anything and grants the user unnatural strength.
SET  weapon_ability_chance 20
self.redis.lpush('weapon_ability', 'bull')
self.redis.hset('weapon_ability_description', 'bull', '{"name":"the bull",  "description":"grants the user unnatural strength"     }')
self.redis.lpush('weapon_ability', 'grace')
self.redis.hset('weapon_ability_description', 'grace', '{"name":"grace",     "description":"grants the user an unnatural grace"     }')
self.redis.lpush('weapon_ability', 'toughness')
self.redis.hset('weapon_ability_description', 'toughness', '{"name":"toughness", "description":"grants the user unnatural constitution" }')
self.redis.lpush('weapon_ability', 'owl')
self.redis.hset('weapon_ability_description', 'owl', '{"name":"the owl",   "description":"grants the user unnatural insight"      }')
self.redis.lpush('weapon_ability', 'genius')
self.redis.hset('weapon_ability_description', 'genius', '{"name":"genius",    "description":"grants the user unnatural intelligence" }')
self.redis.lpush('weapon_ability', 'charm')
self.redis.hset('weapon_ability_description', 'charm', '{"name":"charm",     "description":"grants the user unnatural charisma"     }')
self.redis.lpush('weapon_ability', 'holy')
self.redis.hset('weapon_ability_description', 'holy', '{"name":"the holy",  "description":"may cause fear in the undead"           }')
self.redis.lpush('weapon_ability', 'defense')
self.redis.hset('weapon_ability_description', 'defense', '{"name":"defense",   "description":"may protect the user from some attacks" }')
self.redis.lpush('weapon_ability', 'returning')
self.redis.hset('weapon_ability_description', 'returning', '{"name":"returning", "description":"will return to the user if thrown"      }')
        
# the _____ sword of the bull  _______________________________________ and grants the user unnatural strength.
# the sharp sword of the bull will occasionally slice through anything and grants the user unnatural strength.
self.redis.lpush('weapon_effect', 'sharp')
self.redis.hset('weapon_effect_description', 'sharp', '{"name":"sharp",     "description":"will occasionally slice through anything"                  }')
self.redis.lpush('weapon_effect', 'painful')
self.redis.hset('weapon_effect_description', 'painful', '{"name":"painful",   "description":"causes a traumatic jolt of unexpected pain"                }')
self.redis.lpush('weapon_effect', 'magical')
self.redis.hset('weapon_effect_description', 'magical', '{"name":"magical",   "description":"causes an unexpected jolt of magical energy"               }')
self.redis.lpush('weapon_effect', 'flaming')
self.redis.hset('weapon_effect_description', 'flaming', '{"name":"flaming",   "description":"causes a small flare of fire that burns the target"        }')
self.redis.lpush('weapon_effect', 'electric')
self.redis.hset('weapon_effect_description', 'electric', '{"name":"electric",  "description":"causes a small surge of electricity that stuns the target" }')
self.redis.lpush('weapon_effect', 'frigid')
self.redis.hset('weapon_effect_description', 'frigid', '{"name":"frigid",    "description":"causes a mind numbing cold that chills the target"         }')
self.redis.lpush('weapon_effect', 'acidic')
self.redis.hset('weapon_effect_description', 'acidic', '{"name":"acidic",    "description":"causes a wound that is drenched in acid"                   }')
self.redis.lpush('weapon_effect', 'sonic')
self.redis.hset('weapon_effect_description', 'sonic', '{"name":"sonic",     "description":"causes a deafening roar that only affects the target"      }')
self.redis.lpush('weapon_effect', 'exploding')
self.redis.hset('weapon_effect_description', 'exploding', '{"name":"exploding", "description":"causes a concussive blast against the target"              }')

SET  weapon_flaw_chance 30
# This sword is rather distinctive due to a[n] ___________ on the weapon.
self.redis.lpush('weapon_flaw', 'chip')
self.redis.hset('weapon_flaw_description', 'chip', '{"name":"small chip",         "description":""  }')
self.redis.lpush('weapon_flaw', 'missing')
self.redis.hset('weapon_flaw_description', 'missing', '{"name":"missing decoration", "description":""  }')
self.redis.lpush('weapon_flaw', 'crack')
self.redis.hset('weapon_flaw_description', 'crack', '{"name":"crack",              "description":""  }')
self.redis.lpush('weapon_flaw', 'discolored')
self.redis.hset('weapon_flaw_description', 'discolored', '{"name":"discolored spot",    "description":""  }')
self.redis.lpush('weapon_flaw', 'blackened')
self.redis.hset('weapon_flaw_description', 'blackened', '{"name":"blackened spot",     "description":""  }')
self.redis.lpush('weapon_flaw', 'bloodstained')
self.redis.hset('weapon_flaw_description', 'bloodstained', '{"name":"bloodstain",         "description":""  }')

# When _____________, the weapon emits a faint glow
self.redis.lpush('weapon_visualcause', 'orc')
self.redis.hset('weapon_visualcause_description', 'orc', '{"name":"orc",      "description":"exposed to orcs"         }')
self.redis.lpush('weapon_visualcause', 'darkness')
self.redis.hset('weapon_visualcause_description', 'darkness', '{"name":"darkness", "description":"held in the darkness"    }')
self.redis.lpush('weapon_visualcause', 'blood')
self.redis.hset('weapon_visualcause_description', 'blood', '{"name":"blood",    "description":"covered with blood"    }')
self.redis.lpush('weapon_visualcause', 'danger')
self.redis.hset('weapon_visualcause_description', 'danger', '{"name":"danger",    "description":"danger is near"    }')

# When exposed to Orcs, the weapon  ____________________.
SET  weapon_visualeffect_chance 10
self.redis.lpush('weapon_visualeffect', 'sparkles')
self.redis.hset('weapon_visualeffect_description', 'sparkles', '{"name":"sparkles",    "description":"emits a faint sparkle"                   }')
self.redis.lpush('weapon_visualeffect', 'glows')
self.redis.hset('weapon_visualeffect_description', 'glows', '{"name":"glows",       "description":"emits a bright glow"                     }')
self.redis.lpush('weapon_visualeffect', 'redpulse')
self.redis.hset('weapon_visualeffect_description', 'redpulse', '{"name":"red pulse",    "description":"pulses red in time with your heartbeat" }')
self.redis.lpush('weapon_visualeffect', 'electricity')
self.redis.hset('weapon_visualeffect_description', 'electricity', '{"name":"electricity", "description":"crackles with visible electricity"       }')

# the sword is made of __________
self.redis.lpush('weapon_material', 'coldiron')
self.redis.hset('weapon_material_description', 'coldiron', '{"name":"cold iron",       "description":"beautiful cold steel"    }')
self.redis.lpush('weapon_material', 'steel')
self.redis.hset('weapon_material_description', 'steel', '{"name":"steel",       "description":"high quality steel"          }')
self.redis.lpush('weapon_material', 'crystal')
self.redis.hset('weapon_material_description', 'crystal', '{"name":"crystal",     "description":"a strange crystal"           }')
self.redis.lpush('weapon_material', 'bone')
self.redis.hset('weapon_material_description', 'bone', '{"name":"bone",        "description":"a specially treated bone"    }')

# and the blade is decorated with __________________
SET  weapon_decoration_chance 10
self.redis.lpush('weapon_decoration', 'flames')
self.redis.hset('weapon_decoration_description', 'flames', '{"name":"flames",   "description":"streaks of red and yellow which glisten like flames"  }')
self.redis.lpush('weapon_decoration', 'inlay')
self.redis.hset('weapon_decoration_description', 'inlay', '{"name":"inlay",    "description":"beautiful gold and silver inlays"                     }')
self.redis.lpush('weapon_decoration', 'carvings')
self.redis.hset('weapon_decoration_description', 'carvings', '{"name":"carvings", "description":"intricate carvings"                                   }')
self.redis.lpush('weapon_decoration', 'writing')
self.redis.hset('weapon_decoration_description', 'writing', '{"name":"writing",  "description":"beautiful writing in a strange language"              }')
self.redis.lpush('weapon_decoration', 'runes')
self.redis.hset('weapon_decoration_description', 'runes', '{"name":"runes",  "description":"strange and cryptic runes"                              }')

#The __________ is a 

# painful sword[ of the bull]
self.redis.lpush('weapon_name_template', '{{ params.effect_description[\'name\'] }} {{ params.category_description[\'name\']}}{%if params.ability_description%} of {{params.ability_description[\'name\']}}{%endif%}')
# Bob\'s frigid sword
self.redis.lpush('weapon_name_template', '{{ params.npc.name.shortname }}\'s {{ params.category_description[\'name\'] }}')
# Sharp sword of Bob
self.redis.lpush('weapon_name_template', '{{ params.effect_description[\'name\'] }} {{ params.category_description[\'name\'] }} of {{ params.npc.name.shortname }}')
# Sword of Bob
self.redis.lpush('weapon_name_template', '{{ params.category_description[\'name\'] }} of {{ params.npc.name.shortname }}')

