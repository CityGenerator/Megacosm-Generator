#

self.redis.lpush('npc_race', 'ogre')

SET ogre_details       {"name": "Ogre",       "size": "large",   "description": "large size and dim wits"}

self.redis.lpush('ogre_covering', 'skin')


SET ogre_subrace_chance 30
# Note that descriptions aren\'t heavily used right now anyways.
self.redis.lpush('ogre_subrace', 'merrow')
self.redis.lpush('ogre_subrace', 'mage')

HSET ogre_subrace_description merrow      {"subrace": "Merrow (Ogre)",     "description": "aquatic ogre" }
HSET ogre_subrace_description mage        {"subrace": "Ogre Mage",         "description": "" }

self.redis.lpush('ogrename_fullname_template', '{{params.title}} {{params.first_pre}}{{params.first_root}} {{params.last_pre}}{{params.last_root}} {{params.trailer}}')
self.redis.lpush('ogrename_shortname_template', '{{params.first_pre}}{{params.first_root}}')
self.redis.lpush('ogrename_formalname_template', '{{params.title}} {{params.last_pre}}{{params.last_root}}')

set ogrename_first_pre_chance 100
set ogrename_first_root_chance 100
set ogrename_last_pre_chance 100
set ogrename_last_root_chance 100

self.redis.lpush('ogrename_first_pre', 'Po')
self.redis.lpush('ogrename_first_pre', 'Do')
self.redis.lpush('ogrename_first_pre', 'Du')
self.redis.lpush('ogrename_first_pre', 'Da')
self.redis.lpush('ogrename_first_pre', 'Gu')
self.redis.lpush('ogrename_first_pre', 'U')
self.redis.lpush('ogrename_first_pre', 'Gha')
self.redis.lpush('ogrename_first_pre', 'Go')
self.redis.lpush('ogrename_first_pre', 'Gu')
self.redis.lpush('ogrename_first_pre', 'Ki')

self.redis.lpush('ogrename_first_root', 'sh')
self.redis.lpush('ogrename_first_root', 'k')
self.redis.lpush('ogrename_first_root', 'ap')
self.redis.lpush('ogrename_first_root', 'gan')
self.redis.lpush('ogrename_first_root', 'duk')
self.redis.lpush('ogrename_first_root', 'bel')
self.redis.lpush('ogrename_first_root', 'bal')
        
self.redis.lpush('ogrename_last_pre', 'Bear')
self.redis.lpush('ogrename_last_pre', 'Boar')
self.redis.lpush('ogrename_last_pre', 'Eagle')
self.redis.lpush('ogrename_last_pre', 'Rock')
self.redis.lpush('ogrename_last_pre', 'Oak')
self.redis.lpush('ogrename_last_pre', 'Ox')

self.redis.lpush('ogrename_last_root', 'mane')
self.redis.lpush('ogrename_last_root', 'snout')
self.redis.lpush('ogrename_last_root', 'fang')
self.redis.lpush('ogrename_last_root', 'claw')
self.redis.lpush('ogrename_last_root', 'tooth')
self.redis.lpush('ogrename_last_root', 'root')
self.redis.lpush('ogrename_last_root', 'branch')
self.redis.lpush('ogrename_last_root', 'nut')
        
    
