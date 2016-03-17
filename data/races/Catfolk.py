#

self.redis.lpush('npc_race', 'catfolk')

SET catfolk_details    {"name": "Catfolk",    "size": "medium",  "description": "very agile and excellent sense of sight"}

self.redis.lpush('catfolk_covering', 'fur')

SET catfolk_subrace_chance 30
# Note that descriptions aren\'t heavily used right now anyways.
self.redis.lpush('catfolk_subrace', 'leosapien')
self.redis.lpush('catfolk_subrace', 'pardii')
self.redis.lpush('catfolk_subrace', 'lynxin')

self.redis.hset('catfolk_subrace_description', 'leosapien', '{"subrace": "Leosapien (Lionfolk)",     "description": "Largest and most powerful of the catfolk" }')
self.redis.hset('catfolk_subrace_description', 'pardii', '{"subrace": "Pardii (Leopardfolk)",     "description": "a sly and cunning felinid" }')
self.redis.hset('catfolk_subrace_description', 'lynxin', '{"subrace": "Lynxin (catfolk)",         "description": "a solitary and gruff felinid" }')


self.redis.lpush('catfolkname_fullname_template', '{{params.title}} {{params.first_pre}}{{params.first_root}} {{params.middle_root}} {{params.last_pre}}{{params.last_root}} {{params.trailer}}')
self.redis.lpush('catfolkname_shortname_template', '{{params.first_pre}}{{params.first_root}}')
self.redis.lpush('catfolkname_formalname_template', '{{params.title}} {{params.last_pre}}{{params.last_root}}')

set catfolkname_first_pre_chance 100
set catfolkname_first_root_chance 100
set catfolkname_first_middle_chance 100
set catfolkname_last_pre_chance 100
set catfolkname_last_root_chance 100

self.redis.lpush('catfolkname_first_pre', 'Bar')
self.redis.lpush('catfolkname_first_pre', 'Barm')
self.redis.lpush('catfolkname_first_pre', 'Ber')
self.redis.lpush('catfolkname_first_pre', 'Breg')
self.redis.lpush('catfolkname_first_pre', 'Brid')
self.redis.lpush('catfolkname_first_pre', 'Brod')
self.redis.lpush('catfolkname_first_pre', 'Brokk')
self.redis.lpush('catfolkname_first_pre', 'Broud')
self.redis.lpush('catfolkname_first_pre', 'Burr')
self.redis.lpush('catfolkname_first_pre', 'Deg')
self.redis.lpush('catfolkname_first_pre', 'Dreg')
self.redis.lpush('catfolkname_first_pre', 'Drig')
self.redis.lpush('catfolkname_first_pre', 'Drog')
self.redis.lpush('catfolkname_first_pre', 'Gar')
self.redis.lpush('catfolkname_first_pre', 'Garm')
self.redis.lpush('catfolkname_first_pre', 'Gart')
self.redis.lpush('catfolkname_first_pre', 'Ger')
self.redis.lpush('catfolkname_first_pre', 'Germ')
self.redis.lpush('catfolkname_first_pre', 'Gert')
self.redis.lpush('catfolkname_first_pre', 'Grat')
self.redis.lpush('catfolkname_first_pre', 'Gret')
self.redis.lpush('catfolkname_first_pre', 'Grot')
self.redis.lpush('catfolkname_first_pre', 'Mae')
self.redis.lpush('catfolkname_first_pre', 'Maeg')
self.redis.lpush('catfolkname_first_pre', 'Mar')
self.redis.lpush('catfolkname_first_pre', 'Meg')
self.redis.lpush('catfolkname_first_pre', 'Mel')
self.redis.lpush('catfolkname_first_pre', 'Mer')
self.redis.lpush('catfolkname_first_pre', 'Mog')
self.redis.lpush('catfolkname_first_pre', 'Mor')
self.redis.lpush('catfolkname_first_pre', 'Mot')
self.redis.lpush('catfolkname_first_pre', 'Mul')
self.redis.lpush('catfolkname_first_pre', 'Mur')
self.redis.lpush('catfolkname_first_pre', 'Mut')
self.redis.lpush('catfolkname_first_pre', 'Nag')
self.redis.lpush('catfolkname_first_pre', 'Neg')
self.redis.lpush('catfolkname_first_pre', 'Nog')

