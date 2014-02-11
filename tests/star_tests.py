
from generators.Star import Star
import unittest2 as unittest
from mock import MagicMock


class TestStar(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis=MagicMock()


    def test_creation(self):
        """  """
        print "workin"
        star = Star(self.redis);
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()


