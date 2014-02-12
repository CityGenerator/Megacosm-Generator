
from generators.Generator import Generator
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os

config = ConfigParser.RawConfigParser()
config.read('data/config.ini')
url = config.get('redis', 'url')


class TestGenerator(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis=redis.from_url(url)

    def test_creation(self):
        """  """
        generator = Generator(self.redis, {'seed':1007})
        self.assertEqual(generator.seed,1007)
        with self.assertRaises(AttributeError) as context:
            generator.missingfeature

    def test_randomseed(self):
        generator = Generator(self.redis)
        self.assertIs(type(generator.seed), int)

    def test_select_by_roll(self):
        generator = Generator(self.redis, {'seed':1007})
        self.assertEquals('"{\'text\':\'average\',     \'multiplier\':1.0}"', generator.select_by_roll('starsize',37))

    def test_select_by_roll_key_doesnt_exist(self):
        generator = Generator(self.redis, {'seed':1007})
        with self.assertRaisesRegexp(Exception, 'the key \(funion\) doesn\'t appear') as context:
            generator.select_by_roll('funion')

    def test_select_by_roll_highmin(self):
        generator = Generator(self.redis, {'seed':1007})
        self.assertEquals('"{\'text\':\'trinary star\',    \'count\':3}"',generator.select_by_roll('starcount',1037))
        self.assertEquals('"{\'text\':\'single star\',     \'count\':1}"',generator.select_by_roll('starcount',-1037))

    def test_select_by_roll_key_wrong_type(self):
        generator = Generator(self.redis, {'seed':1007})
        with self.assertRaisesRegexp(Exception, "the key \(starpre\) doesn't appear to exist or isn't a zset \(list\).") as context:
            generator.select_by_roll('starpre',37)
        
    def test_rand_value(self):
        generator = Generator(self.redis, {'seed':1007})
        self.assertIs(str, type(generator.rand_value('starpre')))

    def test_rand_value_key_wrong_type(self):
        generator = Generator(self.redis, {'seed':1007})
        with self.assertRaisesRegexp(Exception, "the key \(starsize\) doesn't appear to exist or isn't a list \(zset\).") as context:
            generator.rand_value('starsize')

    def test_rand_value_key_doesnt_exist(self):
        generator = Generator(self.redis, {'seed':1007})
        with self.assertRaisesRegexp(Exception, "the key \(somekey\) doesn't appear to exist or isn't a list") as context:
            generator.rand_value('somekey')
       
       

if __name__ == '__main__':
    unittest.main()


