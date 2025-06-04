from rest_framework.test import APITestCase
from unittest.mock import patch
from django.urls import reverse
from category.tests.test_category_base import CategoryMixin
from category.api.serializer import CategorySerializer


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

        category_url = reverse('category:category-api')
        response = self.client.post(category_url, data=valid_category, format='json')

        self.assertEqual(
            response.status_code,
            201
        )

    def test_category_api_post_returns_status_code_400(self):
        payload = self.make_category_payload()
        payload.pop("category_name")

        url = reverse('category:category-api')
        response = self.client.post(url, data=payload, format='json')

        self.assertEqual(response.status_code, 400)


class TestApiDetailCategoryStatusCode(APITestCase, CategoryMixin):
    # endpoints GET
    def test_category_api_detail_get_returns_status_code_200(self):
        category = self.make_category()
        category_detail_url = reverse(
            'category:category-detail-api', 
            kwargs={
                'category_id': category.pk
                }
            )
        response = self.client.get(category_detail_url)
        self.assertEqual(
            response.status_code,
            200
        )

    def test_category_api_detail_get_returns_status_code_404(self):
        category_detail_url = reverse(
            'category:category-detail-api', 
            kwargs={
                'category_id': 9999
                }
            )
        response = self.client.get(category_detail_url)
        self.assertEqual(
            response.status_code,
            404
        )

    @patch('category.api.views.Category.objects.get') 
    def test_get_category_api_detail_get_returns_status_code_500(self, mock_get):
        mock_get.side_effect = Exception("Erro simulado")
        category = self.make_category()

        url = reverse(
            'category:category-detail-api',
            kwargs={'category_id': category.pk}
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 500)

    # endpoints PUT
    def test_category_api_detail_put_returns_status_code_200(self):
        category = self.make_category()
        data = self.make_updated_payload(category)

        url = reverse('category:category-detail-api', kwargs={'category_id': category.pk})
        response = self.client.put(url, data=data, format='json')

        self.assertEqual(response.status_code, 200)

    def test_category_api_detail_put_returns_status_code_404(self):
        category = self.make_category()
        data = self.make_updated_payload(category)

        url = reverse('category:category-detail-api', kwargs={'category_id': 9999})
        response = self.client.put(url, data=data, format='json')

        self.assertEqual(response.status_code, 404)

    @patch('category.api.views.Category.objects.get')
    def test_category_api_detail_put_returns_status_code_400(self, mock_get):
        mock_get.side_effect = Exception("Erro simulado")

        data = {
            "category_name": "Erro forçado"
        }
        url = reverse('category:category-detail-api', kwargs={'category_id': 1})
        response = self.client.put(url, data=data, format='json')

        self.assertEqual(response.status_code, 400)

    # endpoints PATCH
    def test_category_api_detail_patch_returns_status_code_200(self):
        category = self.make_category()
        data = self.make_updated_payload(category)

        url = reverse('category:category-detail-api', kwargs={'category_id': category.pk})
        response = self.client.patch(url, data=data, format='json')

        self.assertEqual(response.status_code, 200)

    def test_category_api_detail_patch_returns_status_code_404(self):
        category = self.make_category()
        data = self.make_updated_payload(category)

        url = reverse('category:category-detail-api', kwargs={'category_id': 9999})
        response = self.client.patch(url, data=data, format='json')

        self.assertEqual(response.status_code, 404)

    @patch('category.api.views.Category.objects.get')
    def test_category_api_detail_patch_returns_status_code_400(self, mock_get):
        mock_get.side_effect = Exception("Erro simulado")

        data = {
            "category_name": "Erro forçado"
        }
        url = reverse('category:category-detail-api', kwargs={'category_id': 1})
        response = self.client.patch(url, data=data, format='json')

        self.assertEqual(response.status_code, 400)

