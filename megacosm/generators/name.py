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
        """ Given a namesource, generate features for it:
            e.g. human -> humanname_*
            Next, query redis and ensure that templates exist 
            for the three basic names (full, short, formal).
            Finally, render the templates using the naming features
            already generated.
           """
        self.namesource=namesource
        #Generate the content for a name, e.g. humanname_*
        self.generate_features(namesource+"name")
        self.render()

    def render(self):
        for nametype in ['full','short', 'formal']:
            # Ensure that all three templates exist.
            if not hasattr(self,nametype+'name_template'):
                # Throw an exception if our templates are missing.
                raise LookupError("%sname_template not found for %s" % (nametype, self.namesource ) )
            else:
                # Get the name template
                template=getattr(self,nametype+'name_template')
                # Render the name template
                rendered_template=self.render_template(template).strip(' ')
                print("%s: %s" %(nametype,rendered_template))
                # Assign the rendered template text to the right variable.
                setattr(self, nametype+"name", rendered_template)
        

    def __str__(self):
        return self.fullname.title()
