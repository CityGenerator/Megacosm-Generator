#

self.redis.lpush('npc_race', 'molekin')

SET molekin_details    {"name": "Molekin",    "size": "medium",  "description": "poor eyesight and excellent sense of smell"}

self.redis.lpush('molekin_covering', 'fur')


SET molekin_subrace_chance 10
# Note that descriptions aren\'t heavily used right now anyways.
self.redis.lpush('molekin_subrace', 'starnose')

self.redis.hset('molekin_subrace_description', 'starnose', '{"subrace": "Star-nosed Molekin",      "description": "an unsettling hunter" }')

self.redis.lpush('molekinname_fullname_template', '{{params.title}} {{params.first_pre}}{{params.first_root}} {{params.middle_root}} {{params.last_pre}}{{params.last_root}} {{params.trailer}}')
self.redis.lpush('molekinname_shortname_template', '{{params.first_pre}}{{params.first_root}}')
self.redis.lpush('molekinname_formalname_template', '{{params.title}} {{params.last_pre}}{{params.last_root}}')


set molekinname_first_pre_chance 100
set molekinname_first_root_chance 100
set molekinname_middle_root_chance 70
set molekinname_last_pre_chance 100
set molekinname_last_root_chance 100



self.redis.lpush('molekinname_first_pre', 'Bar')
self.redis.lpush('molekinname_first_pre', 'Barm')
self.redis.lpush('molekinname_first_pre', 'Ber')
self.redis.lpush('molekinname_first_pre', 'Breg')
self.redis.lpush('molekinname_first_pre', 'Brid')
self.redis.lpush('molekinname_first_pre', 'Brod')
self.redis.lpush('molekinname_first_pre', 'Brokk')
self.redis.lpush('molekinname_first_pre', 'Broud')
self.redis.lpush('molekinname_first_pre', 'Burr')
self.redis.lpush('molekinname_first_pre', 'Deg')
self.redis.lpush('molekinname_first_pre', 'Dreg')
self.redis.lpush('molekinname_first_pre', 'Drig')
self.redis.lpush('molekinname_first_pre', 'Drog')
self.redis.lpush('molekinname_first_pre', 'Gar')
self.redis.lpush('molekinname_first_pre', 'Garm')
self.redis.lpush('molekinname_first_pre', 'Gart')
self.redis.lpush('molekinname_first_pre', 'Ger')
self.redis.lpush('molekinname_first_pre', 'Germ')
self.redis.lpush('molekinname_first_pre', 'Gert')
self.redis.lpush('molekinname_first_pre', 'Grat')
self.redis.lpush('molekinname_first_pre', 'Gret')
self.redis.lpush('molekinname_first_pre', 'Grot')
self.redis.lpush('molekinname_first_pre', 'Mae')
self.redis.lpush('molekinname_first_pre', 'Maeg')
self.redis.lpush('molekinname_first_pre', 'Mar')
self.redis.lpush('molekinname_first_pre', 'Meg')
self.redis.lpush('molekinname_first_pre', 'Mel')
self.redis.lpush('molekinname_first_pre', 'Mer')
self.redis.lpush('molekinname_first_pre', 'Mog')
self.redis.lpush('molekinname_first_pre', 'Mor')
self.redis.lpush('molekinname_first_pre', 'Mot')
self.redis.lpush('molekinname_first_pre', 'Mul')
self.redis.lpush('molekinname_first_pre', 'Mur')
self.redis.lpush('molekinname_first_pre', 'Mut')
self.redis.lpush('molekinname_first_pre', 'Nag')
self.redis.lpush('molekinname_first_pre', 'Neg')
self.redis.lpush('molekinname_first_pre', 'Nog')

