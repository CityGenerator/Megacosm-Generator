#

self.redis.lpush('npc_race', 'hobgoblin')

SET hobgoblin_details     {"name": "Hobgoblin",     "size": "hobgoblin",   "description": "the more civilized of the goblinoids"}

self.redis.lpush('hobgoblin_covering', 'skin')

SET hobgoblin_subrace_chance 30
# Note that descriptions aren\'t heavily used right now anyways.
self.redis.lpush('hobgoblin_subrace', 'shadow')
self.redis.lpush('hobgoblin_subrace', 'koalinth')

self.redis.hset('hobgoblin_subrace_description', 'shadow', '{"subrace": "Shadow Hobgoblin",      "description": "" }')
self.redis.hset('hobgoblin_subrace_description', 'koalinth', '{"subrace": "Koalinth Hobgoblin",      "description": "" }')


self.redis.lpush('hobgoblinname_fullname_template', '{{params.title}} {{params.first_pre}}{{params.first_root}} {{params.last_pre}}{{params.last_root}} {{params.trailer}}')
self.redis.lpush('hobgoblinname_shortname_template', '{{params.first_pre}}{{params.first_root}}')
self.redis.lpush('hobgoblinname_formalname_template', '{{params.title}} {{params.last_pre}}{{params.last_root}}')

set hobgoblinname_first_pre_chance 100
set hobgoblinname_first_root_chance 100
set hobgoblinname_last_pre_chance 100
set hobgoblinname_last_root_chance 100




self.redis.lpush('hobgoblinname_first_pre', 'Ba')
self.redis.lpush('hobgoblinname_first_pre', 'Be')
self.redis.lpush('hobgoblinname_first_pre', 'Bo')
self.redis.lpush('hobgoblinname_first_pre', 'Da')
self.redis.lpush('hobgoblinname_first_pre', 'De')
self.redis.lpush('hobgoblinname_first_pre', 'Do')
self.redis.lpush('hobgoblinname_first_pre', 'Fa')
self.redis.lpush('hobgoblinname_first_pre', 'Fe')
self.redis.lpush('hobgoblinname_first_pre', 'Fo')
self.redis.lpush('hobgoblinname_first_pre', 'Fu')
self.redis.lpush('hobgoblinname_first_pre', 'Ga')
self.redis.lpush('hobgoblinname_first_pre', 'Ge')
self.redis.lpush('hobgoblinname_first_pre', 'Go')
self.redis.lpush('hobgoblinname_first_pre', 'In')
self.redis.lpush('hobgoblinname_first_pre', 'Ka')
self.redis.lpush('hobgoblinname_first_pre', 'Ke')
self.redis.lpush('hobgoblinname_first_pre', 'Ko')
self.redis.lpush('hobgoblinname_first_pre', 'La')
self.redis.lpush('hobgoblinname_first_pre', 'Lo')
self.redis.lpush('hobgoblinname_first_pre', 'Ma')
self.redis.lpush('hobgoblinname_first_pre', 'Me')
self.redis.lpush('hobgoblinname_first_pre', 'Mo')
self.redis.lpush('hobgoblinname_first_pre', 'Na')
self.redis.lpush('hobgoblinname_first_pre', 'Ne')
self.redis.lpush('hobgoblinname_first_pre', 'No')
self.redis.lpush('hobgoblinname_first_pre', 'Ol')
self.redis.lpush('hobgoblinname_first_pre', 'Or')
self.redis.lpush('hobgoblinname_first_pre', 'Ox')
self.redis.lpush('hobgoblinname_first_pre', 'Pa')
self.redis.lpush('hobgoblinname_first_pre', 'Pe')
self.redis.lpush('hobgoblinname_first_pre', 'Po')
self.redis.lpush('hobgoblinname_first_pre', 'Ra')
self.redis.lpush('hobgoblinname_first_pre', 'Re')
self.redis.lpush('hobgoblinname_first_pre', 'Ro')
self.redis.lpush('hobgoblinname_first_pre', 'Sa')
self.redis.lpush('hobgoblinname_first_pre', 'Se')
self.redis.lpush('hobgoblinname_first_pre', 'So')
self.redis.lpush('hobgoblinname_first_pre', 'Ta')
self.redis.lpush('hobgoblinname_first_pre', 'Te')
self.redis.lpush('hobgoblinname_first_pre', 'To')
self.redis.lpush('hobgoblinname_first_pre', 'Ul')
self.redis.lpush('hobgoblinname_first_pre', 'Ux')
self.redis.lpush('hobgoblinname_first_pre', 'Va')
self.redis.lpush('hobgoblinname_first_pre', 'Ve')
self.redis.lpush('hobgoblinname_first_pre', 'Vo')
self.redis.lpush('hobgoblinname_first_pre', 'Wo')
self.redis.lpush('hobgoblinname_first_pre', 'Xa')
self.redis.lpush('hobgoblinname_first_pre', 'Xo')
self.redis.lpush('hobgoblinname_first_pre', 'Za')
self.redis.lpush('hobgoblinname_first_pre', 'Ze')
self.redis.lpush('hobgoblinname_first_pre', 'Zo')

