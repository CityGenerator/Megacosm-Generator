#

self.redis.lpush('npc_race', 'coatikin')

SET coatikin_details    {"name": "Coatikin",    "size": "small",  "description": "agile with excellent night vision"}

self.redis.lpush('coatikin_covering', 'fur')


self.redis.lpush('coatikinname_fullname_template', '{{params.title}} {{params.first_root}} {{params.last_pre}}{{params.last_root}}{{params.last_post}} {{params.trailer}}')
self.redis.lpush('coatikinname_shortname_template', '{{params.first_root}}')
self.redis.lpush('coatikinname_formalname_template', '{{params.title}} {{params.last_pre}}{{params.last_root}}{{params.last_post}}')

set coatikinname_first_root_chance 100
set coatikinname_last_pre_chance 100
set coatikinname_last_root_chance 100
set coatikinname_last_post_chance 80




self.redis.lpush('coatikinname_first_root', 'Beetle')
self.redis.lpush('coatikinname_first_root', 'Frog')
self.redis.lpush('coatikinname_first_root', 'Lichen')
self.redis.lpush('coatikinname_first_root', 'Leaf')
self.redis.lpush('coatikinname_first_root', 'Toad')
self.redis.lpush('coatikinname_first_root', 'Nut')
self.redis.lpush('coatikinname_first_root', 'Acorn')
self.redis.lpush('coatikinname_first_root', 'Bark')
self.redis.lpush('coatikinname_first_root', 'Berry')
self.redis.lpush('coatikinname_first_root', 'Root')
self.redis.lpush('coatikinname_first_root', 'Tadpole')
self.redis.lpush('coatikinname_first_root', 'Gecko')
self.redis.lpush('coatikinname_first_root', 'Bee')
self.redis.lpush('coatikinname_first_root', 'Buggy')
self.redis.lpush('coatikinname_first_root', 'Twig')
self.redis.lpush('coatikinname_first_root', 'Bushy')
self.redis.lpush('coatikinname_first_root', 'Grassley')





self.redis.lpush('coatikinname_last_pre', 'B')
self.redis.lpush('coatikinname_last_pre', 'D')
self.redis.lpush('coatikinname_last_pre', 'R')
self.redis.lpush('coatikinname_last_pre', 'T')
self.redis.lpush('coatikinname_last_pre', 'G')
self.redis.lpush('coatikinname_last_pre', 'J')
self.redis.lpush('coatikinname_last_pre', 'K')
self.redis.lpush('coatikinname_last_pre', 'L')
self.redis.lpush('coatikinname_last_pre', 'Z')
self.redis.lpush('coatikinname_last_pre', 'Ch')
self.redis.lpush('coatikinname_last_pre', 'Sh')
self.redis.lpush('coatikinname_last_pre', 'N')
self.redis.lpush('coatikinname_last_pre', 'M')
self.redis.lpush('coatikinname_last_pre', 'Bl')
self.redis.lpush('coatikinname_last_pre', 'Th')
self.redis.lpush('coatikinname_last_pre', 'Cr')


self.redis.lpush('coatikinname_last_root', 'ab')
self.redis.lpush('coatikinname_last_root', 'ad')
self.redis.lpush('coatikinname_last_root', 'af')
self.redis.lpush('coatikinname_last_root', 'ag')
self.redis.lpush('coatikinname_last_root', 'ak')
self.redis.lpush('coatikinname_last_root', 'al')
self.redis.lpush('coatikinname_last_root', 'am')
self.redis.lpush('coatikinname_last_root', 'an')
self.redis.lpush('coatikinname_last_root', 'ar')
self.redis.lpush('coatikinname_last_root', 'as')
self.redis.lpush('coatikinname_last_root', 'at')
self.redis.lpush('coatikinname_last_root', 'av')
self.redis.lpush('coatikinname_last_root', 'aw')
self.redis.lpush('coatikinname_last_root', 'ax')
self.redis.lpush('coatikinname_last_root', 'az')


