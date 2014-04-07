
from generators.Misfire import Misfire
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os
from util.Seeds import *


config = ConfigParser.RawConfigParser()
config.read('data/config.ini')
url = config.get('redis', 'url')

class TestMisfire(unittest.TestCase):

    def setUp(self):
        """  """
        
        self.redis=redis.from_url(url)
#        self.seed=set_seed( "3" )

    def test_random_misfire(self):
        """  """
        misfire = Misfire(self.redis )
        print misfire.text
        self.assertNotEqual(misfire.text,'')
        self.assertEqual("%s" % (misfire),   misfire.text)


