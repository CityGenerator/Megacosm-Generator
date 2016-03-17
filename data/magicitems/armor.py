#

self.redis.lpush('magicitem_kind', 'armor')


self.redis.lpush('armor_category', 'leatherarmor')
HSET  armor_category_description leatherarmor   {"name":"leather armor",     "materialpart":"chest" }
self.redis.lpush('armor_category', 'breastplate')
HSET  armor_category_description breastplate    {"name":"breastplate",       "materialpart":"chest" }
self.redis.lpush('armor_category', 'chainmail')
HSET  armor_category_description chainmail      {"name":"chainmail",         "materialpart":"trim" }
self.redis.lpush('armor_category', 'hidearmor')
HSET  armor_category_description hidearmor      {"name":"hide armor",        "materialpart":"chest" }
self.redis.lpush('armor_category', 'platearmor')
HSET  armor_category_description platearmor     {"name":"plate armor",       "materialpart":"chest" }
self.redis.lpush('armor_category', 'shield')
HSET  armor_category_description shield         {"name":"shield",            "materialpart":"front" }
self.redis.lpush('armor_category', 'helm')
HSET  armor_category_description helm           {"name":"helm",              "materialpart":"top"   }
self.redis.lpush('armor_category', 'gauntlets')
HSET  armor_category_description gauntlets      {"name":"gauntlet set",      "materialpart":"wrist" }
self.redis.lpush('armor_category', 'bracers')
HSET  armor_category_description bracers        {"name":"bracer set",        "materialpart":"forearm" }



SET   armor_ability_chance 20
self.redis.lpush('armor_ability', 'shock')
HSET  armor_ability_description shock           {"name":"shock",        "description":"has a chance of stunning an attacker" }
self.redis.lpush('armor_ability', 'glory')
HSET  armor_ability_description glory           {"name":"glory",        "description":"emboldens comrades in battle" }
self.redis.lpush('armor_ability', 'shadows')
HSET  armor_ability_description shadows         {"name":"the shadows",  "description":"makes the wearer virtually undetectable in shadows" }
self.redis.lpush('armor_ability', 'grace')
HSET  armor_ability_description grace           {"name":"grace",        "description":"grants the user an unnatural grace"     }
self.redis.lpush('armor_ability', 'toughness')
HSET  armor_ability_description toughness       {"name":"toughness",    "description":"grants the user unnatural constitution" }
self.redis.lpush('armor_ability', 'holy')
HSET  armor_ability_description holy            {"name":"the holy",     "description":"may cause fear in the undead"           }
self.redis.lpush('armor_ability', 'defense')
HSET  armor_ability_description defense         {"name":"defense",      "description":"may protect the user from some attacks" }

self.redis.lpush('armor_effect', 'muffled')
HSET  armor_effect_description muffled          {"name":"muffled",          "description":"allows the wearer to move more quietly than otherwise possible" }
self.redis.lpush('armor_effect', 'slick')
HSET  armor_effect_description slick            {"name":"slick",            "description":"cause the wearer to be difficult to grasp" }
self.redis.lpush('armor_effect', 'deflecting')
HSET  armor_effect_description deflecting       {"name":"deflecting",       "description":"deflects some projectiles that would otherwise hit" }
self.redis.lpush('armor_effect', 'ringing')
HSET  armor_effect_description ringing          {"name":"ringing",          "description":"causes a deafening roar when struck"      }




SET   armor_flaw_chance 30

self.redis.lpush('armor_flaw', 'dent')
HSET  armor_flaw_description dent               {"name":"dent", "description":"" }
self.redis.lpush('armor_flaw', 'ding')
HSET  armor_flaw_description ding               {"name":"ding", "description":"" }
self.redis.lpush('armor_flaw', 'chip')
HSET  armor_flaw_description chip               {"name":"small chip",         "description":""  }
self.redis.lpush('armor_flaw', 'missing')
HSET  armor_flaw_description missing            {"name":"missing decoration", "description":""  }
self.redis.lpush('armor_flaw', 'crack')
HSET  armor_flaw_description crack              {"name":"crack",              "description":""  }
self.redis.lpush('armor_flaw', 'discolored')
HSET  armor_flaw_description discolored         {"name":"discolored spot",    "description":""  }
self.redis.lpush('armor_flaw', 'blackened')
HSET  armor_flaw_description blackened          {"name":"blackened spot",     "description":""  }
self.redis.lpush('armor_flaw', 'bloodstained')
HSET  armor_flaw_description bloodstained       {"name":"bloodstain",         "description":""  }


