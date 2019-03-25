#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """


def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.lpush('magicitem_creator_template', '{{params.npc.race | article}} named {{params.npc.name.fullname}}')
    self.redis.lpush('magicitem_location', 'buried in a nest')
    self.redis.lpush('magicitem_vibe', 'gives you feelings of power')
    self.redis.lpush('magicitem_vibe_when', 'looking at')
    self.redis.set('magicitem_curse_chance', 40)

    self.redis.zadd('magicitem_age', {'{"name":"over a century ago",    "score":100 }': 100})
    self.redis.zadd('magicitem_quality', {'{"name":"excellent", "score":100 }': 100})
    self.redis.zadd('magicitem_repair', {'{"name":"in pristine condition",  "score":100 }': 100})
    self.redis.zadd('magicitem_strength', {'{"name":"powerful",  "score":100  }': 100})
    self.redis.zadd('magicitem_value', {'{"name":"artifact",  "score": 100  }': 100})
    self.redis.lpush('magicitem_kind', 'armor')
    import_armor_fixtures(self)
    import_weapon_fixtures(self)
    import_potion_fixtures(self)
    import_scroll_fixtures(self)


def import_armor_fixtures(self):
    """ Armor Fixtures"""
    self.redis.hset('armor_ability_description',
                    'shock', '{"name":"shock",  "description":"has a chance of stunning an attacker" }')
    self.redis.hset('armor_category_description',
                    'leatherarmor', '{"name":"leather armor",  "materialpart":"chest" }')
    self.redis.hset('armor_decoration_description',
                    'flames', '{"name":"flames", "description":"streaks of red and yellow which glisten like flames"}')
    self.redis.hset('armor_effect_description',
                    'muffled', '{"name":"muffled", ' +
                    '"description":"allows the wearer to move more quietly than otherwise possible" }')
    self.redis.hset('armor_flaw_description',
                    'dent', '{"name":"dent", "description":"" }')
    self.redis.hset('armor_material_description',
                    'coldiron', '{"name":"cold iron",  "description":"beautiful cold steel"    }')
    self.redis.hset('armor_visualcause_description',
                    'orc', '{"name":"orc",  "description":"exposed to orcs"  }')
    self.redis.hset('armor_visualeffect_description',
                    'sparkles', '{"name":"sparkles",    "description":"emits a faint sparkle"  }')

    self.redis.lpush('armor_ability', 'shock')
    self.redis.lpush('armor_category', 'leatherarmor')
    self.redis.lpush('armor_decoration', 'flames')
    self.redis.lpush('armor_effect', 'muffled')
    self.redis.lpush('armor_flaw', 'dent')
    self.redis.lpush('armor_material', 'coldiron')
    self.redis.lpush('armor_template',
                     '{{ params.effect_description["name"] }} {{ params.category_description["name"]}}' +
                     '{%if params.ability_description%} of {{params.ability_description["name"]}}{%endif%}')
    self.redis.lpush('armor_visualcause', 'orc')
    self.redis.lpush('armor_visualeffect', 'sparkles')


def import_potion_fixtures(self):
    """ Potion Fixtures"""
    self.redis.lpush('potion_template',
                     '{{ params.strength["name"] }} {{ params.effect_description["name"] }} {{ params.kind }}')
    self.redis.hset('potion_effect_description',
                    'accuracyboost', '{"name":"accuracy boost", "description":"increases accuracy with projectiles" }')
    self.redis.lpush('potion_effect', 'accuracyboost')

    self.redis.zadd('potion_duration', {'{"name":"is permanent",  "score":100 }': 100})
    self.redis.zadd('potion_consistency', {'{"name":"gritty",  "score":100 }': 100})
    self.redis.lpush('potion_color', 'aquamarine')
    self.redis.hset('potion_color_description', 'aquamarine', '{"name":"aquamarine", "hex":"7FFFD4" }')
    self.redis.lpush('potion_sideeffect', 'seizures')
    self.redis.lpush('potion_variety', 'potion')
    self.redis.lpush('potion_smell', 'bubblegum')
    self.redis.lpush('potion_taste', 'acidic')
    self.redis.lpush('potion_texture', 'chalky')
    self.redis.lpush('potion_container_material', 'glass')
    self.redis.lpush('potion_container_decoration', 'cryptic writing')
    self.redis.lpush('potion_container_label', 'illegible')
    self.redis.lpush('potion_container_shape', 'ampoule')


def import_scroll_fixtures(self):
    """ Scroll Fixtures"""
    self.redis.lpush('scroll_template', '{{ params.strength["name"] }} {{ params.effect_description["name"] }} scroll')
    self.redis.hset('scroll_effect_description', 'adnauseum',
                    '{"name":"ad nauseum",    "description":"causes sudden and severe nausea" }')
    self.redis.lpush('scroll_effect', 'adnauseum')
    self.redis.zadd('scroll_duration', {'{"name":"is permanent",  "score":100  }': 100})
    self.redis.lpush('scroll_sideeffect', 'seizures')
    self.redis.lpush('scroll_material', 'papyrus')
    self.redis.lpush('scroll_writingtype', 'cryptic')
    self.redis.lpush('scroll_writingform', 'symbols')
    self.redis.lpush('scroll_container_label', 'illegible')
    self.redis.lpush('scroll_container_type', 'scroll case')


def import_weapon_fixtures(self):
    """ Weapon Fixtures"""
    self.redis.lpush('weapon_category', 'sword')
    self.redis.hset('weapon_category_description', 'sword', '{"name":"sword",  "materialpart":"blade"    }')
    self.redis.lpush('weapon_ability', 'bull')
    self.redis.hset('weapon_ability_description', 'bull',
                    '{"name":"the bull",  "description":"grants the user unnatural strength"  }')
    self.redis.lpush('weapon_effect', 'sharp')
    self.redis.hset('weapon_effect_description', 'sharp',
                    '{"name":"sharp",  "description":"will occasionally slice through anything"  }')

    self.redis.lpush('weapon_flaw', 'chip')
    self.redis.hset('weapon_flaw_description', 'chip', '{"name":"small chip",  "description":""  }')
    self.redis.lpush('weapon_visualcause', 'orc')
    self.redis.hset('weapon_visualcause_description', 'orc', '{"name":"orc",  "description":"exposed to orcs"  }')
    self.redis.lpush('weapon_visualeffect', 'sparkles')
    self.redis.lpush('weapon_material', 'coldiron')
    self.redis.hset('weapon_material_description', 'coldiron',
                    '{"name":"cold iron",  "description":"beautiful cold steel"   }')
    self.redis.lpush('weapon_decoration', 'flames')
    self.redis.hset('weapon_decoration_description', 'flames',
                    '{"name":"flames", "description":"streaks of red and yellow which glisten like flames"  }')
    self.redis.lpush('weapon_template',
                     '{{ params.effect_description["name"] }} {{ params.category_description["name"]}}' +
                     '{%if params.ability_description%} of {{params.ability_description["name"]}}{%endif%}')