self.redis.lpush('catfolkname_first_root', 'da')
self.redis.lpush('catfolkname_first_root', 'do')
self.redis.lpush('catfolkname_first_root', 'ta')
self.redis.lpush('catfolkname_first_root', 'to')
self.redis.lpush('catfolkname_first_root', 'la')
self.redis.lpush('catfolkname_first_root', 'lo')
self.redis.lpush('catfolkname_first_root', 'ma')
self.redis.lpush('catfolkname_first_root', 'mo')
self.redis.lpush('catfolkname_first_root', 'ga')
self.redis.lpush('catfolkname_first_root', 'go')
self.redis.lpush('catfolkname_first_root', 'ra')
self.redis.lpush('catfolkname_first_root', 'ro')
self.redis.lpush('catfolkname_first_root', 'lin')





self.redis.lpush('catfolkname_middle_root', 'of')





self.redis.lpush('catfolkname_last_pre', 'Bar')
self.redis.lpush('catfolkname_last_pre', 'Barm')
self.redis.lpush('catfolkname_last_pre', 'Ber')
self.redis.lpush('catfolkname_last_pre', 'Breg')
self.redis.lpush('catfolkname_last_pre', 'Brid')
self.redis.lpush('catfolkname_last_pre', 'Brod')
self.redis.lpush('catfolkname_last_pre', 'Brokk')
self.redis.lpush('catfolkname_last_pre', 'Broud')
self.redis.lpush('catfolkname_last_pre', 'Burr')
self.redis.lpush('catfolkname_last_pre', 'Deg')
self.redis.lpush('catfolkname_last_pre', 'Dreg')
self.redis.lpush('catfolkname_last_pre', 'Drig')
self.redis.lpush('catfolkname_last_pre', 'Drog')
self.redis.lpush('catfolkname_last_pre', 'Gar')
self.redis.lpush('catfolkname_last_pre', 'Garm')
self.redis.lpush('catfolkname_last_pre', 'Gart')
self.redis.lpush('catfolkname_last_pre', 'Ger')
self.redis.lpush('catfolkname_last_pre', 'Germ')
self.redis.lpush('catfolkname_last_pre', 'Gert')
self.redis.lpush('catfolkname_last_pre', 'Grat')
self.redis.lpush('catfolkname_last_pre', 'Gret')
self.redis.lpush('catfolkname_last_pre', 'Grot')
self.redis.lpush('catfolkname_last_pre', 'Mae')
self.redis.lpush('catfolkname_last_pre', 'Maeg')
self.redis.lpush('catfolkname_last_pre', 'Mar')
self.redis.lpush('catfolkname_last_pre', 'Meg')
self.redis.lpush('catfolkname_last_pre', 'Mel')
self.redis.lpush('catfolkname_last_pre', 'Mer')
self.redis.lpush('catfolkname_last_pre', 'Mog')
self.redis.lpush('catfolkname_last_pre', 'Mor')
self.redis.lpush('catfolkname_last_pre', 'Mot')
self.redis.lpush('catfolkname_last_pre', 'Mul')
self.redis.lpush('catfolkname_last_pre', 'Mur')
self.redis.lpush('catfolkname_last_pre', 'Mut')
self.redis.lpush('catfolkname_last_pre', 'Nag')
self.redis.lpush('catfolkname_last_pre', 'Neg')
self.redis.lpush('catfolkname_last_pre', 'Nog')

self.redis.lpush('catfolkname_last_root', 'da')
self.redis.lpush('catfolkname_last_root', 'do')
self.redis.lpush('catfolkname_last_root', 'ta')
self.redis.lpush('catfolkname_last_root', 'to')
self.redis.lpush('catfolkname_last_root', 'la')
self.redis.lpush('catfolkname_last_root', 'lo')
self.redis.lpush('catfolkname_last_root', 'ma')
self.redis.lpush('catfolkname_last_root', 'mo')
self.redis.lpush('catfolkname_last_root', 'ga')
self.redis.lpush('catfolkname_last_root', 'go')
self.redis.lpush('catfolkname_last_root', 'ra')
self.redis.lpush('catfolkname_last_root', 'ro')
self.redis.lpush('catfolkname_last_root', 'lin')
