#

# The party upset _________. __________ swore vengeance against the sheriff.
self.redis.lpush('organizationname_fullname_template', '{{params.leader.shortname}}\'s {{params.kind|title}}')
self.redis.lpush('organizationname_fullname_template', '{{params.pre}}{{params.root}}{{params.post}}\'s {{params.kind|title}}')
self.redis.lpush('organizationname_fullname_template', 'The {{params.leader.formalname}} {{params.kind|title}}')
self.redis.lpush('organizationname_fullname_template', 'The {{params.leader.formalname}} {{params.trailer|title}}')
self.redis.lpush('organizationname_fullname_template', 'The {{params.pre}}{{params.root}}{{params.post}} {{params.kind|title}}')
self.redis.lpush('organizationname_fullname_template', 'The {{params.pre}}{{params.root}}{{params.post}} {{params.trailer}}')


#I can\'t belive you angered ____
self.redis.lpush('organizationname_shortname_template', 'The {{params.kind|title}}')
self.redis.lpush('organizationname_shortname_template', 'The {{params.trailer}}')
self.redis.lpush('organizationname_shortname_template', 'The {{params.pre}}{{params.root}}{{params.post}}')

self.redis.lpush('organizationname_formalname_template', '{{params.fullname}}')

SET   organizationname_post_chance 40

self.redis.lpush('organizationname_pre', 'Af')
self.redis.lpush('organizationname_pre', 'Ban')
self.redis.lpush('organizationname_pre', 'Blood')
self.redis.lpush('organizationname_pre', 'Blud')
self.redis.lpush('organizationname_pre', 'Gwan')
self.redis.lpush('organizationname_pre', 'Tef')
self.redis.lpush('organizationname_pre', 'Yak')

self.redis.lpush('organizationname_root', 'for')
self.redis.lpush('organizationname_root', 'mal')
self.redis.lpush('organizationname_root', 'u')

self.redis.lpush('organizationname_post', 'ket')
self.redis.lpush('organizationname_post', 'met')
self.redis.lpush('organizationname_post', 'set')
self.redis.lpush('organizationname_post', 'pel')
self.redis.lpush('organizationname_post', 'za')
self.redis.lpush('organizationname_post', 'gua')


self.redis.lpush('organizationname_trailer', 'Angels')
self.redis.lpush('organizationname_trailer', 'Boys')
self.redis.lpush('organizationname_trailer', 'Crew')
self.redis.lpush('organizationname_trailer', 'Dragons')
self.redis.lpush('organizationname_trailer', 'Hand')
self.redis.lpush('organizationname_trailer', 'Horsemen')
self.redis.lpush('organizationname_trailer', 'Hustlers')
self.redis.lpush('organizationname_trailer', 'Rats')
self.redis.lpush('organizationname_trailer', 'Saints')


