#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
import logging
import json
from pprint import pprint
class Name(Generator):

    def __init__(self, server, namesource, features={}):
        Generator.__init__(self, server, features)
        self.logger = logging.getLogger(__name__)
        """ Given a namesource, query redis and ensure that templates exist 
            for the three basic names (full, short, formal).
           """
        #Generate the content for a name, e.g. humanname_*
        self.generate_features(namesource+"name")

        # Ensure that all three templates exist.
        for nametype in ['full','short', 'formal']:
            if not hasattr(self,nametype+'name_template'):
                raise LookupError("%sname_template not found for %s" % (nametype, namesource ) )

        # Build the name from the template
        for nametype in ['full','short', 'formal']:
            #Set fullname, shortname, or formalname from the hash
            setattr(self, nametype+'name', self.build_hash_name(nametype))

    def build_hash_name(self, nametype):
        name=""
        namehashstring=getattr(self,nametype+"name_template" )
        namehash= json.loads(namehashstring)

        for namepart in namehash:
            if hasattr(self, namepart):
                name+=getattr(self,namepart)
            elif namepart == " ":
                name+=(" ")
        return name.strip()

    def __str__(self):
        return str(self.fullname)
