#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fully test this module's functionality through the use of fixtures."""

from importer import Importer
import unittest
import fakeredis
import json
# from fixtures import artwork, gem, npc, motivation, phobia, deity


class TestImporter(unittest.TestCase):
    """ Test the Iporter Class"""
    def setUp(self):
        """ Set up the required fixtures """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        self.imp = Importer(self.redis)

    def tearDown(self):
        """ Clean up any changes from the last run. """
        self.imp = None
        self.redis.flushall()

    def test_importer_init(self):
        """ Create an importer object. """
        imp = Importer(self.redis)
        self.assertEqual(imp.command_count, 0)
        self.assertEqual(imp.json_validate, 0)
        self.assertEqual(imp.image_count, 0)

    def test_parse_data_file(self):
        self.assertEqual(self.imp.image_count, 0)
        # TODO

    def test_process_set(self):
        # self
        imp = Importer(self.redis)
        imp.process_set("foo bar")
        self.assertEqual(self.redis.get("foo"), "bar")
        self.redis.flushall()

    def test_process_hset(self):
        # self
        imp = Importer(self.redis)
        hsetvar = """test type1 { "name":"type one", "description":"a test"  }"""
        imp.process_hset(hsetvar)
        self.assertEqual(self.redis.hget("test", "type1"), '{ "name":"type one", "description":"a test"  }')

    def test_process_hset_bad_data(self):
        # self
        imp = Importer(self.redis)
        bad_json = """test type1 "name":"type one", 's;'"""
        with self.assertRaises(json.JSONDecodeError) as cm:
            imp.process_hset(bad_json)
        
        #self.assertEqual(self.redis.hget("test", "type1"), '')



    # def test_process_hset(self, args):
    # def test_process_zadd(self, args):
    # def test_validate_json(self, value):
    # def test_create_geomorphimage_record(self, image_name):
    # def test_create_dungeonbackground_record(self, image_name):
    # def test_create_dungeondecoration_record(self, image_name):
    # def vis_ascii(s):


if __name__ == '__main__':
    unittest.main()
