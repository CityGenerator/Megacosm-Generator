#
#import megacosm
#import unittest2 as unittest
#import flask.ext.testing
#from flask import Flask
#
#
#
#class MegacosmFlaskTestCast(flask.ext.testing.TestCase):
#
#    def create_app(self):
#        app = Flask(__name__)
#        app.config['TESTING'] = True
#        return app
#
#    def setUp(self):
#        self.app = megacosm.app.test_client()
#
#    def test_index_route(self):
#        response = self.app.get("/")
#        self.assertTemplateUsed('index.html')
#        self.assert200(response)
#
#
#if __name__ == '__main__':
#    unittest.main()
