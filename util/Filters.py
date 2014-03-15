
import inflect

p = inflect.engine()

def select_article(s):
    return p.an(s)

def select_pluralize(s,n):
    return p.plural(s,n)

def select_conjunction(wordlist):
    return p.join(wordlist)
