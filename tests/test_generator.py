#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Generator
import unittest2 as unittest
import json
from mock import Mock, patch, MagicMock

import fakeredis
import fixtures
from config import TestConfiguration
from pprint import pprint

class TestGenerator(unittest.TestCase):

    def setUp(self):
        self.redis = fakeredis.FakeRedis()
        fixtures.generator.import_fixtures(self)

    def tearDown(self):
        self.redis.flushall()

    def test_missing_feature(self):
        """  Test a feature that doesn't exist."""

        generator = Generator(self.redis)
        with self.assertRaises(AttributeError):
            generator.bananasmissingfeature

    def test_static_seed(self):
        ''' Ensure a static seed can be set. '''
        generator = Generator(self.redis, {'seed':1337})
        self.assertEqual(generator.seed, 1337)

    def test_randomseed(self):
        ''' ensure a see that is an integer is created. '''
        generator = Generator(self.redis)
        self.assertIs(type(generator.seed), int)
        #FIXME these were taken from megacosm.util.Seed.Seed values. Don't hardcode them.
        self.assertGreaterEqual(generator.seed,1)
        self.assertLessEqual(generator.seed, 10000000)

    def test_select_by_roll(self):
        ''' Select the bogus_size greater than or equal to the rolled number.'''
        generator = Generator(self.redis, {'seed': 1007, 'bogus_size_roll': 37})
        self.assertEqual({u'score': 40, u'name': u'large', u'multiplier': 1.0} ,generator.select_by_roll('bogus_size'))


    def test_select_by_roll_key_doesnt_exist(self):
        ''' Try to select funion for a role, only to find it doesn't exist.'''
        generator = Generator(self.redis)
        with self.assertRaisesRegexp(ValueError, 'The key funion does not exist.'):
            generator.select_by_roll('funion')
        self.assertNotEqual('', generator.select_by_roll('bogus_size'))

    def test_select_by_roll_highmin(self):
        ''' Test rolling outside our limits of 0-100. '''
        generator = Generator(self.redis, { 'bogus_size_roll': 1037})

        self.assertEquals({u'score': 100, u'name': u'giant', u'multiplier': 2.0},
                          generator.select_by_roll('bogus_size'))
        generator = Generator(self.redis, {'bogus_size_roll': -1037})
        self.assertEquals({u'score': 1, u'name': u'tiny', u'multiplier': 0.5},
                          generator.select_by_roll('bogus_size'))

    def test_select_by_roll_key_wrong_type(self):
        '''Intentionally try to roll on the wrong datatype.'''
        generator = Generator(self.redis, {'seed': 1007, 'bogus_mylist_roll': 37})
        with self.assertRaisesRegexp(Exception,
                                     "The key bogus_mylist is not a zset; the type is list."):
            generator.select_by_roll('bogus_mylist')

    def test_random_list_value(self):
        ''' Find a random list value '''
        generator = Generator(self.redis)
        self.assertIn(generator.rand_value('bogus_mylist'), ['1','2','3','4'])

    def test_rand_value_key_wrong_type(self):
        ''' Try to use a zset as a list. '''
        generator = Generator(self.redis)
        with self.assertRaisesRegexp(Exception,
                                     "the key \(bogus_size\) doesn't appear to exist or isn't a list \(zset\)."):
            generator.rand_value('bogus_size')

    def test_rand_value_key_doesnt_exist(self):
        ''' Try to generate a rand_value from a key that doesn't exist at all. '''
        generator = Generator(self.redis)
        with self.assertRaisesRegexp(Exception, "the key \(somekey\) doesn't appear to exist or isn't a list"):
            generator.rand_value('somekey')

    def test_dump_vars(self):
        '''Ensure that the generator dumps properly. '''
        generator = Generator(self.redis, {'seed': 1007})
        self.assertIn('seed', generator.dump_vars())
        self.assertEqual(vars(generator), generator.dump_vars())

    def test_generate_features(self):
        '''test Feature Generation from a namekey'''
        generator = Generator(self.redis, {'bogus_size_roll': 1})
        self.assertNotIn('bogus', generator.dump_vars())
        generator.generate_features('bogus')
        self.assertIn('booyahfeature', generator.dump_vars())
        self.assertEqual('Booyah',generator.booyahfeature)
        self.assertEqual('tiny', generator.size['name'])
        '''Ensure misslist from other was not included. '''
        with self.assertRaises(AttributeError):
            generator.misslist

    def test_generate_feature_chance_100(self):
        '''test Feature Generation from a namekey with 100% chance.'''
        generator = Generator(self.redis, {'chnc_size_roll': 1})
        self.assertNotIn('chnc', generator.dump_vars())
        generator.generate_features('chnc')
        self.assertIn('mylist', generator.dump_vars())
        self.assertIn(generator.mylist, ['1','2','3','4'])
        self.assertEqual('tiny', generator.size['name'])
        '''Ensure misslist from other was not included. '''
        with self.assertRaises(AttributeError):
            generator.misslist

    def test_generate_feature_chance_roll(self):
        '''test Feature Generation from a namekey with 0% chance.'''
        generator = Generator(self.redis, {'nochnc_size_roll': 1, 'nochnc_size_chance':5,'nochnc_mylist_chance':5 })
        self.assertNotIn('mylist_chance', generator.dump_vars())
        generator.generate_features('nochnc')
        self.assertIn('mylist_chance', generator.dump_vars())

        '''Ensure misslist from other was not included. '''
        with self.assertRaises(AttributeError):
            generator.misslist

    def test_kind_description(self):
        '''Ensure that kind description JSON is loaded properly.'''
        generator = Generator(self.redis)
        self.assertNotIn('kind', generator.dump_vars())
        generator.generate_features('myknd')
        self.assertIn('kind', generator.dump_vars())


    def test_bad_kind_description(self):
        '''Ensure that kind description with bad JSON throws an error.'''
        generator = Generator(self.redis)
        self.assertNotIn('kind', generator.dump_vars())
        with self.assertRaises(ValueError):
            generator.generate_features('mybadknd')


    def test_error_handling_roll(self):
        '''Ensure that select_by_roll handles errors properly.'''
        generator = Generator(self.redis, {'incompleteset_size_roll':10 })


        with self.assertRaises(ValueError) as cm:
            generator.select_by_roll('derpderp_size')
        self.assertEqual(str(cm.exception), "The key derpderp_size does not exist.")


        with self.assertRaises(LookupError) as cm:
            generator.select_by_roll('incompleteset_size')
        self.assertEqual(str(cm.exception), 'The key (incompleteset_size) appears to be empty for a roll of 10- This should never happen.')

        with self.assertRaises(ValueError) as cm:
            generator.select_by_roll('badjson_widget')
        self.assertEqual(str(cm.exception), '("JSON parsing error: Couldn\'t read json", \'waffles not json\')')

    def test_bogus_generator(self):
        '''Ensure that a fullname is generated.'''
        generator = Generator(self.redis,{},'bogus')
        self.assertIn('booyahfeature',generator.dump_vars())
        
    def test_generate_feature(self):
        '''Ensure that a fullname is generated.'''
        generator = Generator(self.redis,{'mylist':'foobar'})
        generator.generate_feature( 'bogus', 'bogus_mylist')

        generator = Generator(self.redis,{'kind':'small', 'kind_description':'foobar'})
        generator.generate_feature( 'myknd', 'myknd_kind')


    def test_render_template(self):
        '''Ensure that a fullname is generated.'''
        generator = Generator(self.redis,{'test_value':'a bigger string'})    
        self.assertEqual('A large string, a bigger string.',generator.render_template("A large string, {{params.test_value}}."))
