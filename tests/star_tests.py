
from generators.Star import Star
import unittest2 as unittest
from mock import MagicMock


import redis
import ConfigParser, os

config = ConfigParser.RawConfigParser()
config.read('data/config.ini')
url = config.get('redis', 'url')

class TestStar(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis=redis.from_url(url)


    def test_creation(self):
        """  """
        star = Star(self.redis);


if __name__ == '__main__':
    unittest.main()


