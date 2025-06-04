from rest_framework.test import APITestCase
from category.api.serializer import CategorySerializer
from django.urls import reverse
from category.models import Category
from category.tests.test_category_base import CategoryMixin


class TestApiCategoryData(APITestCase, CategoryMixin):
    # endpoints GET
    def test_category_api_get_returns_valid_data(self):
        data = self.make_category_in_batch(amount=5)
        category_url = reverse('category:category-api')
        response = self.client.get(category_url)
        serializer = CategorySerializer(data, many=True)
        self.assertEqual(response.data, serializer.data)

    # endpoints POST
    def test_category_api_post_returns_valid_data(self):
        payload = self.make_category_payload()
        url = reverse('category:category-api')

        response = self.client.post(url, data=payload, format='json')
        serializer = CategorySerializer(Category.objects.get(id=response.data["id"]))

        self.assertEqual(response.data, serializer.data)


class TestApiDetailCategoryData(APITestCase, CategoryMixin):
    # endpoints GET
    def test_category_api_detail_get_returns_valid_data(self):
        data = self.make_category_in_batch()
        category = data[0]

        category_detail_url = reverse(
            'category:category-detail-api',
            kwargs={'category_id': category.pk}
        )
        response = self.client.get(category_detail_url)
        serializer = CategorySerializer(category)

        self.assertEqual(response.data, serializer.data)

    # endpoints PUT
    def test_category_api_detail_put_returns_valid_data(self):
        category_instance = self.make_category()

        updated_data = self.make_updated_payload(category=category_instance)
        category_detail_url = reverse(
            'category:category-detail-api',
            kwargs={'category_id': category_instance.pk}
        )
        response = self.client.put(
            category_detail_url,
            data=updated_data,
            format='json'
        )

        self.assertEqual(response.data['category_name'], updated_data['category_name'])

    # endpoints PUT
    def test_category_api_detail_patch_returns_valid_data(self):
        category_instance = self.make_category()

        updated_data = self.make_updated_payload(category=category_instance)
        category_detail_url = reverse(
            'category:category-detail-api',
            kwargs={'category_id': category_instance.pk}
        )
        response = self.client.patch(
            category_detail_url,
            data=updated_data,
            format='json'
        )

        self.assertEqual(response.data['category_name'], updated_data['category_name'])
    
    # endpoints DELETE
    def test_category_api_detail_delete_data(self):
        category_instance = self.make_category()

        category_detail_url = reverse(
            'category:category-detail-api',
            kwargs={'category_id': category_instance.pk}
        )

        response = self.client.delete(category_detail_url)

        self.assertFalse(Category.objects.filter(pk=category_instance.pk).exists())
