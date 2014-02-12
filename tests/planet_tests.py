
from generators.Planet import Planet
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os

config = ConfigParser.RawConfigParser()
config.read('data/config.ini')
url = config.get('redis', 'url')


class TestPlanet(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis=redis.from_url(url)

    def test_creation(self):
        """  """
        planet = Planet(self.redis, {'seed':1007})

    def test_randomseed(self):
        planet = Planet(self.redis)
   

if __name__ == '__main__':
    unittest.main()