# When _____________, the armor emits a faint glow
self.redis.lpush('armor_visualcause', 'orc')
HSET  armor_visualcause_description orc      {"name":"orc",      "description":"exposed to orcs"         }
self.redis.lpush('armor_visualcause', 'darkness')
HSET  armor_visualcause_description darkness {"name":"darkness", "description":"worn in the darkness"    }
self.redis.lpush('armor_visualcause', 'blood')
HSET  armor_visualcause_description blood    {"name":"blood",    "description":"covered with blood"    }
self.redis.lpush('armor_visualcause', 'danger')
HSET  armor_visualcause_description danger   {"name":"danger",    "description":"danger is near"    }


SET   armor_visualeffect_chance 10
self.redis.lpush('armor_visualeffect', 'sparkles')
HSET  armor_visualeffect_description sparkles    {"name":"sparkles",    "description":"emits a faint sparkle"                   }
self.redis.lpush('armor_visualeffect', 'glows')
HSET  armor_visualeffect_description glows       {"name":"glows",       "description":"emits a bright glow"                     }
self.redis.lpush('armor_visualeffect', 'redpulse')
HSET  armor_visualeffect_description redpulse    {"name":"red pulse",    "description":"pulses red in time with your heartbeat" }
self.redis.lpush('armor_visualeffect', 'electricity')
HSET  armor_visualeffect_description electricity {"name":"electricity", "description":"crackles with visible electricity"       }



self.redis.lpush('armor_material', 'coldiron')
HSET  armor_material_description coldiron {"name":"cold iron",       "description":"beautiful cold steel"    }
self.redis.lpush('armor_material', 'steel')
HSET  armor_material_description steel    {"name":"steel",       "description":"high quality steel"          }
self.redis.lpush('armor_material', 'crystal')
HSET  armor_material_description crystal  {"name":"crystal",     "description":"a strange crystal"           }
self.redis.lpush('armor_material', 'bone')
HSET  armor_material_description bone     {"name":"bone",        "description":"a specially treated bone"    }


SET   armor_decoration_chance 10

self.redis.lpush('armor_decoration', 'flames')
HSET  armor_decoration_description flames   {"name":"flames",   "description":"streaks of red and yellow which glisten like flames"  }
self.redis.lpush('armor_decoration', 'inlay')
HSET  armor_decoration_description inlay    {"name":"inlay",    "description":"beautiful gold and silver inlays"                     }
self.redis.lpush('armor_decoration', 'carvings')
HSET  armor_decoration_description carvings {"name":"carvings", "description":"intricate carvings"                                   }
self.redis.lpush('armor_decoration', 'writing')
HSET  armor_decoration_description writing  {"name":"writing",  "description":"beautiful writing in a strange language"              }
self.redis.lpush('armor_decoration', 'runes')
HSET  armor_decoration_description runes    {"name":"runes",  "description":"strange and cryptic runes"                              }



# painful sword[ of the bull]
self.redis.lpush('armor_name_template', '{{ params.effect_description[\'name\'] }} {{ params.category_description[\'name\']}}{%if params.ability_description%} of {{params.ability_description[\'name\']}}{%endif%}')
# Bob\'s frigid sword
self.redis.lpush('armor_name_template', '{{ params.npc.name.shortname }}\'s {{ params.category_description[\'name\'] }}')
# Sharp sword of Bob
self.redis.lpush('armor_name_template', '{{ params.effect_description[\'name\'] }} {{ params.category_description[\'name\'] }} of {{ params.npc.name.shortname }}')
# Sword of Bob
self.redis.lpush('armor_name_template', '{{ params.category_description[\'name\'] }} of {{ params.npc.name.shortname }}')


