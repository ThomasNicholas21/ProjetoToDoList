from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class TestUrlActivity(TestCase):
    def test_url_activity_is_correct(self):
        activity_get_url = reverse('activity:activity-api')
        self.assertEqual(activity_get_url, '/api/activity/')
