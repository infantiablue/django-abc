from django.test import TestCase
from django.test import Client


class TestViews(TestCase):
    def test_view_index(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
