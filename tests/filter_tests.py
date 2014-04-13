#
import unittest2 as unittest
from util.Filters import *

class TestFilter(unittest.TestCase):

#

################################################################
    def test_select_article(self):
        self.assertEquals( 'a dog',     select_article('dog') )
        self.assertEquals( 'an apple',  select_article('apple') )
        self.assertEquals( 'an hour',   select_article('hour') )
################################################################
    def test_select_pluralize(self):
        self.assertEquals( 'dogs', select_pluralize('dog',0) )
        self.assertEquals( 'dog',  select_pluralize('dog',1) )
        self.assertEquals( 'dogs', select_pluralize('dog',2) )
        self.assertEquals( 'classes',   select_pluralize('class',0) )
        self.assertEquals( 'class',     select_pluralize('class',1) )
        self.assertEquals( 'classes',   select_pluralize('class',2) )
################################################################
    def test_select_conjunction(self):
        self.assertEquals( "a",                 select_conjunction(['a']) )
        self.assertEquals( "a and b",           select_conjunction(['a','b']) )
        self.assertEquals( "a, b, and c",       select_conjunction(['a','b','c']) )
        self.assertEquals( "a, b, c, and d",    select_conjunction(['a','b','c','d']) )
################################################################
    def test_select_plural_verb(self):
        self.assertEquals( "were", select_plural_verb('was',0) )
        self.assertEquals( "was", select_plural_verb('was',1) )
        self.assertEquals( "were", select_plural_verb('was',2) )
################################################################
    def test_select_plural_verb(self):
        self.assertEquals( "some", select_plural_adj('a',0) )
        self.assertEquals( "a",    select_plural_adj('a',1) )
        self.assertEquals( "some", select_plural_adj('a',2) )

        self.assertEquals( "these", select_plural_adj('this',0) )
        self.assertEquals( "this",  select_plural_adj('this',1) )
        self.assertEquals( "these", select_plural_adj('this',2) )

        self.assertEquals( "those", select_plural_adj('that',0) )
        self.assertEquals( "that",  select_plural_adj('that',1) )
        self.assertEquals( "those", select_plural_adj('that',2) )

        self.assertEquals( "our", select_plural_adj('my',0) )
        self.assertEquals( "my",  select_plural_adj('my',1) )
        self.assertEquals( "our", select_plural_adj('my',2) )
