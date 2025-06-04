from rest_framework.test import APITestCase
from django.urls import reverse
from category.tests.test_category_base import CategoryMixin


class TestApiCategoryStatusCode(APITestCase, CategoryMixin):
    # endpoints GET
    def test_category_api_get_returns_status_code_200(self):
        category_url = reverse('category:category-api')
        response = self.client.get(category_url)
        self.assertEqual(
            response.status_code,
            200
        )
