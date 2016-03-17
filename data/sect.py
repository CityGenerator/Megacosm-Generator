#

#    <acceptance><!--Sect members are see as _____ by the faithful -->
ZADD sect_acceptance   5 {"name":"heretical",  "score":5   } 
ZADD sect_acceptance  10 {"name":"blasphemous",  "score":10   } 
ZADD sect_acceptance  15 {"name":"sectarian",  "score":15   } 
ZADD sect_acceptance  20 {"name":"rebellious",  "score":20   } 
ZADD sect_acceptance  25 {"name":"defecting",  "score":25   } 
ZADD sect_acceptance  30 {"name":"dissenting",  "score":30   } 
ZADD sect_acceptance  35 {"name":"agitating",  "score":35   } 
ZADD sect_acceptance  40 {"name":"deviant",  "score":40   } 
ZADD sect_acceptance  45 {"name":"mislead",  "score":45   } 
ZADD sect_acceptance  50 {"name":"non-confirming",  "score":50   } 
ZADD sect_acceptance  55 {"name":"faithful",  "score":55   } 
ZADD sect_acceptance  60 {"name":"honorable",  "score":60   } 
ZADD sect_acceptance  65 {"name":"noble",  "score":65   } 
ZADD sect_acceptance  70 {"name":"loyal",  "score":70   } 
ZADD sect_acceptance  75 {"name":"dutiful",  "score":75   } 
ZADD sect_acceptance  80 {"name":"reverent",  "score":80   } 
ZADD sect_acceptance  85 {"name":"devout",  "score":85   } 
ZADD sect_acceptance  90 {"name":"virtuous",  "score":90   } 
ZADD sect_acceptance  95 {"name":"righteous",  "score":95   } 
ZADD sect_acceptance 100 {"name":"saintly",  "score":100   } 
    
#    <secttype>
self.redis.lpush('sect_kind', 'brotherhood')
self.redis.lpush('sect_kind', 'chapter')
self.redis.lpush('sect_kind', 'clan')
self.redis.lpush('sect_kind', 'coven')
self.redis.lpush('sect_kind', 'cult')
self.redis.lpush('sect_kind', 'faction')
self.redis.lpush('sect_kind', 'following')
self.redis.lpush('sect_kind', 'order')
self.redis.lpush('sect_kind', 'sect')
self.redis.lpush('sect_kind', 'society')




# The ___________ _________ _______ are a beloved sect that focuses on stray cats.

SET   name_secttitle_chance 30
self.redis.lpush('name_secttitle', 'Order of the ')
self.redis.lpush('name_secttitle', 'Message of the')
self.redis.lpush('name_secttitle', 'Pilgrims of ')
self.redis.lpush('name_secttitle', 'Brethren of')
self.redis.lpush('name_secttitle', 'Church of the ')
self.redis.lpush('name_secttitle', 'Reformed')
self.redis.lpush('name_secttitle', 'Sacred')
self.redis.lpush('name_secttitle', 'Ancient Order of')

self.redis.lpush('name_sectpre', 'Prima')
self.redis.lpush('name_sectpre', 'Kanno')
self.redis.lpush('name_sectpre', 'Eani')
self.redis.lpush('name_sectpre', 'Shaki')
self.redis.lpush('name_sectpre', 'Orei')
self.redis.lpush('name_sectpre', 'Ordi')
self.redis.lpush('name_sectpre', 'Kabba')
self.redis.lpush('name_sectpre', 'Delphi')
self.redis.lpush('name_sectpre', 'Sera')
self.redis.lpush('name_sectpre', 'Anna')
self.redis.lpush('name_sectpre', 'Brudo')
self.redis.lpush('name_sectpre', 'Diani')
self.redis.lpush('name_sectpre', 'Free')
self.redis.lpush('name_sectpre', 'Fera')
self.redis.lpush('name_sectpre', 'Gonko')
self.redis.lpush('name_sectpre', 'Lecto')

SET   name_sectpost_chance 80
self.redis.lpush('name_sectroot', 'tav')
self.redis.lpush('name_sectroot', 'dar')
self.redis.lpush('name_sectroot', 'bor')
self.redis.lpush('name_sectroot', 'c')
self.redis.lpush('name_sectroot', 'bal')
self.redis.lpush('name_sectroot', 'damp')
self.redis.lpush('name_sectroot', 'moto')
self.redis.lpush('name_sectroot', 'costal')
self.redis.lpush('name_sectroot', 'far')
self.redis.lpush('name_sectroot', 'rik')
self.redis.lpush('name_sectroot', 'versal')
self.redis.lpush('name_sectroot', 'dun')

SET   name_sectpost_chance 30
self.redis.lpush('name_sectpost', 'ism')
self.redis.lpush('name_sectpost', 'um')
self.redis.lpush('name_sectpost', 'aj')
self.redis.lpush('name_sectpost', 'ic')
self.redis.lpush('name_sectpost', 'ites')
self.redis.lpush('name_sectpost', 'oxy')
self.redis.lpush('name_sectpost', 'ogy')
self.redis.lpush('name_sectpost', 'ons')
self.redis.lpush('name_sectpost', 'ists')


SET   name_secttrailer_chance 30
self.redis.lpush('name_secttrailer', 'Movement')
self.redis.lpush('name_secttrailer', 'Temple')
self.redis.lpush('name_secttrailer', 'Society')
self.redis.lpush('name_secttrailer', 'Fellowship')
self.redis.lpush('name_secttrailer', 'Witnesses')
self.redis.lpush('name_secttrailer', 'Followers')
self.redis.lpush('name_secttrailer', 'Radiance')
