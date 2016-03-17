#

self.redis.lpush('npc_race', 'gnome')

SET gnome_details      {"name": "Gnome",      "size": "small",   "description": "having engineering and intellectual expertise" }

self.redis.lpush('gnome_covering', 'skin')


SET gnome_subrace_chance 30
# Note that descriptions aren\'t heavily used right now anyways.
self.redis.lpush('gnome_subrace', 'deep')
self.redis.lpush('gnome_subrace', 'forest')
self.redis.lpush('gnome_subrace', 'rock')
self.redis.lpush('gnome_subrace', 'tinker')
self.redis.lpush('gnome_subrace', 'garden')

self.redis.hset('gnome_subrace_description', 'deep', '{"subrace": "Deep Gnome",       "description": "" }')
self.redis.hset('gnome_subrace_description', 'forest', '{"subrace": "Forest Gnome",     "description": "" }')
self.redis.hset('gnome_subrace_description', 'rock', '{"subrace": "Rock Gnome",       "description": "" }')
self.redis.hset('gnome_subrace_description', 'tinker', '{"subrace": "Tinker Gnome",     "description": "" }')
self.redis.hset('gnome_subrace_description', 'garden', '{"subrace": "Garden Gnome",     "description": "" }')

self.redis.lpush('gnomename_fullname_template', '{{params.title}} {{params.first_pre}}{{params.first_root}} {{params.last_pre}}{{params.last_root}} {{params.trailer}}')
self.redis.lpush('gnomename_shortname_template', '{{params.first_pre}}{{params.first_root}}')
self.redis.lpush('gnomename_formalname_template', '{{params.title}} {{params.last_pre}}{{params.last_root}}')


set gnomename_first_pre_chance 100
set gnomename_first_root_chance 70
set gnomename_last_pre_chance 100
set gnomename_last_root_chance 100


self.redis.lpush('gnomename_first_pre', 'Ada')
self.redis.lpush('gnomename_first_pre', 'Ai')
self.redis.lpush('gnomename_first_pre', 'Alli')
self.redis.lpush('gnomename_first_pre', 'Arn')
self.redis.lpush('gnomename_first_pre', 'Bab')
self.redis.lpush('gnomename_first_pre', 'Bea')
self.redis.lpush('gnomename_first_pre', 'Bon')
self.redis.lpush('gnomename_first_pre', 'Cot')
self.redis.lpush('gnomename_first_pre', 'Car')
self.redis.lpush('gnomename_first_pre', 'Gav')
self.redis.lpush('gnomename_first_pre', 'Gab')
self.redis.lpush('gnomename_first_pre', 'Gil')
self.redis.lpush('gnomename_first_pre', 'Ham')
self.redis.lpush('gnomename_first_pre', 'Hew')
self.redis.lpush('gnomename_first_pre', 'Jen')
self.redis.lpush('gnomename_first_pre', 'Jun')
self.redis.lpush('gnomename_first_pre', 'Kia')
self.redis.lpush('gnomename_first_pre', 'Mal')
self.redis.lpush('gnomename_first_pre', 'Nin')
self.redis.lpush('gnomename_first_pre', 'Tul')
self.redis.lpush('gnomename_first_pre', 'Tor')
self.redis.lpush('gnomename_first_pre', 'Wiz')
self.redis.lpush('gnomename_first_pre', 'Tom')
self.redis.lpush('gnomename_first_pre', 'Tom')
self.redis.lpush('gnomename_first_root', 'an')
self.redis.lpush('gnomename_first_root', 'va')
self.redis.lpush('gnomename_first_root', 'son')
self.redis.lpush('gnomename_first_root', 'rette')
self.redis.lpush('gnomename_first_root', 'mida')
self.redis.lpush('gnomename_first_root', 'gan')
self.redis.lpush('gnomename_first_root', 'lita')
self.redis.lpush('gnomename_first_root', 'gles')
self.redis.lpush('gnomename_first_root', 'nk')
self.redis.lpush('gnomename_first_root', 'tsy')
self.redis.lpush('gnomename_first_root', 'lin')
self.redis.lpush('gnomename_first_root', 'by')
self.redis.lpush('gnomename_first_root', 'ley')
self.redis.lpush('gnomename_first_root', 'ina')
self.redis.lpush('gnomename_first_root', 'xie')
self.redis.lpush('gnomename_first_root', 'key')
self.redis.lpush('gnomename_first_root', 'ita')
self.redis.lpush('gnomename_first_root', 'ton')
self.redis.lpush('gnomename_first_root', 'vin')
self.redis.lpush('gnomename_first_root', 'eno')
self.redis.lpush('gnomename_first_root', 'wan')
self.redis.lpush('gnomename_first_root', 'dan')

        
self.redis.lpush('gnomename_last_pre', 'Coggle')
self.redis.lpush('gnomename_last_pre', 'Cobble')
self.redis.lpush('gnomename_last_pre', 'Electro')
self.redis.lpush('gnomename_last_pre', 'Fuse')
self.redis.lpush('gnomename_last_pre', 'Gear')
self.redis.lpush('gnomename_last_pre', 'Grease')
self.redis.lpush('gnomename_last_pre', 'Gyro')
self.redis.lpush('gnomename_last_pre', 'Rocket')
self.redis.lpush('gnomename_last_pre', 'Thermo')
self.redis.lpush('gnomename_last_pre', 'Tiddly')
self.redis.lpush('gnomename_last_pre', 'Tinker')
self.redis.lpush('gnomename_last_pre', 'Trigger')
self.redis.lpush('gnomename_last_pre', 'Wizz')
self.redis.lpush('gnomename_last_pre', 'Wobb')
self.redis.lpush('gnomename_last_root', 'fiz')
self.redis.lpush('gnomename_last_root', 'gauge')
self.redis.lpush('gnomename_last_root', 'sprocket')
self.redis.lpush('gnomename_last_root', 'gadget')
self.redis.lpush('gnomename_last_root', 'bit')
self.redis.lpush('gnomename_last_root', 'scope')
self.redis.lpush('gnomename_last_root', 'cog')
self.redis.lpush('gnomename_last_root', 'fuel')
self.redis.lpush('gnomename_last_root', 'bolt')
self.redis.lpush('gnomename_last_root', 'jet')
self.redis.lpush('gnomename_last_root', 'wink')
self.redis.lpush('gnomename_last_root', 'tonk')
self.redis.lpush('gnomename_last_root', 'blast')
self.redis.lpush('gnomename_last_root', 'bun')

        

