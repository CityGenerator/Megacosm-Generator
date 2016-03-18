def import_fixtures(self):
    self.redis.zadd('event_magnitude', '{  "name":"of dire importance",            "score":100      }', 100)
    self.redis.lpush('eventfestival_variety', 'a trade')
    self.redis.lpush('eventdisaster_variety', 'animal infestation')
    self.redis.lpush('event_kind', 'disaster')
    self.redis.lpush('event_template', "{{params.variety }} {{params.kind}}, which is {{params.magnitude['name']}} to the people in the area.")

