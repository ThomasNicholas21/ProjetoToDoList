from rest_framework.test import APITestCase
from category.api.serializer import CategorySerializer
from django.urls import reverse
from category.tests.test_category_base import CategoryMixin


class TestApiCategoryData(APITestCase, CategoryMixin):
    # endpoints GET
    def test_activity_api_get_returns_valid_data(self):
        data = self.make_category_in_batch(amount=5)
        activity_url = reverse('category:category-api')
        response = self.client.get(activity_url)
        serializer = CategorySerializer(data, many=True)
        self.assertEqual(response.data, serializer.data)
