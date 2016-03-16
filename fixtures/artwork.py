
def import_fixtures(self):
    self.redis.lpush('artwork_metal', 'bronze')
    self.redis.lpush('artwork_weapon', 'dagger')
    self.redis.lpush('artwork_item', 'harp')
    self.redis.lpush('artwork_item_material', 'ivory')
    self.redis.lpush('artwork_item_decoration', 'bear')
    self.redis.lpush('artwork_jewelry', 'ring')
    self.redis.lpush('artwork_cloth_item', 'glove')
    self.redis.lpush('artwork_cloth_material', 'silk')
    self.redis.lpush('artwork_template', "a necklace of {{params.gem.size}} {{params.gem.kind_description['name']|pluralize(2)}}")

