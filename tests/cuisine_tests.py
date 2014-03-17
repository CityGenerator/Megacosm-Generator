
from generators.Cuisine import Cuisine
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os
from util.Seeds import *


config = ConfigParser.RawConfigParser()
config.read('data/config.ini')
url = config.get('redis', 'url')

class TestCuisine(unittest.TestCase):

    def setUp(self):
        """  """
        
        self.redis=redis.from_url(url)
#        self.seed=set_seed( "3" )

    def test_random_cuisine(self):
        """  """
        cuisine = Cuisine(self.redis )
        print cuisine.text
        self.assertNotEqual(cuisine.text,'')


if __name__ == '__main__':
    unittest.main()




