from rest_framework.test import APITestCase
from category.api.serializer import CategorySerializer
from django.urls import reverse
from category.models import Category
from category.tests.test_category_base import CategoryMixin


class TestApiCategoryData(APITestCase, CategoryMixin):
    # endpoints GET
    def test_activity_api_get_returns_valid_data(self):
        data = self.make_category_in_batch(amount=5)
        activity_url = reverse('category:category-api')
        response = self.client.get(activity_url)
        serializer = CategorySerializer(data, many=True)
        self.assertEqual(response.data, serializer.data)

    # endpoints POST
    def test_category_api_post_returns_valid_data(self):
        payload = self.make_category_payload()
        url = reverse('category:category-api')

        response = self.client.post(url, data=payload, format='json')
        serializer = CategorySerializer(Category.objects.get(id=response.data["id"]))

        self.assertEqual(response.data, serializer.data)
