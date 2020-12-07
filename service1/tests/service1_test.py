from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_page(self):
        with patch("requests.get") as g:
            with patch("requests.post") as p:
                g.return_value.text = "Half-Orc"
                p.return_value.text = "Bonus Stats: +2 to Strength, +1 to Constitution"

                response = self.client.get(url_for("index"))
                self.assertIn(b'Bonus Stats: +2 to Strength, +1 to Constitution"', response.data)