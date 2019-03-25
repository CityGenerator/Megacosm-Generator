#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

#These are used to test the abstract generator's functionality.
def import_fixtures(self):
    """ Create simple fixture entries..."""
    #Used for testing chances that always happen
    self.redis.zadd('bogus_size', {'{ "name":"tiny", "multiplier":0.5, "score":1 }': 1.0})
    self.redis.zadd('bogus_size', {'{ "name":"large", "multiplier":1.0, "score":40 }': 40.0})
    self.redis.zadd('bogus_size', {'{ "name":"giant", "multiplier":2.0, "score":100 }': 100.0})
    self.redis.lpush('bogus_mylist', 1)
    self.redis.lpush('bogus_mylist', 2)
    self.redis.lpush('bogus_mylist', 3)
    self.redis.lpush('bogus_mylist', 4)

    self.redis.set('bogus_booyahfeature', 'Booyah')

    self.redis.lpush('other_misslist', 'a')
    self.redis.lpush('other_misslist', 'b')
    self.redis.set('chnc_size_chance', 101)
    self.redis.zadd('chnc_size', {'{ "name":"tiny", "multiplier":0.5, "score":1 }': 1.0})
    self.redis.zadd('chnc_size', {'{ "name":"large", "multiplier":1.0, "score":40 }': 40.0})
    self.redis.zadd('chnc_size', {'{ "name":"giant", "multiplier":2.0, "score":100 }': 100.0})
    self.redis.set('chnc_mylist_chance', 101)
    self.redis.lpush('chnc_mylist', 1)
    self.redis.lpush('chnc_mylist', 2)
    self.redis.lpush('chnc_mylist', 3)

    #Used for testing chances that never happen
    self.redis.set('nochnc_size_chance', 0)
    self.redis.zadd('nochnc_size', {'{ "name":"tiny", "multiplier":0.5, "score":1 }': 1.0})
    self.redis.zadd('nochnc_size', {'{ "name":"large", "multiplier":1.0, "score":40 }': 40.0})
    self.redis.zadd('nochnc_size', {'{ "name":"giant", "multiplier":2.0, "score":100 }': 100.0})
    self.redis.set('nochnc_mylist_chance', 0)
    self.redis.lpush('nochnc_mylist', 1)
    self.redis.lpush('nochnc_mylist', 2)
    self.redis.lpush('nochnc_mylist', 3)

    self.redis.lpush('myknd_kind', 'big')
    self.redis.lpush('myknd_kind', 'med')
    self.redis.lpush('myknd_kind', 'small')
    self.redis.hset('myknd_kind_description', 'small', '{"name":"Small", "description":"A Small thing"}')
    self.redis.hset('myknd_kind_description', 'med', '{"name":"Medium", "description":"A Medium thing"}')
    self.redis.hset('myknd_kind_description', 'big', '{"name":"Big", "description":"A Big thing"}')

    self.redis.lpush('mybadknd_kind', 'small')
    self.redis.hset('mybadknd_kind_description', 'small', 'whoops this is bad')

    self.redis.zadd('incompleteset_size', {'{ "name":"tiny", "multiplier":0.5, "score":1 }': 1.0})

    self.redis.zadd('badjson_widget', {'waffles not json': 100.0})

    import_city_name_fixtures(self)

def import_city_name_fixtures(self):
    """ import fixtures for name testing."""
    self.redis.set('fullcitytitle_chance', 100)
    self.redis.set('fullcitypre_chance', 100)
    self.redis.set('fullcitytrailer_chance', 100)

    self.redis.lpush('fullcitytitle', 'Alta')
    self.redis.lpush('fullcitytitle', 'Bad')

    self.redis.lpush('fullcitypre', 'De')
    self.redis.lpush('fullcitypre', 'Le')
    self.redis.lpush('fullcityroot', 'Ack')
    self.redis.lpush('fullcityroot', 'Ad')
    self.redis.lpush('fullcitypost', 'thistle')
    self.redis.lpush('fullcitypost', 'wood')
    self.redis.lpush('fullcitytrailer', 'Mount')
    self.redis.lpush('fullcitytrailer', 'Park')
    self.redis.set('mincitytitle_chance', 0)
    self.redis.set('mincitypre_chance', 0)
    self.redis.set('mincitytrailer_chance', 0)

    self.redis.lpush('mincitytitle', 'Alta')
    self.redis.lpush('mincitytitle', 'Bad')

    self.redis.lpush('mincitypre', 'De')
    self.redis.lpush('mincitypre', 'Le')
    self.redis.lpush('mincityroot', 'Ack')
    self.redis.lpush('mincityroot', 'Ad')
    self.redis.lpush('mincitypost', 'thistle')
    self.redis.lpush('mincitypost', 'wood')
    self.redis.lpush('mincitytrailer', 'Mount')
    self.redis.lpush('mincitytrailer', 'Park')


