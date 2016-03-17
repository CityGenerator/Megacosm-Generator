# what
self.redis.lpush('continentname_fullname_template', '{{params.title}} {{params.pre}}{{params.root}}{{params.post}}')
self.redis.lpush('continentname_shortname_template', '{{params.title}} {{params.pre}}{{params.root}}{{params.post}}')
self.redis.lpush('continentname_formalname_template', '{{params.title}} {{params.pre}}{{params.root}}{{params.post}}')


set continentname_title_chance 10
set continentname_pre_chance 100
set continentname_root_chance 100
set continentname_post_chance 30


self.redis.lpush('continentname_title', 'North')
self.redis.lpush('continentname_title', 'South')
self.redis.lpush('continentname_title', 'East')
self.redis.lpush('continentname_title', 'West')

self.redis.lpush('continentname_pre', 'As')
self.redis.lpush('continentname_pre', 'Eur')
self.redis.lpush('continentname_pre', 'An')
self.redis.lpush('continentname_pre', 'Del')
self.redis.lpush('continentname_pre', 'Mon')
self.redis.lpush('continentname_pre', 'Na')
self.redis.lpush('continentname_pre', 'Ko')
self.redis.lpush('continentname_pre', 'Mol')

self.redis.lpush('continentname_root', 'sar')
self.redis.lpush('continentname_root', 'gar')
self.redis.lpush('continentname_root', 'bel')
self.redis.lpush('continentname_root', 'por')
self.redis.lpush('continentname_root', 'ama')
self.redis.lpush('continentname_root', 'lax')
self.redis.lpush('continentname_root', 'dov')
self.redis.lpush('continentname_root', 'rov')

self.redis.lpush('continentname_post', 'ica')
self.redis.lpush('continentname_post', 'iv')
self.redis.lpush('continentname_post', 'ek')
self.redis.lpush('continentname_post', 'ar')
self.redis.lpush('continentname_post', 'i')


