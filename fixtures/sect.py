#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.zadd('sect_acceptance', '{"name":"saintly",  "score":100   }', 100)
    self.redis.lpush("sect_kind","chapter")
    self.redis.lpush("sectname_fullname_template","{{params.title}} {{params.pre}}{{params.root}}{{params.post}} {{params.trailer}}")
    self.redis.lpush("sectname_shortname_template","{{params.fullname}}")
    self.redis.lpush("sectname_formalname_template","{{params.fullname}}")

    self.redis.lpush("sectname_title","Order of the")
    self.redis.lpush("sectname_pre","Orei")
    self.redis.lpush("sectname_root","bal")
    self.redis.lpush("sectname_post","ic")
    self.redis.lpush("name_sect_trailer","Followers")
