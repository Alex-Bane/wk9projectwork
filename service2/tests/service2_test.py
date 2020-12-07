from flask import url_for
from flask_testing import TestCase

from app import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestAlpha(TestBase):
    def test_alpha(self):
        response = self.client.get(url_for('char_class'))
        self.assertEquals(response.status_code,200)