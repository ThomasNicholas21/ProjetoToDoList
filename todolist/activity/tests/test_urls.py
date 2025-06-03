from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class TestUrlActivity(TestCase):
    def test_url_activity_is_correct(self):
        activity_url = reverse('activity:activity-api')
        self.assertEqual(activity_url, '/api/activity/')

    def test_url_activity_detail_is_correct(self):
        activity_detail_url = reverse('activity:activity-detail-api')
        self.assertEqual(activity_detail_url, kwargs={'activity_id': 1})
