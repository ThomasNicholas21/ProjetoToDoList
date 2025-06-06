from rest_framework.test import APITestCase
from activity.api.serializer import ActivitySerializers
from activity.models import Activity
from django.urls import reverse
from django.utils import timezone
from django.utils.dateparse import parse_datetime
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

    def test_activity_api_post_returns_valid_data_status_finished(self):
        payload = self.make_activity_payload()
        payload['status'] = 'finished'

        url = reverse('activity:activity-api')
        response = self.client.post(url, data=payload, format='json')

        finished_at_str = response.data.get('finished_at')
        self.assertIsNotNone(finished_at_str)

        finished_at = parse_datetime(finished_at_str)

        now = timezone.now()
        delta = abs((finished_at - now).total_seconds())
        self.assertLessEqual(delta, 2)


class TestApiDetailActivityData(APITestCase, ActivityMixin):
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

    def test_activity_api_put_returns_valid_data_status_finished(self):
        activity = self.make_activity()
        payload = self.make_updated_payload(activity)
        payload['status'] = 'finished'

        url = reverse('activity:activity-detail-api', kwargs={'activity_id': activity.pk})
        response = self.client.put(url, data=payload, format='json')

        finished_at_str = response.data.get('finished_at')
        self.assertIsNotNone(finished_at_str)

        finished_at = parse_datetime(finished_at_str)

        now = timezone.now()
        delta = abs((finished_at - now).total_seconds())
        self.assertLessEqual(delta, 2)


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
    
    def test_activity_api_patch_returns_valid_data_status_finished(self):
        activity = self.make_activity()
        payload = self.make_updated_payload(activity)
        payload['status'] = 'finished'

        url = reverse('activity:activity-detail-api', kwargs={'activity_id': activity.pk})
        response = self.client.patch(url, data=payload, format='json')

        finished_at_str = response.data.get('finished_at')
        self.assertIsNotNone(finished_at_str)

        finished_at = parse_datetime(finished_at_str)

        now = timezone.now()
        delta = abs((finished_at - now).total_seconds())
        self.assertLessEqual(delta, 2)

    # endpoints DELETE
    def test_activity_api_detail_delete_data(self):
        activity_instance = self.make_activity()

        activity_detail_url = reverse(
            'activity:activity-detail-api',
            kwargs={'activity_id': activity_instance.pk}
        )

        response = self.client.delete(activity_detail_url)

        self.assertFalse(Activity.objects.filter(pk=activity_instance.pk).exists())