self.redis.lpush('hobgoblinname_first_root', 'arg')
self.redis.lpush('hobgoblinname_first_root', 'ck')
self.redis.lpush('hobgoblinname_first_root', 'erg')
self.redis.lpush('hobgoblinname_first_root', 'f')
self.redis.lpush('hobgoblinname_first_root', 'g')
self.redis.lpush('hobgoblinname_first_root', 'gg')
self.redis.lpush('hobgoblinname_first_root', 'k')
self.redis.lpush('hobgoblinname_first_root', 'kk')
self.redis.lpush('hobgoblinname_first_root', 'lenf')
self.redis.lpush('hobgoblinname_first_root', 'lf')
self.redis.lpush('hobgoblinname_first_root', 'lg')
self.redis.lpush('hobgoblinname_first_root', 'lk')
self.redis.lpush('hobgoblinname_first_root', 'lnf')
self.redis.lpush('hobgoblinname_first_root', 'm')
self.redis.lpush('hobgoblinname_first_root', 'nf')
self.redis.lpush('hobgoblinname_first_root', 'nn')
self.redis.lpush('hobgoblinname_first_root', 'og')
self.redis.lpush('hobgoblinname_first_root', 'r')
self.redis.lpush('hobgoblinname_first_root', 'rd')
self.redis.lpush('hobgoblinname_first_root', 'rez')
self.redis.lpush('hobgoblinname_first_root', 'rg')
self.redis.lpush('hobgoblinname_first_root', 'rof')
self.redis.lpush('hobgoblinname_first_root', 'rog')
self.redis.lpush('hobgoblinname_first_root', 'rr')
self.redis.lpush('hobgoblinname_first_root', 't')
self.redis.lpush('hobgoblinname_first_root', 'tt')
self.redis.lpush('hobgoblinname_first_root', 'x')
self.redis.lpush('hobgoblinname_first_root', 'z')
self.redis.lpush('hobgoblinname_first_root', 'zar')










self.redis.lpush('hobgoblinname_last_pre', 'Bihg')
self.redis.lpush('hobgoblinname_last_pre', 'Blaad')
self.redis.lpush('hobgoblinname_last_pre', 'Braun')
self.redis.lpush('hobgoblinname_last_pre', 'Cleevr')
self.redis.lpush('hobgoblinname_last_pre', 'Damm')
self.redis.lpush('hobgoblinname_last_pre', 'Dakk')
self.redis.lpush('hobgoblinname_last_pre', 'Dred')
self.redis.lpush('hobgoblinname_last_pre', 'Evel')
self.redis.lpush('hobgoblinname_last_pre', 'Fuel')
self.redis.lpush('hobgoblinname_last_pre', 'Ghasht')
self.redis.lpush('hobgoblinname_last_pre', 'Gint')
self.redis.lpush('hobgoblinname_last_pre', 'Gret')
self.redis.lpush('hobgoblinname_last_pre', 'Grat')
self.redis.lpush('hobgoblinname_last_pre', 'Irn')
self.redis.lpush('hobgoblinname_last_pre', 'Laf')
self.redis.lpush('hobgoblinname_last_pre', 'Metl')
self.redis.lpush('hobgoblinname_last_pre', 'Mital')
self.redis.lpush('hobgoblinname_last_pre', 'Nit')
self.redis.lpush('hobgoblinname_last_pre', 'Ahgr')
self.redis.lpush('hobgoblinname_last_pre', 'Uze')
self.redis.lpush('hobgoblinname_last_pre', 'Rent')
self.redis.lpush('hobgoblinname_last_pre', 'Rahk')
self.redis.lpush('hobgoblinname_last_pre', 'Wurm')

self.redis.lpush('hobgoblinname_last_root', 'bashr')
self.redis.lpush('hobgoblinname_last_root', 'beast')
self.redis.lpush('hobgoblinname_last_root', 'boone')
self.redis.lpush('hobgoblinname_last_root', 'cuttr')
self.redis.lpush('hobgoblinname_last_root', 'mat')
self.redis.lpush('hobgoblinname_last_root', 'deth')
self.redis.lpush('hobgoblinname_last_root', 'duum')
self.redis.lpush('hobgoblinname_last_root', 'fery')
self.redis.lpush('hobgoblinname_last_root', 'glume')
self.redis.lpush('hobgoblinname_last_root', 'hend')
self.redis.lpush('hobgoblinname_last_root', 'hast')
self.redis.lpush('hobgoblinname_last_root', 'hule')
self.redis.lpush('hobgoblinname_last_root', 'kell')
self.redis.lpush('hobgoblinname_last_root', 'maw')
self.redis.lpush('hobgoblinname_last_root', 'mauth')
self.redis.lpush('hobgoblinname_last_root', 'murdr')
self.redis.lpush('hobgoblinname_last_root', 'rendir')
self.redis.lpush('hobgoblinname_last_root', 'rawt')
self.redis.lpush('hobgoblinname_last_root', 'shadwr')
self.redis.lpush('hobgoblinname_last_root', 'shreddir')
self.redis.lpush('hobgoblinname_last_root', 'sley')
self.redis.lpush('hobgoblinname_last_root', 'stomch')
self.redis.lpush('hobgoblinname_last_root', 'wizer')



