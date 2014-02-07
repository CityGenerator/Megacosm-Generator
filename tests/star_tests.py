
from generators.Star import Star
import unittest2 as unittest


class TestStar(unittest.TestCase):

    def setUp(self):
        """  """
        self.star = Star();

    def test_creation(self):
        """  """
        print "workin"
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()


