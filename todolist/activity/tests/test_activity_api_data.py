from rest_framework.test import APITestCase
from activity.api.serializer import ActivitySerializers
from activity.models import Activity
from django.urls import reverse
from django.utils import timezone
from datetime import datetime
from activity.tests.test_activity_base import ActivityMixin


class TestApiActivityData(APITestCase, ActivityMixin):
    # endpoints GET
    def test_activity_api_get_returns_valid_data(self):
        data = self.make_activity_in_batch(amount=5)
        activity_url = reverse('activity:activity-api')
        response = self.client.get(activity_url)
        serializer = ActivitySerializers(data, many=True)
        self.assertEqual(response.data, serializer.data)

    # endpoints POST
    def test_activity_api_post_returns_valid_data(self):
        payload = self.make_activity_payload()
        url = reverse('activity:activity-api')

        response = self.client.post(url, data=payload, format='json')
        serializer = ActivitySerializers(Activity.objects.get(id=response.data["id"]))

        self.assertEqual(response.data, serializer.data)
    
    def test_activity_api_post_returns_valid_data_status_late(self):
        payload = self.make_activity_payload()
        payload['due_date'] = timezone.make_aware(datetime(year=2024, month=12, day=30))

        url = reverse('activity:activity-api')
        response = self.client.post(url, data=payload, format='json')

        self.assertEqual(response.data['status'], 'late')


class TestApiDetailActivityStatusCode(APITestCase, ActivityMixin):
    # endpoints GET
    def test_activity_api_detail_get_returns_valid_data(self):
        data = self.make_activity_in_batch()
        activity = data[0]

        activity_detail_url = reverse(
            'activity:activity-detail-api',
            kwargs={'activity_id': activity.pk}
        )
        response = self.client.get(activity_detail_url)
        serializer = ActivitySerializers(activity)

        self.assertEqual(response.data, serializer.data)

    # endpoints PUT
    def test_activity_api_detail_put_returns_valid_data(self):
        activity_instance = self.make_activity()

        updated_data = self.make_updated_payload(activity=activity_instance)
        activity_detail_url = reverse(
            'activity:activity-detail-api',
            kwargs={'activity_id': activity_instance.pk}
        )
        response = self.client.put(
            activity_detail_url,
            data=updated_data,
            format='json'
        )

        self.assertEqual(response.data['title'], updated_data['title'])
        self.assertEqual(response.data['status'], updated_data['status'])
        self.assertEqual(response.data['priority'], updated_data['priority'])

    def test_activity_api_detail_put_returns_valid_data_status_late(self):
        activity_instance = self.make_activity()

        updated_data = self.make_updated_payload(activity=activity_instance)
        updated_data['due_date'] = timezone.make_aware(datetime(year=2024, month=12, day=30))
        activity_detail_url = reverse(
            'activity:activity-detail-api',
            kwargs={'activity_id': activity_instance.pk}
        )
        response = self.client.put(
            activity_detail_url,
            data=updated_data,
            format='json'
        )

        self.assertEqual(response.data['status'], 'late')

    # endpoints PATCH
    def test_activity_api_detail_patch_returns_valid_data(self):
        activity_instance = self.make_activity()

        patch_data = {
            'title': 'Título atualizado via PATCH',
            'status': 'finished',
            'priority': 'high'
        }
        activity_detail_url = reverse(
            'activity:activity-detail-api',
            kwargs={'activity_id': activity_instance.pk}
        )
        response = self.client.patch(
            activity_detail_url,
            data=patch_data,
            format='json'
        )

        self.assertEqual(response.data['title'], patch_data['title'])
        self.assertEqual(response.data['status'], patch_data['status'])
        self.assertEqual(response.data['priority'], patch_data['priority'])

    def test_activity_api_detail_patch_returns_valid_data_status_late(self):
        activity_instance = self.make_activity()

        updated_data = self.make_updated_payload(activity=activity_instance)
        updated_data['due_date'] = timezone.make_aware(datetime(year=2024, month=12, day=30))
        activity_detail_url = reverse(
            'activity:activity-detail-api',
            kwargs={'activity_id': activity_instance.pk}
        )
        response = self.client.patch(
            activity_detail_url,
            data=updated_data,
            format='json'
        )

        self.assertEqual(response.data['status'], 'late')
