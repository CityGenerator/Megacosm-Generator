
from generators.Continent import Continent
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os
from util.Seeds import *


config = ConfigParser.RawConfigParser()
config.read('data/config.ini')
url = config.get('redis', 'url')

class TestContinent(unittest.TestCase):

    def setUp(self):
        """  """
        
        self.redis=redis.from_url(url)
        self.seed=set_seed( "3" )

    def test_random_continent(self):
        """  """
        continent = Continent(self.redis )
        continent.add_countries()
        self.assertGreaterEqual(len(continent.countries),0)


    def test_continent_country(self):
        """  """
        continent = Continent(self.redis, {'countrycount':25})
        continent.add_countries()
        self.assertEqual(len(continent.countries),25)
        print continent.__dict__


if __name__ == '__main__':
    unittest.main()




