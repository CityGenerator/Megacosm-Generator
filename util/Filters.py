
import inflect

p = inflect.engine()

def select_article(s):
    return p.an(s)

def select_pluralize(s):
    return p.plural(s)

