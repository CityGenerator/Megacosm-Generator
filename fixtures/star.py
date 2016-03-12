def import_fixtures(self):
    self.redis.lpush('starname_fullname_template', '{{params.pre}}{{params.root}}{{params.post}}')
    self.redis.lpush('starname_shortname_template', '{{params.fullname}}')
    self.redis.lpush('starname_formalname_template', '{{params.fullname}}')
    self.redis.lpush('starname_pre', 'Kro')
    self.redis.lpush('starname_root', 'j')
    self.redis.lpush('starname_post', 'el')

    self.redis.lpush('starposition', '{"name": "companion",    "x":-150,    "y":4,  "z":4  }' )
    self.redis.lpush('starposition', '{"name": "companion2",    "x":-150,    "y":-4,  "z":4  }' )
