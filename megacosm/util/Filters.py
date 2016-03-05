#

import inflect

p = inflect.engine()


def select_uppercase(s):
    return s.upper()

def select_article(s):
    return p.an(s)


def select_pluralize(subject, count):
    return p.plural(subject, count)


def select_plural_verb(verb, subject):
    return p.plural_verb(verb, subject)


def select_plural_adj(adj, subject):
    return p.plural_adj(adj, subject)


def select_conjunction(wordlist):
    """Join a list with commas and such."""
    return p.join(wordlist)
