from rest_framework.test import APITestCase
from django.urls import reverse
from unittest.mock import patch
from activity.tests.test_activity_base import ActivityMixin


class TestApiActivityStatusCode(APITestCase, ActivityMixin):
    # endpoints GET
    def test_activity_api_get_returns_status_code_200(self):
        activity_url = reverse('activity:activity-api')
        response = self.client.get(activity_url)
        self.assertEqual(
            response.status_code,
            200
        )

    @patch('activity.api.views.Activity.objects.all')  
    def test_get_activity_raises_exception_returns_500(self, mock_all):
        mock_all.side_effect = Exception("Erro simulado")
        url = reverse('activity:activity-api') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 500)

    # endpoints POST
    def test_activity_api_post_returns_status_code_201(self):
        valid_activity = self.make_activity_payload()

        activity_url = reverse('activity:activity-api')
        response = self.client.post(activity_url, data=valid_activity, format='json')

        self.assertEqual(
            response.status_code,
            201
        )

    def test_activity_api_post_returns_status_code_400(self):
        payload = self.make_activity_payload()
        payload.pop("title")

        url = reverse('activity:activity-api')
        response = self.client.post(url, data=payload, format='json')

        self.assertEqual(response.status_code, 400)


class TestApiDetailActivityStatusCode(APITestCase, ActivityMixin):
    # endpoints GET
    def test_activity_api_detail_get_returns_status_code_200(self):
        activity = self.make_activity()
        activity_detail_url = reverse(
            'activity:activity-detail-api', 
            kwargs={
                'activity_id': activity.pk
                }
            )
        response = self.client.get(activity_detail_url)
        self.assertEqual(
            response.status_code,
            200
        )

    # endpoints PUT
    def test_activity_api_detail_put_returns_status_code_200(self):
        activity = self.make_activity()
        activity_detail_url = reverse(
            'activity:activity-detail-api', 
            kwargs={
                'activity_id': activity.pk
                }
            )
        response = self.client.put(activity_detail_url)
        self.assertEqual(
            response.status_code,
            200
        )

    # endpoints PATCH
    def test_activity_api_detail_patch_returns_status_code_200(self):
        activity = self.make_activity()
        activity_detail_url = reverse(
            'activity:activity-detail-api', 
            kwargs={
                'activity_id': activity.pk
                }
            )
        response = self.client.patch(activity_detail_url)
        self.assertEqual(
            response.status_code,
            200
        )

    # endpoints DELETE
    def test_activity_api_detail_delete_returns_status_code_200(self):
        activity = self.make_activity()
        activity_detail_url = reverse(
            'activity:activity-detail-api', 
            kwargs={
                'activity_id': activity.pk
                }
            )
        response = self.client.delete(activity_detail_url)
        self.assertEqual(
            response.status_code,
            200
        )
