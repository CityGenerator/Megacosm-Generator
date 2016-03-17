#

self.redis.lpush('magicitem_kind', 'armor')


self.redis.lpush('armor_category', 'leatherarmor')
self.redis.hset('armor_category_description', 'leatherarmor', '{"name":"leather armor",     "materialpart":"chest" }')
self.redis.lpush('armor_category', 'breastplate')
self.redis.hset('armor_category_description', 'breastplate', '{"name":"breastplate",       "materialpart":"chest" }')
self.redis.lpush('armor_category', 'chainmail')
self.redis.hset('armor_category_description', 'chainmail', '{"name":"chainmail",         "materialpart":"trim" }')
self.redis.lpush('armor_category', 'hidearmor')
self.redis.hset('armor_category_description', 'hidearmor', '{"name":"hide armor",        "materialpart":"chest" }')
self.redis.lpush('armor_category', 'platearmor')
self.redis.hset('armor_category_description', 'platearmor', '{"name":"plate armor",       "materialpart":"chest" }')
self.redis.lpush('armor_category', 'shield')
self.redis.hset('armor_category_description', 'shield', '{"name":"shield",            "materialpart":"front" }')
self.redis.lpush('armor_category', 'helm')
self.redis.hset('armor_category_description', 'helm', '{"name":"helm",              "materialpart":"top"   }')
self.redis.lpush('armor_category', 'gauntlets')
self.redis.hset('armor_category_description', 'gauntlets', '{"name":"gauntlet set",      "materialpart":"wrist" }')
self.redis.lpush('armor_category', 'bracers')
self.redis.hset('armor_category_description', 'bracers', '{"name":"bracer set",        "materialpart":"forearm" }')



SET   armor_ability_chance 20
self.redis.lpush('armor_ability', 'shock')
self.redis.hset('armor_ability_description', 'shock', '{"name":"shock",        "description":"has a chance of stunning an attacker" }')
self.redis.lpush('armor_ability', 'glory')
self.redis.hset('armor_ability_description', 'glory', '{"name":"glory",        "description":"emboldens comrades in battle" }')
self.redis.lpush('armor_ability', 'shadows')
self.redis.hset('armor_ability_description', 'shadows', '{"name":"the shadows",  "description":"makes the wearer virtually undetectable in shadows" }')
self.redis.lpush('armor_ability', 'grace')
self.redis.hset('armor_ability_description', 'grace', '{"name":"grace",        "description":"grants the user an unnatural grace"     }')
self.redis.lpush('armor_ability', 'toughness')
self.redis.hset('armor_ability_description', 'toughness', '{"name":"toughness",    "description":"grants the user unnatural constitution" }')
self.redis.lpush('armor_ability', 'holy')
self.redis.hset('armor_ability_description', 'holy', '{"name":"the holy",     "description":"may cause fear in the undead"           }')
self.redis.lpush('armor_ability', 'defense')
self.redis.hset('armor_ability_description', 'defense', '{"name":"defense",      "description":"may protect the user from some attacks" }')

self.redis.lpush('armor_effect', 'muffled')
self.redis.hset('armor_effect_description', 'muffled', '{"name":"muffled",          "description":"allows the wearer to move more quietly than otherwise possible" }')
self.redis.lpush('armor_effect', 'slick')
self.redis.hset('armor_effect_description', 'slick', '{"name":"slick",            "description":"cause the wearer to be difficult to grasp" }')
self.redis.lpush('armor_effect', 'deflecting')
self.redis.hset('armor_effect_description', 'deflecting', '{"name":"deflecting",       "description":"deflects some projectiles that would otherwise hit" }')
self.redis.lpush('armor_effect', 'ringing')
self.redis.hset('armor_effect_description', 'ringing', '{"name":"ringing",          "description":"causes a deafening roar when struck"      }')




SET   armor_flaw_chance 30

self.redis.lpush('armor_flaw', 'dent')
self.redis.hset('armor_flaw_description', 'dent', '{"name":"dent", "description":"" }')
self.redis.lpush('armor_flaw', 'ding')
self.redis.hset('armor_flaw_description', 'ding', '{"name":"ding", "description":"" }')
self.redis.lpush('armor_flaw', 'chip')
self.redis.hset('armor_flaw_description', 'chip', '{"name":"small chip",         "description":""  }')
self.redis.lpush('armor_flaw', 'missing')
self.redis.hset('armor_flaw_description', 'missing', '{"name":"missing decoration", "description":""  }')
self.redis.lpush('armor_flaw', 'crack')
self.redis.hset('armor_flaw_description', 'crack', '{"name":"crack",              "description":""  }')
self.redis.lpush('armor_flaw', 'discolored')
self.redis.hset('armor_flaw_description', 'discolored', '{"name":"discolored spot",    "description":""  }')
self.redis.lpush('armor_flaw', 'blackened')
self.redis.hset('armor_flaw_description', 'blackened', '{"name":"blackened spot",     "description":""  }')
self.redis.lpush('armor_flaw', 'bloodstained')
self.redis.hset('armor_flaw_description', 'bloodstained', '{"name":"bloodstain",         "description":""  }')


