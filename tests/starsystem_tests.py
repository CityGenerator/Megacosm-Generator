
from generators.StarSystem import StarSystem
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os

config = ConfigParser.RawConfigParser()
config.read('data/config.ini')
url = config.get('redis', 'url')


class TestStarSystem(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis=redis.from_url(url)

    def test_creation(self):
        """  """
        star = StarSystem(self.redis, {'seed':1007})

    def test_starcount(self):
        """ """ 
        star = StarSystem(self.redis,{'seed':1,'star_count':3})
        self.assertEqual(star.seed,1)
        self.assertEqual(star.star_count,3)
        self.assertEqual(len(star.stars),3)
 

if __name__ == '__main__':
    unittest.main()


