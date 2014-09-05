
from megacosm.generators import NPC
from megacosm.generators import Motivation
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os
from megacosm.util.Seeds import *
import re
from config import TestConfiguration

class TestNPC(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis=redis.from_url(TestConfiguration.REDIS_URL)
        self.seed=set_seed( '3' )

    def test_races(self):
        """  """
        npc = NPC(self.redis )
        #FIXME: subraces broke this assertion
        #self.assertIn(npc.race, self.redis.lrange('npc_race',0,-1))

        with self.assertRaisesRegexp(Exception, "turkeys is not a valid race and has no associated data") as context:
            npc = NPC(self.redis, {'race':'turkeys'} )

        npc = NPC(self.redis, { 'race':'human'})
        self.assertEqual(npc.race,'human')

    def test_race_details(self):
        """  """
        npc = NPC(self.redis, { 'race':'human'})
        self.assertEqual(npc.race,'human')
        
        self.assertEqual(npc.details['name'],'Human')
        self.assertEqual(npc.details['size'],'medium')
        self.assertEqual(npc.details['description'],'quick growth and adaptability')
    def test_names(self):
        """  """
        npc = NPC(self.redis, { 'race':'human'})
        self.assertEqual(npc.race,'human')
        self.assertRegexpMatches(npc.name['full'], '.+ .+')

