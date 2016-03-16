#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generator import Generator
import logging
import json
from pprint import pprint
class Name(Generator):

    def __init__(self, server, namesource, features={}):
        """ Given a namesource, generate features for it:
            e.g. human -> humanname_*
            Next, query redis and ensure that templates exist
            for the three basic names (full, short, formal).
            Finally, render the templates using the naming features
            already generated.
        """
        Generator.__init__(self, server, features)
        self.logger = logging.getLogger(__name__)
        self.namesource=namesource

        #Generate the content for a name, e.g. humanname_*
        self.generate_features(namesource+"name")
        #Now that we have the features, render the names
        self.render()

    def render(self):
        """ Using the current object features, populate the templates for all
            three names. Many objects may have identical names, but some do not.
            Each naming convention will have its own templates on how to build it.
            Examples:
            Full: Greater Albijan Province
            Short: Greater Albijan
            Formal: Greater Albijan Province
            Full: Chief Grubtak Backsnapper the Red
            Short: Grubtak the Red
            Formal Chief Backsnapper
            Full: Eerie Catacombs of Doom
        """

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
