#
import megacosm
import unittest2 as unittest
import flask.ext.testing
from flask import Flask



class MegacosmFlaskTestCast(flask.ext.testing.TestCase):
#
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.app = megacosm.app.test_client()

    def test_index_route(self):
        response = self.app.get("/")
        self.assertTemplateUsed('index.html')
        self.assert200(response)

################################################################
    def test_magicitem_route(self):
        response = self.app.get("/magicitem")
        self.assert200(response)

    def test_magicitem_builder_route(self):
        response = self.app.get("/magicitem_builder")
        self.assert200(response)
################################################################
    def test_rumor_route(self):
        response = self.app.get("/rumor")
        self.assert200(response)

    def test_rumor_builder_route(self):
        response = self.app.get("/rumor_builder")
        self.assert200(response)
################################################################

    def test_npc_route(self):
        response = self.app.get("/npc")
        self.assert200(response)

    def test_npc_builder_route(self):
        response = self.app.get("/npc_builder")
        self.assert200(response)
################################################################
    def test_planet_route(self):
        response = self.app.get("/planet")
        self.assert200(response)

    def test_planet_builder_route(self):
        response = self.app.get("/planet_builder")
        self.assert200(response)
################################################################
    def test_bond_route(self):
        response = self.app.get("/bond")
        self.assert200(response)

    def test_bond_builder_route(self):
        response = self.app.get("/bond_builder")
        self.assert200(response)
################################################################
    def test_misfire_route(self):
        response = self.app.get("/misfire")
        self.assert200(response)

    def test_misfire_builder_route(self):
        response = self.app.get("/misfire_builder")
        self.assert200(response)
################################################################
    def test_currency_route(self):
        response = self.app.get("/currency")
        self.assert200(response)

    def test_currency_builder_route(self):
        response = self.app.get("/currency_builder")
        self.assert200(response)
################################################################
    def test_legend_route(self):
        response = self.app.get("/legend")
        self.assert200(response)

    def test_legend_builder_route(self):
        response = self.app.get("/legend_builder")
        self.assert200(response)
################################################################
    def test_business_route(self):
        response = self.app.get("/business")
        self.assert200(response)

    def test_business_builder_route(self):
        response = self.app.get("/business_builder")
        self.assert200(response)
################################################################
    def test_moon_route(self):
        response = self.app.get("/moon")
        self.assert200(response)

    def test_moon_builder_route(self):
        response = self.app.get("/moon_builder")
        self.assert200(response)
################################################################
    def test_star_route(self):
        response = self.app.get("/star")
        self.assert200(response)

    def test_star_builder_route(self):
        response = self.app.get("/star_builder")
        self.assert200(response)
################################################################
    def test_continent_route(self):
        response = self.app.get("/continent")
        self.assert200(response)

    def test_continent_builder_route(self):
        response = self.app.get("/continent_builder")
        self.assert200(response)
################################################################
    def test_sect_route(self):
        response = self.app.get("/sect")
        self.assert200(response)

    def test_sect_builder_route(self):
        response = self.app.get("/sect_builder")
        self.assert200(response)
################################################################
    def test_country_route(self):
        response = self.app.get("/country")
        self.assert200(response)

    def test_country_builder_route(self):
        response = self.app.get("/country_builder")
        self.assert200(response)
################################################################
    def test_cuisine_route(self):
        response = self.app.get("/cuisine")
        self.assert200(response)

    def test_cuisine_builder_route(self):
        response = self.app.get("/cuisine_builder")
        self.assert200(response)
################################################################
    def test_deity_route(self):
        response = self.app.get("/deity")
        self.assert200(response)

    def test_deity_builder_route(self):
        response = self.app.get("/deity_builder")
        self.assert200(response)
################################################################





if __name__ == '__main__':
    unittest.main()
