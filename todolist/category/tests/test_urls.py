from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class TestUrlCategory(TestCase):
    def test_url_category_is_correct(self):
        category_url = reverse('category:category-api')
        self.assertEqual(category_url, '/api/category/')

    def test_url_category_detail_is_correct(self):
        category_detail_url = reverse('category:category-datail-api', kwargs={'category_id': 1})
        self.assertEqual(category_detail_url, '/api/category/<int:category_id>')
