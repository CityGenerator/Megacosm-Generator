#

self.redis.lpush('npc_race', 'troglodyte')

SET troglodyte_details {"name": "Troglodyte", "size": "medium",  "description": "crude behavior and foul smell"}

self.redis.lpush('troglodyte_covering', 'scales')

self.redis.lpush('troglodytename_fullname_template', '{{params.title}} {{params.first_pre}}{{params.first_root}}  {{params.trailer}}')
self.redis.lpush('troglodytename_shortname_template', '{{params.first_pre}}{{params.first_root}}')
self.redis.lpush('troglodytename_formalname_template', '{{params.title}} {{params.first_pre}}{{params.first_root}}')


set troglodytename_first_pre_chance 100
set troglodytename_first_root_chance 100


self.redis.lpush('troglodytename_first_pre', 'An')
self.redis.lpush('troglodytename_first_pre', 'Cee')
self.redis.lpush('troglodytename_first_pre', 'Elh')
self.redis.lpush('troglodytename_first_pre', 'Ghri')
self.redis.lpush('troglodytename_first_pre', 'Goz')
self.redis.lpush('troglodytename_first_pre', 'Por')
self.redis.lpush('troglodytename_first_pre', 'Surp')
self.redis.lpush('troglodytename_first_pre', 'Til')
self.redis.lpush('troglodytename_first_pre', 'Voth')

self.redis.lpush('troglodytename_first_root', 'ra')
self.redis.lpush('troglodytename_first_root', 'zer')
self.redis.lpush('troglodytename_first_root', 's')
self.redis.lpush('troglodytename_first_root', 'ka')
self.redis.lpush('troglodytename_first_root', 'lak')
self.redis.lpush('troglodytename_first_root', 'raz')
self.redis.lpush('troglodytename_first_root', 'g')
self.redis.lpush('troglodytename_first_root', 'karo')
        
    
