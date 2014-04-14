#
import unittest2 as unittest
from mock import MagicMock
import glob

from qunitsuite.suite import QUnitSuite

class Testjs(unittest.TestCase):

    def test_flagjs(self):
        """ Test Flag js"""
        result = unittest.TestResult()
        suite=QUnitSuite("static/js/tests/flag_test.html")
        suite(result)

    def test_flagshapejs(self):
        """ Test Flag Shape js"""
        result = unittest.TestResult()
        suite=QUnitSuite("static/js/tests/flagshape_test.html")
        suite(result)

