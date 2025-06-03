from rest_framework.test import APITestCase
from activity.api.serializer import ActivitySerializers
from activity.models import Activity
from django.urls import reverse
from activity.tests.test_activity_base import ActivityMixin


class TestApiActivityData(APITestCase, ActivityMixin):
    def test_activity_api_get_returns_valid_data(self):
        data = self.make_activity_in_batch(amount=5)
        activity_url = reverse('activity:activity-api')
        response = self.client.get(activity_url)
        serializer = ActivitySerializers(data, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_activity_api_post_returns_valid_data(self):
        payload = self.make_activity_payload()
        url = reverse('activity:activity-api')

        response = self.client.post(url, data=payload, format='json')
        serializer = ActivitySerializers(Activity.objects.get(id=response.data["id"]))

        self.assertEqual(response.data, serializer.data)


class TestApiDetailActivityStatusCode(APITestCase, ActivityMixin):
    ...
