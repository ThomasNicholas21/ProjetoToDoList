from rest_framework.test import APITestCase
from unittest.mock import patch
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

    @patch('category.api.views.Category.objects.all')  
    def test_get_category_raises_exception_returns_500(self, mock_all):
        mock_all.side_effect = Exception("Erro simulado")
        url = reverse('category:category-api') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 500)
    
    # endpoints POST
    def test_category_api_post_returns_status_code_201(self):
        valid_category = self.make_category_payload()

        activity_url = reverse('category:category-api')
        response = self.client.post(activity_url, data=valid_category, format='json')

        self.assertEqual(
            response.status_code,
            201
        )

