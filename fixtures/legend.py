#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.lpush('legend_ability', 'make someone speak the truth')
    self.redis.lpush('legend_abilitytype', 'capability')
    self.redis.lpush('legend_area', 'swamps')
    self.redis.lpush('legend_badaction', 'took a hostage and demanded a ransom')
    self.redis.lpush('legend_badfate', 'will be stricken blind')
    self.redis.lpush('legend_badguy', 'a {{params.badguytype}} named {{params.villain.name.fullname}}')
    self.redis.lpush('legend_badguytype', 'devil')
    self.redis.lpush('legend_bait', 'ask for your help')
    self.redis.lpush('legend_caughtfailing', 'didn\'t get close')
    self.redis.lpush('legend_chumps', 'the royals')
    self.redis.lpush('legend_detect', 'confront')
    self.redis.lpush('legend_drawn', 'and was drawn towards thieves')
    self.redis.lpush('legend_failedresolution', 'stop the {{params.badguytype}}')
    self.redis.lpush('legend_goodstart', 'thrived')
    self.redis.lpush('legend_goodstatus', 'quiet')
    self.redis.lpush('legend_hero', 'a {{params.npc.behavior}} {{params.npc.race}} named {{params.npc.name.fullname}}')
    self.redis.lpush('legend_lastseen', 'mysteriously disappeared')
    self.redis.lpush('legend_monster', 'old woman')
    self.redis.lpush('legend_object', 'bag of beans')
    self.redis.lpush('legend_planaction', 'by making a wager with {{params.villain.name.fullname}}')
    self.redis.lpush('legend_plan', 'the thought to slay the {{params.badguytype}}')
    self.redis.lpush('legend_reputation', 'possessed')
    self.redis.lpush('legend_results', 'tricked {{params.villain.name.fullname}}')
    self.redis.lpush('legend_stopit', 'unless you offer a sacrifice')
    self.redis.lpush('legend_storytime', 'In olden times')
    self.redis.lpush('legend_talent', 'a valiant knight')
    self.redis.lpush('legend_template',
                     '{{params.storytime}}, {{params.badguytype |article }} named {{params.villain.name.fullname}} '+
                     '{{params.wander}} the {{params.area}} {{params.when}} {{params.drawn}}. {{params.who}} say '+
                     'that if you {{params.detect}} {{params.villain.sex["third-person"]}}, you {{params.badfate}} '+
                     '{{params.stopit}}.')
    self.redis.lpush('legend_trap', 'give you a gift if you are nice')
    self.redis.lpush('legend_victory', 'and rescued the hostages')
    self.redis.lpush('legend_virtue', 'never trusting another {{params.badguytype}}')
    self.redis.lpush('legend_wander', 'haunted')
    self.redis.lpush('legend_when', 'when the wind blows from the west')
    self.redis.lpush('legend_who', 'People')

