#

self.redis.lpush('npc_race', 'harpy')

SET harpy_details {"name": "Harpy", "size": "medium",  "description": "winged and feathered feral humanoid with a greedy reputation"}

self.redis.lpush('harpy_covering', 'feathers')



self.redis.lpush('harpyname_fullname_template', '{{params.title}} {{params.first_pre}}{{params.first_root}} {{params.trailer}}')
self.redis.lpush('harpyname_shortname_template', '{{params.first_pre}}{{params.first_root}}')
self.redis.lpush('harpyname_formalname_template', '{{params.title}} {{params.first_pre}}{{params.first_root}}')

set harpyname_first_pre_chance 100
set harpyname_first_root_chance 100




self.redis.lpush('harpyname_first_pre', 'Ae')
self.redis.lpush('harpyname_first_pre', 'Ocy')
self.redis.lpush('harpyname_first_pre', 'Cela')
self.redis.lpush('harpyname_first_pre', 'Pod')
self.redis.lpush('harpyname_first_pre', 'Nico')
self.redis.lpush('harpyname_first_pre', 'Achi')
self.redis.lpush('harpyname_first_pre', 'Aga')
self.redis.lpush('harpyname_first_pre', 'Aphro')
self.redis.lpush('harpyname_first_pre', 'Daph')
self.redis.lpush('harpyname_first_pre', 'Dor')
self.redis.lpush('harpyname_first_pre', 'Elek')
self.redis.lpush('harpyname_first_pre', 'Eva')
self.redis.lpush('harpyname_first_pre', 'Fron')
self.redis.lpush('harpyname_first_pre', 'Gia')
self.redis.lpush('harpyname_first_pre', 'Hath')
self.redis.lpush('harpyname_first_pre', 'Hy')
self.redis.lpush('harpyname_first_pre', 'Io')
self.redis.lpush('harpyname_first_pre', 'Kassa')
self.redis.lpush('harpyname_first_pre', 'Mel')
self.redis.lpush('harpyname_first_pre', 'My')
self.redis.lpush('harpyname_first_pre', 'Nata')
self.redis.lpush('harpyname_first_pre', 'Oly')
self.redis.lpush('harpyname_first_pre', 'Pan')

self.redis.lpush('harpyname_first_root', 'llo')
self.redis.lpush('harpyname_first_root', 'pete')
self.redis.lpush('harpyname_first_root', 'eno')
self.redis.lpush('harpyname_first_root', 'arge')
self.redis.lpush('harpyname_first_root', 'thoe')
self.redis.lpush('harpyname_first_root', 'dora')
self.redis.lpush('harpyname_first_root', 'thys')
self.redis.lpush('harpyname_first_root', 'rine')
self.redis.lpush('harpyname_first_root', 'pias')
self.redis.lpush('harpyname_first_root', 'tine')
self.redis.lpush('harpyname_first_root', 'ibe')
self.redis.lpush('harpyname_first_root', 'andra')
self.redis.lpush('harpyname_first_root', 'thea')
self.redis.lpush('harpyname_first_root', 'rinna')
self.redis.lpush('harpyname_first_root', 'isto')
self.redis.lpush('harpyname_first_root', 'bel')