self.redis.lpush('coatikinname_last_root', 'eb')
self.redis.lpush('coatikinname_last_root', 'ed')
self.redis.lpush('coatikinname_last_root', 'ef')
self.redis.lpush('coatikinname_last_root', 'eg')
self.redis.lpush('coatikinname_last_root', 'ek')
self.redis.lpush('coatikinname_last_root', 'el')
self.redis.lpush('coatikinname_last_root', 'em')
self.redis.lpush('coatikinname_last_root', 'en')
self.redis.lpush('coatikinname_last_root', 'ep')
self.redis.lpush('coatikinname_last_root', 'er')
self.redis.lpush('coatikinname_last_root', 'es')
self.redis.lpush('coatikinname_last_root', 'et')
self.redis.lpush('coatikinname_last_root', 'ev')
self.redis.lpush('coatikinname_last_root', 'ew')
self.redis.lpush('coatikinname_last_root', 'ex')
self.redis.lpush('coatikinname_last_root', 'ez')
self.redis.lpush('coatikinname_last_root', 'ib')
self.redis.lpush('coatikinname_last_root', 'id')
self.redis.lpush('coatikinname_last_root', 'if')
self.redis.lpush('coatikinname_last_root', 'ig')
self.redis.lpush('coatikinname_last_root', 'ik')
self.redis.lpush('coatikinname_last_root', 'il')
self.redis.lpush('coatikinname_last_root', 'im')
self.redis.lpush('coatikinname_last_root', 'in')
self.redis.lpush('coatikinname_last_root', 'ip')
self.redis.lpush('coatikinname_last_root', 'ir')
self.redis.lpush('coatikinname_last_root', 'is')
self.redis.lpush('coatikinname_last_root', 'iv')
self.redis.lpush('coatikinname_last_root', 'iw')
self.redis.lpush('coatikinname_last_root', 'ix')
self.redis.lpush('coatikinname_last_root', 'iz')
self.redis.lpush('coatikinname_last_root', 'ob')
self.redis.lpush('coatikinname_last_root', 'od')
self.redis.lpush('coatikinname_last_root', 'of')
self.redis.lpush('coatikinname_last_root', 'og')
self.redis.lpush('coatikinname_last_root', 'ok')
self.redis.lpush('coatikinname_last_root', 'ol')
self.redis.lpush('coatikinname_last_root', 'om')
self.redis.lpush('coatikinname_last_root', 'on')
self.redis.lpush('coatikinname_last_root', 'op')
self.redis.lpush('coatikinname_last_root', 'or')
self.redis.lpush('coatikinname_last_root', 'os')
self.redis.lpush('coatikinname_last_root', 'ot')
self.redis.lpush('coatikinname_last_root', 'ov')
self.redis.lpush('coatikinname_last_root', 'ow')
self.redis.lpush('coatikinname_last_root', 'ox')
self.redis.lpush('coatikinname_last_root', 'oz')

self.redis.lpush('coatikinname_last_post', 'by')
self.redis.lpush('coatikinname_last_post', 'cy')
self.redis.lpush('coatikinname_last_post', 'dy')
self.redis.lpush('coatikinname_last_post', 'fy')
self.redis.lpush('coatikinname_last_post', 'gy')
self.redis.lpush('coatikinname_last_post', 'ky')
self.redis.lpush('coatikinname_last_post', 'ly')
self.redis.lpush('coatikinname_last_post', 'my')
self.redis.lpush('coatikinname_last_post', 'ny')
self.redis.lpush('coatikinname_last_post', 'py')
self.redis.lpush('coatikinname_last_post', 'ry')
self.redis.lpush('coatikinname_last_post', 'sy')
self.redis.lpush('coatikinname_last_post', 'ty')
self.redis.lpush('coatikinname_last_post', 'vy')
self.redis.lpush('coatikinname_last_post', 'xy')
self.redis.lpush('coatikinname_last_post', 'zy')





