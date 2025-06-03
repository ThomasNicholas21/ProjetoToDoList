from rest_framework.test import APITestCase
from django.urls import reverse
from activity.tests.test_activity_base import ActivityMixin


class TestApiActivityStatusCode(APITestCase, ActivityMixin):
    def test_activity_api_get_returns_status_code_200(self):
        activity_url = reverse('activity:activity-api')
        response = self.client.get(activity_url)
        self.assertEqual(
            response.status_code,
            200
        )

    def test_activity_api_post_returns_status_code_200(self):
        activity_url = reverse('activity:activity-api')
        response = self.client.post(activity_url)
        self.assertEqual(
            response.status_code,
            200
        )
