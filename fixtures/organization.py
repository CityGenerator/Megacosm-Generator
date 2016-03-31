#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""

    self.redis.lpush('organization_identification', 'with difficulty')
    self.redis.lpush('organization_kind', 'crime ring')
    self.redis.lpush('organizationname_post', 'gua')
    self.redis.lpush('organizationname_pre', 'Yak')
    self.redis.lpush('organizationname_root', 'u')
    self.redis.lpush('organizationname_trailer', 'Dragons')
    self.redis.lpush('organization_powertype', 'gambling')
    self.redis.lpush('organization_template', "{{params.leader.name.shortname}}'s {{params.kind|title}}")
    self.redis.zadd('organization_adaptability', '{"name":"stay ahead of new development",    "score":100  }', 100)
    self.redis.zadd('organization_age', '{"name":"ancient",       "score":100  }', 100)
    self.redis.zadd('organization_entry', '{"name":"impossible",      "score":100  }', 100)
    self.redis.zadd('organization_failure', '{ "name":"better guidance and training",  "score":100 }', 100)
    self.redis.zadd('organization_leadership', '{ "name":"strong",     "score":100 }', 100)
    self.redis.zadd('organization_legal', '{"name":"legitimate",   "score":100   }', 100)
    self.redis.zadd('organization_morale', '{"name":"encouraged",          "score":100  }', 100)
    self.redis.zadd('organization_regulation', '{ "name":"strictly enforced",  "score":100 }', 100)
    self.redis.zadd('organization_rules', '{ "name":"rigidly",    "score":100 }', 100)
    self.redis.zadd('organization_size', '{ "name":"world",       "score":100 }', 100)
    self.redis.zadd('organization_stability', '{ "name":"are rock solid",     "score":100 }', 100)
    self.redis.zadd('organization_structure', '{ "name":"rigidly",    "score":100 }', 100)
    self.redis.zadd('organization_teamwork', '{ "name":"as a well oiled machine",         "score":100 }', 100)
    self.redis.zadd('organization_violence', '{"name":"passive",       "score":100  }', 100)
    self.redis.zadd('organization_visibility', '{ "name":"well known",            "score":100 }', 100)
    self.redis.lpush('organizationname_fullname_template', 'The {{params.pre}}{{params.root}}{{params.post}} {{params.trailer}}')
    self.redis.lpush('organizationname_shortname_template', 'The {{params.kind|title}}')
    self.redis.lpush('organizationname_formalname_template', '{{params.fullname}}')

