from django.test import TestCase
from django.core.urlresolvers import resolve


class AssessmentAPITest(TestCase):

    def test_resolve_app_url(self):
        response = self.client.get('/pcdpdata/')
        self.assertEqual(response.status_code, 200)

    def test_get_assessment(self):
        response = self.client.get('/pcdpdata/assessment/')
        self.assertEqual(response.status_code, 200)
