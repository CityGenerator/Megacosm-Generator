
from generators.Generator import Generator
import unittest2 as unittest
from mock import MagicMock


class TestGenerator(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis=MagicMock()

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
        testText="{'text':'large',       'multiplier':2.0}"
        self.redis.zrangebyscore.return_value=testText
        self.redis.type.return_value='zset'
        generator = Generator(self.redis, {'seed':1007})
        self.assertEquals(testText, generator.select_by_roll(37,'starsize'))

    def test_select_by_roll_key_doesnt_exist(self):
        self.redis.exists.return_value=False
        generator = Generator(self.redis, {'seed':1007})
        with self.assertRaisesRegexp(Exception, 'the key funion doesn\'t appear') as context:
            generator.select_by_roll(37,'funion')

    def test_select_by_roll_no_value_found(self):
        self.redis.zrangebyscore.return_value=None
        self.redis.type.return_value='zset'
        generator = Generator(self.redis, {'seed':1007})
        with self.assertRaisesRegexp(Exception, 'the key funion appears to be empty for a value of 37- This should never happen.') as context:
            generator.select_by_roll(37,'funion')

    def test_select_by_roll_key_wrong_type(self):
        testType="zset"
        self.redis.exists.return_value=True
        self.redis.type.return_value=None
        generator = Generator(self.redis, {'seed':1007})
        with self.assertRaisesRegexp(Exception, 'the key funion doesn\'t appear') as context:
            generator.select_by_roll(37,'funion')
        
    def test_rand_value(self):
        self.redis.exists.return_value=True
        self.redis.type.return_value='list'
        self.redis.llen.return_value=1
        returntext='fakeresult'
        self.redis.lindex.return_value=returntext
        generator = Generator(self.redis, {'seed':1007})
        self.assertEqual(returntext, generator.rand_value('somekey'))

    def test_rand_value_key_wrong_type(self):
        self.redis.exists.return_value=True
        self.redis.type.return_value='badkey'
        self.redis.llen.return_value=1
        returntext='fakeresult'
        self.redis.lindex.return_value=returntext
        generator = Generator(self.redis, {'seed':1007})
        with self.assertRaisesRegexp(Exception, "the key somekey doesn't appear to exist or isn't a list \(badkey\).") as context:
            generator.rand_value('somekey')

    def test_rand_value_key_doesnt_exist(self):
        self.redis.exists.return_value=False
        returntext='fakeresult'
        self.redis.lindex.return_value=returntext
        generator = Generator(self.redis, {'seed':1007})
        with self.assertRaisesRegexp(Exception, "the key somekey doesn't appear to exist or isn't a list") as context:
            generator.rand_value('somekey')
       
       

if __name__ == '__main__':
    unittest.main()


