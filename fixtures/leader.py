#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""

    self.redis.lpush('leader_scope', 'country')
    self.redis.lpush('leader_scope', 'region')
    self.redis.lpush('leader_scope', 'city')
    self.redis.lpush('leader_scope', 'organization')

    self.redis.lpush('leadercountry_kind', 'absolutemonarchy')
    self.redis.lpush('leaderregion_kind', 'barony')
    self.redis.lpush('leadercity_kind', 'mayorcouncil')
    self.redis.lpush('leaderorganization_kind', 'gang')

    self.redis.lpush('leaderabsolutemonarchy_leader', 'king')
    self.redis.hset('leaderabsolutemonarchy_leader_description', 'king', '{ "male":"King",    "female":"Queen"     }')

    self.redis.lpush('leaderbarony_leader', 'baron')
    self.redis.hset('leaderbarony_leader_description', 'baron', '{ "male":"Baron",      "female":"Baroness"      }')

    self.redis.lpush('leadermayorcouncil_leader', 'mayor')
    self.redis.hset('leadermayorcouncil_leader_description', 'mayor', '{ "male":"Mayor",      "female":"Mayor"   }')

    self.redis.lpush('leadergang_leader', 'gangleader')
    self.redis.hset('leadergang_leader_description', 'gangleader', '{ "male":"GangLeader", "female":"Gang Leader"  }')












