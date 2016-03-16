    
def import_fixtures(self):


    
    self.redis.lpush('currency_back','dragon')
    self.redis.lpush('currency_edges','ridges')
    self.redis.lpush('currency_front',"man's face")
    self.redis.lpush('currency_material','wood')
    self.redis.lpush('currencyname_formalname_template', '{{params.fullname}}')
    self.redis.lpush('currencyname_fullname_template', '{{params.pre}}{{params.root}}{{params.post}}')
    self.redis.lpush('currencyname_post','abbi')    
    self.redis.lpush('currencyname_pre','yua')
    self.redis.lpush('currencyname_root','fel')
    self.redis.lpush('currencyname_shortname_template', '{{params.fullname}}')
    self.redis.lpush('currency_shape','square')
    self.redis.lpush('currency_template', "{{params.name.fullname|article|title}} is {{params.weight['name'] | article}}, {{params.value['name']}} coin that is common in the {{params.scope['name']}}. It is {{params.size['name']}}, {{params.shape}}, and made of {{params.material}}. The coins are covered with {{params.detail['name']}} designs.")
    self.redis.zadd('currency_amount','{ "name":"a large pile of",    "min":100,  "max":3000, "score":100 }',100)
    self.redis.zadd('currency_detail','{ "name":"unmistakable" , "score":100  }',100)
    self.redis.zadd('currency_scope','{ "name":"continent",   "score":100  }',100)
    self.redis.zadd('currency_size','{ "name":"giant (40mm )"    , "score":100 }',100)
    self.redis.zadd('currency_value','{ "name":"priceless",         "score":100  }',100)
    self.redis.zadd('currency_weight','{ "name":"hefty" , "score":100  }',100)
    
    
    
    
    
    
    
    
    
    
    
    
    
