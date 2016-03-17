#

self.redis.lpush('npc_race', 'kobold')

SET kobold_details     {"name": "Kobold",     "size": "small",   "description": "their small stature and cowardice"}

self.redis.lpush('kobold_covering', 'scales')

SET kobold_subrace_chance 30
# Note that descriptions aren\'t heavily used right now anyways.
self.redis.lpush('kobold_subrace', 'aquatic')
self.redis.lpush('kobold_subrace', 'sand')
self.redis.lpush('kobold_subrace', 'mud')
self.redis.lpush('kobold_subrace', 'jungle')

self.redis.hset('kobold_subrace_description', 'aquatic', '{"subrace": "Aquatic Kobold",   "description": "" }')
self.redis.hset('kobold_subrace_description', 'sand', '{"subrace": "Sand Kobold",      "description": "" }')
self.redis.hset('kobold_subrace_description', 'mud', '{"subrace": "Mud Kobold",       "description": "" }')
self.redis.hset('kobold_subrace_description', 'jungle', '{"subrace": "Jungle Kobold",    "description": "" }')

self.redis.lpush('koboldname_fullname_template', '{{params.title}} {{params.first_root}}{{params.first_post}} {{params.trailer}}')
self.redis.lpush('koboldname_shortname_template', '{{params.first_root}}')
self.redis.lpush('koboldname_formalname_template', '{{params.title}} {{params.first_root}}')


set koboldname_first_root_chance 100


self.redis.lpush('koboldname_first_root', 'Bat')
self.redis.lpush('koboldname_first_root', 'Bap')
self.redis.lpush('koboldname_first_root', 'Bit')
self.redis.lpush('koboldname_first_root', 'Bip')
self.redis.lpush('koboldname_first_root', 'Bot')
self.redis.lpush('koboldname_first_root', 'Car')
self.redis.lpush('koboldname_first_root', 'Cor')
self.redis.lpush('koboldname_first_root', 'Cak')
self.redis.lpush('koboldname_first_root', 'Dat')
self.redis.lpush('koboldname_first_root', 'Dit')
self.redis.lpush('koboldname_first_root', 'Dot')
self.redis.lpush('koboldname_first_root', 'Fax')
self.redis.lpush('koboldname_first_root', 'Fat')
self.redis.lpush('koboldname_first_root', 'Fot')
self.redis.lpush('koboldname_first_root', 'Gat')
self.redis.lpush('koboldname_first_root', 'Git')
self.redis.lpush('koboldname_first_root', 'Gip')
self.redis.lpush('koboldname_first_root', 'Got')
self.redis.lpush('koboldname_first_root', 'Jat')
self.redis.lpush('koboldname_first_root', 'Jit')
self.redis.lpush('koboldname_first_root', 'Jot')
self.redis.lpush('koboldname_first_root', 'Jop')
self.redis.lpush('koboldname_first_root', 'Lat')
self.redis.lpush('koboldname_first_root', 'Lik')
self.redis.lpush('koboldname_first_root', 'Lot')
self.redis.lpush('koboldname_first_root', 'Nat')
self.redis.lpush('koboldname_first_root', 'Niz')
self.redis.lpush('koboldname_first_root', 'Nip')
self.redis.lpush('koboldname_first_root', 'Not')
self.redis.lpush('koboldname_first_root', 'Nop')
self.redis.lpush('koboldname_first_root', 'Pat')
self.redis.lpush('koboldname_first_root', 'Paz')
self.redis.lpush('koboldname_first_root', 'Pot')
self.redis.lpush('koboldname_first_root', 'Rat')
self.redis.lpush('koboldname_first_root', 'Rap')
self.redis.lpush('koboldname_first_root', 'Rit')
self.redis.lpush('koboldname_first_root', 'Rot')
self.redis.lpush('koboldname_first_root', 'Rop')
self.redis.lpush('koboldname_first_root', 'Taz')
self.redis.lpush('koboldname_first_root', 'Teb')
self.redis.lpush('koboldname_first_root', 'Tean')
self.redis.lpush('koboldname_first_root', 'Vab')
self.redis.lpush('koboldname_first_root', 'Vaz')
self.redis.lpush('koboldname_first_root', 'Vit')
self.redis.lpush('koboldname_first_root', 'Vor')
self.redis.lpush('koboldname_first_root', 'Wat')
self.redis.lpush('koboldname_first_root', 'Wit')
self.redis.lpush('koboldname_first_root', 'Wot')
self.redis.lpush('koboldname_first_root', 'Yat')
self.redis.lpush('koboldname_first_root', 'Yap')
self.redis.lpush('koboldname_first_root', 'Yik')
self.redis.lpush('koboldname_first_root', 'Yip')
self.redis.lpush('koboldname_first_root', 'Yot')
self.redis.lpush('koboldname_first_root', 'Yop')
self.redis.lpush('koboldname_first_root', 'Zat')
self.redis.lpush('koboldname_first_root', 'Zit')
self.redis.lpush('koboldname_first_root', 'Zol')