# When _____________, the armor emits a faint glow
self.redis.lpush('armor_visualcause', 'orc')
self.redis.hset('armor_visualcause_description', 'orc', '{"name":"orc",      "description":"exposed to orcs"         }')
self.redis.lpush('armor_visualcause', 'darkness')
self.redis.hset('armor_visualcause_description', 'darkness', '{"name":"darkness", "description":"worn in the darkness"    }')
self.redis.lpush('armor_visualcause', 'blood')
self.redis.hset('armor_visualcause_description', 'blood', '{"name":"blood",    "description":"covered with blood"    }')
self.redis.lpush('armor_visualcause', 'danger')
self.redis.hset('armor_visualcause_description', 'danger', '{"name":"danger",    "description":"danger is near"    }')


SET   armor_visualeffect_chance 10
self.redis.lpush('armor_visualeffect', 'sparkles')
self.redis.hset('armor_visualeffect_description', 'sparkles', '{"name":"sparkles",    "description":"emits a faint sparkle"                   }')
self.redis.lpush('armor_visualeffect', 'glows')
self.redis.hset('armor_visualeffect_description', 'glows', '{"name":"glows",       "description":"emits a bright glow"                     }')
self.redis.lpush('armor_visualeffect', 'redpulse')
self.redis.hset('armor_visualeffect_description', 'redpulse', '{"name":"red pulse",    "description":"pulses red in time with your heartbeat" }')
self.redis.lpush('armor_visualeffect', 'electricity')
self.redis.hset('armor_visualeffect_description', 'electricity', '{"name":"electricity", "description":"crackles with visible electricity"       }')



self.redis.lpush('armor_material', 'coldiron')
self.redis.hset('armor_material_description', 'coldiron', '{"name":"cold iron",       "description":"beautiful cold steel"    }')
self.redis.lpush('armor_material', 'steel')
self.redis.hset('armor_material_description', 'steel', '{"name":"steel",       "description":"high quality steel"          }')
self.redis.lpush('armor_material', 'crystal')
self.redis.hset('armor_material_description', 'crystal', '{"name":"crystal",     "description":"a strange crystal"           }')
self.redis.lpush('armor_material', 'bone')
self.redis.hset('armor_material_description', 'bone', '{"name":"bone",        "description":"a specially treated bone"    }')


SET   armor_decoration_chance 10

self.redis.lpush('armor_decoration', 'flames')
self.redis.hset('armor_decoration_description', 'flames', '{"name":"flames",   "description":"streaks of red and yellow which glisten like flames"  }')
self.redis.lpush('armor_decoration', 'inlay')
self.redis.hset('armor_decoration_description', 'inlay', '{"name":"inlay",    "description":"beautiful gold and silver inlays"                     }')
self.redis.lpush('armor_decoration', 'carvings')
self.redis.hset('armor_decoration_description', 'carvings', '{"name":"carvings", "description":"intricate carvings"                                   }')
self.redis.lpush('armor_decoration', 'writing')
self.redis.hset('armor_decoration_description', 'writing', '{"name":"writing",  "description":"beautiful writing in a strange language"              }')
self.redis.lpush('armor_decoration', 'runes')
self.redis.hset('armor_decoration_description', 'runes', '{"name":"runes",  "description":"strange and cryptic runes"                              }')



# painful sword[ of the bull]
self.redis.lpush('armor_name_template', '{{ params.effect_description[\'name\'] }} {{ params.category_description[\'name\']}}{%if params.ability_description%} of {{params.ability_description[\'name\']}}{%endif%}')
# Bob\'s frigid sword
self.redis.lpush('armor_name_template', '{{ params.npc.name.shortname }}\'s {{ params.category_description[\'name\'] }}')
# Sharp sword of Bob
self.redis.lpush('armor_name_template', '{{ params.effect_description[\'name\'] }} {{ params.category_description[\'name\'] }} of {{ params.npc.name.shortname }}')
# Sword of Bob
self.redis.lpush('armor_name_template', '{{ params.category_description[\'name\'] }} of {{ params.npc.name.shortname }}')


