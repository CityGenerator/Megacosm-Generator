#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Name
import unittest2 as unittest

from pprint import pprint

import redis
from config import TestConfiguration


class TestName(unittest.TestCase):

    def setUp(self):
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def tearDown(self):
        """Tear stuff Down."""
        #self.redis.flushall()

    def test_races(self):
        """  """
        for race in self.redis.lrange('npc_race',0,-1):
            name = Name(self.redis, race, {'title':'Mr.'})
            self.assertEqual(race, str(name.namesource))
            print "%s:  %s | %s | %s" %(race, name.fullname, name.shortname, name.formalname)
            self.assertIn('{{params.title}} ', str(name.fullname_template))
            self.assertIn(' {{params.trailer}}', str(name.fullname_template))
            self.assertNotIn('{{', str(name.fullname))
            self.assertNotIn('}}', str(name.fullname))
            self.assertNotIn('params', str(name.fullname))
            self.assertNotIn('{{', str(name.shortname))
            self.assertNotIn('}}', str(name.shortname))
            self.assertNotIn('params', str(name.shortname))
            self.assertNotIn('{{', str(name.formalname))
            self.assertNotIn('}}', str(name.formalname))
            self.assertNotIn('params', str(name.formalname))
    def test_business(self):
        """  """
        name = Name(self.redis, 'business', {'businesstype':'Butcher'})
        self.assertEqual('business', str(name.namesource))
        print "business:  %s | %s | %s" %( name.fullname, name.shortname, name.formalname)
        self.assertIn(' {{params.noun}} ', str(name.fullname_template))
        self.assertIn('{{params.adjective}} ', str(name.fullname_template))
        self.assertNotIn('{{', str(name.fullname))
        self.assertNotIn('}}', str(name.fullname))
        self.assertNotIn('params', str(name.fullname))
        self.assertNotIn('{{', str(name.shortname))
        self.assertNotIn('}}', str(name.shortname))
        self.assertNotIn('params', str(name.shortname))
        self.assertNotIn('{{', str(name.formalname))
        self.assertNotIn('}}', str(name.formalname))
        self.assertNotIn('params', str(name.formalname))

    def test_city(self):
        """  """
        name = Name(self.redis, 'city', {'citytype':'Butcher'})
        self.assertEqual('city', str(name.namesource))
        print "city:  %s | %s | %s" %( name.fullname, name.shortname, name.formalname)
        self.assertIn('{{params.title}} ', str(name.fullname_template))
        self.assertIn(' {{params.pre}}', str(name.fullname_template))
        self.assertIn('{{params.root}}', str(name.fullname_template))
        self.assertIn('{{params.post}} ', str(name.fullname_template))
        self.assertIn(' {{params.trailer}}', str(name.fullname_template))
        self.assertNotIn('{{', str(name.fullname))
        self.assertNotIn('}}', str(name.fullname))
        self.assertNotIn('params', str(name.fullname))
        self.assertNotIn('{{', str(name.shortname))
        self.assertNotIn('}}', str(name.shortname))
        self.assertNotIn('params', str(name.shortname))
        self.assertNotIn('{{', str(name.formalname))
        self.assertNotIn('}}', str(name.formalname))
        self.assertNotIn('params', str(name.formalname))
    def test_continent(self):
        """  """
        name = Name(self.redis, 'continent', {'continenttype':'Butcher'})
        self.assertEqual('continent', str(name.namesource))
        print "continent:  %s | %s | %s" %( name.fullname, name.shortname, name.formalname)
        self.assertIn('{{params.title}} ', str(name.fullname_template))
        self.assertIn(' {{params.pre}}', str(name.fullname_template))
        self.assertIn('{{params.root}}', str(name.fullname_template))
        self.assertIn('{{params.post}}', str(name.fullname_template))
        self.assertNotIn('{{', str(name.fullname))
        self.assertNotIn('}}', str(name.fullname))
        self.assertNotIn('params', str(name.fullname))
        self.assertNotIn('{{', str(name.shortname))
        self.assertNotIn('}}', str(name.shortname))
        self.assertNotIn('params', str(name.shortname))
        self.assertNotIn('{{', str(name.formalname))
        self.assertNotIn('}}', str(name.formalname))
        self.assertNotIn('params', str(name.formalname))
