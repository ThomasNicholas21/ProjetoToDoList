from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class TestUrlCategory(TestCase):
    def test_url_category_is_correct(self):
        category_url = reverse('category:category-api')
        self.assertEqual(category_url, '/api/category/')
