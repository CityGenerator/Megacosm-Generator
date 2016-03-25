
def import_fixtures(self):
    self.redis.lpush('artwork_metal', 'bronze')
    self.redis.lpush( 'artworkweapon_subkind', 'spear')
    self.redis.lpush( 'artwork_kind', 'weapon')
    self.redis.lpush( 'artworkweapon_template', 'A ceremonial {{params.metal}} {{params.subkind}} with a {{params.gem.kind_description["name"]}} in the pommel')
