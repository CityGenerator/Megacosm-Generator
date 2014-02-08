
from generators.Planet import Planet
import unittest2 as unittest
from mock import MagicMock


class TestPlanet(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis=MagicMock()

    def test_creation(self):
        """  """
        planet = Planet(self.redis, {'seed':1007})
        self.assertEqual(planet.seed,1007)
        with self.assertRaises(AttributeError) as context:
            planet.missingfeature

    def test_randomseed(self):
        planet = Planet(self.redis)
        self.assertIs(type(planet.seed), int)
   

if __name__ == '__main__':
    unittest.main()


