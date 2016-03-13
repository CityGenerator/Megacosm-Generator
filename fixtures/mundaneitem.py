def import_fixtures(self):
    self.redis.zadd('mundaneitem_quality', '{"name":"excellent","score":100 }', 100)
    self.redis.zadd('mundaneitem_repair', '{"name":"in pristine condition",     "score":100 }', 100)
    self.redis.lpush('mundaneitem_kind', 'wool tunic')

