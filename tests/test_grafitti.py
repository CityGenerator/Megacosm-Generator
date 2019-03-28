#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators.Grafitti import Grafitti
from megacosm.generators.NPC import NPC
import unittest2 as unittest

import fakeredis
import fixtures

class TestGrafitti(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = fakeredis.FakeRedis(decode_responses=True)
        fixtures.npc.import_fixtures(self)
        fixtures.phobia.import_fixtures(self)
        fixtures.motivation.import_fixtures(self)
        fixtures.grafitti.import_fixtures(self)

        self.redis.lpush('npc_race','gnome')


    def tearDown(self):
        self.redis.flushall()

    def test_random_grafitti(self):
        """  """
        grafitti = Grafitti(self.redis)
        self.assertEqual('The following message is written in Gnomish with slime: "The warrior tried to protect us, but was too late..." The message is signed with a hand print. You\'d guess the message is less than a day old.', grafitti.text)
        self.assertEqual('The following message is written in Gnomish with slime: "The warrior tried to protect us, but was too late..." The message is signed with a hand print. You\'d guess the message is less than a day old.', str(grafitti))


    def test_static_npc(self):
        """  """
        npc = NPC(self.redis)
        grafitti = Grafitti(self.redis, {'npc':npc})
        self.assertEqual('The following message is written in Gnomish with slime: "The warrior tried to protect us, but was too late..." The message is signed with a hand print. You\'d guess the message is less than a day old.', grafitti.text)
        self.assertEqual('Tom', grafitti.npcname)

    def test_static_npcprofession(self):
        """  """
        grafitti = Grafitti(self.redis, {'npcprofession': 'Spaceman'})
        self.assertEqual('The following message is written in Gnomish with slime: "The warrior tried to protect us, but was too late..." The message is signed with a hand print. You\'d guess the message is less than a day old.', grafitti.text)
        self.assertEqual('Spaceman', grafitti.npcprofession)

    def test_static_npcpname(self):
        """  """
        grafitti = Grafitti(self.redis, {'npcname': 'Guenter'})
        print(grafitti.text)
        self.assertEqual('The following message is written in Gnomish with slime: "The warrior tried to protect us, but was too late..." The message is signed with a hand print. You\'d guess the message is less than a day old.', grafitti.text)
        self.assertEqual('Guenter', grafitti.npcname)

    def test_static_text(self):
        """  """
        grafitti = Grafitti(self.redis, {'text': 'Nothing good.'})
        self.assertEqual('Nothing good.', str(grafitti))

    def test_static_signature(self):
        """  """
        grafitti = Grafitti(self.redis, {'signature': 'by the crazy guy.'})
        self.assertIn('by the crazy guy.', str(grafitti))

    def test_static_age(self):
        """  """
        grafitti = Grafitti(self.redis, {'age': 'super old.'})
        self.assertIn("You'd guess the message is super old.", str(grafitti))