self.redis.lpush('molekinname_first_root', 'da')
self.redis.lpush('molekinname_first_root', 'do')
self.redis.lpush('molekinname_first_root', 'ta')
self.redis.lpush('molekinname_first_root', 'to')
self.redis.lpush('molekinname_first_root', 'la')
self.redis.lpush('molekinname_first_root', 'lo')
self.redis.lpush('molekinname_first_root', 'ma')
self.redis.lpush('molekinname_first_root', 'mo')
self.redis.lpush('molekinname_first_root', 'ga')
self.redis.lpush('molekinname_first_root', 'go')
self.redis.lpush('molekinname_first_root', 'ra')
self.redis.lpush('molekinname_first_root', 'ro')
self.redis.lpush('molekinname_first_root', 'lin')





self.redis.lpush('molekinname_middle_root', 'of')
self.redis.lpush('molekinname_middle_root', 'from')





self.redis.lpush('molekinname_last_pre', 'Bar')
self.redis.lpush('molekinname_last_pre', 'Barm')
self.redis.lpush('molekinname_last_pre', 'Ber')
self.redis.lpush('molekinname_last_pre', 'Breg')
self.redis.lpush('molekinname_last_pre', 'Brid')
self.redis.lpush('molekinname_last_pre', 'Brod')
self.redis.lpush('molekinname_last_pre', 'Brokk')
self.redis.lpush('molekinname_last_pre', 'Broud')
self.redis.lpush('molekinname_last_pre', 'Burr')
self.redis.lpush('molekinname_last_pre', 'Deg')
self.redis.lpush('molekinname_last_pre', 'Dreg')
self.redis.lpush('molekinname_last_pre', 'Drig')
self.redis.lpush('molekinname_last_pre', 'Drog')
self.redis.lpush('molekinname_last_pre', 'Gar')
self.redis.lpush('molekinname_last_pre', 'Garm')
self.redis.lpush('molekinname_last_pre', 'Gart')
self.redis.lpush('molekinname_last_pre', 'Ger')
self.redis.lpush('molekinname_last_pre', 'Germ')
self.redis.lpush('molekinname_last_pre', 'Gert')
self.redis.lpush('molekinname_last_pre', 'Grat')
self.redis.lpush('molekinname_last_pre', 'Gret')
self.redis.lpush('molekinname_last_pre', 'Grot')
self.redis.lpush('molekinname_last_pre', 'Mae')
self.redis.lpush('molekinname_last_pre', 'Maeg')
self.redis.lpush('molekinname_last_pre', 'Mar')
self.redis.lpush('molekinname_last_pre', 'Meg')
self.redis.lpush('molekinname_last_pre', 'Mel')
self.redis.lpush('molekinname_last_pre', 'Mer')
self.redis.lpush('molekinname_last_pre', 'Mog')
self.redis.lpush('molekinname_last_pre', 'Mor')
self.redis.lpush('molekinname_last_pre', 'Mot')
self.redis.lpush('molekinname_last_pre', 'Mul')
self.redis.lpush('molekinname_last_pre', 'Mur')
self.redis.lpush('molekinname_last_pre', 'Mut')
self.redis.lpush('molekinname_last_pre', 'Nag')
self.redis.lpush('molekinname_last_pre', 'Neg')
self.redis.lpush('molekinname_last_pre', 'Nog')

self.redis.lpush('molekinname_last_root', 'da')
self.redis.lpush('molekinname_last_root', 'do')
self.redis.lpush('molekinname_last_root', 'ta')
self.redis.lpush('molekinname_last_root', 'to')
self.redis.lpush('molekinname_last_root', 'la')
self.redis.lpush('molekinname_last_root', 'lo')
self.redis.lpush('molekinname_last_root', 'ma')
self.redis.lpush('molekinname_last_root', 'mo')
self.redis.lpush('molekinname_last_root', 'ga')
self.redis.lpush('molekinname_last_root', 'go')
self.redis.lpush('molekinname_last_root', 'ra')
self.redis.lpush('molekinname_last_root', 'ro')
self.redis.lpush('molekinname_last_root', 'lin')

