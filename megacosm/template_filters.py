#!/usr/bin/env python3
from megacosm.util import Filters
from megacosm import app

@app.template_filter('uppercase')
def select_uppercase(word):
    """Switch the word to uppercase"""

    return Filters.select_uppercase(word)


@app.template_filter('article')
def select_article(noun):
    """Select the proper article for a noun."""

    return Filters.select_article(noun)


@app.template_filter('pluralize')
def select_pluralize(verb, count):
    """Select the proper verb for a count."""

    return Filters.select_pluralize(verb, count)


@app.template_filter('conjunction')
def select_conjunction(wordlist):
    """Join a list with commas and such."""

    return Filters.select_conjunction(wordlist)


@app.template_filter('plural_verb')
def select_plural_verb(verb, subject):
    """select the proper plural verb."""

    # FIXME is this a duplicate of select_pluralize???

    return Filters.select_plural_verb(verb, subject)


@app.template_filter('plural_adj')
def select_plural_adj(adj, subject):
    """Select the proper version of an adjective."""

    # FIXME is this correct? or is it count-based?

    return Filters.select_plural_adj(adj, subject)
