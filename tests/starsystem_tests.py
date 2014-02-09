
from generators.StarSystem import StarSystem
import unittest2 as unittest
from mock import MagicMock


class TestStarSystem(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis=MagicMock()

    def test_creation(self):
        """  """
        star = StarSystem(self.redis, {'seed':1007})
        self.assertEqual(star.seed,1007)
        with self.assertRaises(AttributeError) as context:
            star.missingfeature

    def test_randomseed(self):
        star = StarSystem(self.redis)
        self.assertIs(type(star.seed), int)
   
    def test_starcount(self):
        """ """ 
        star = StarSystem(self.redis,{'seed':1,'star_count':3})
        self.assertEqual(star.seed,1)
        self.assertEqual(star.star_count,3)
        self.assertEqual(len(star.stars),3)
 

if __name__ == '__main__':
    unittest.main()


