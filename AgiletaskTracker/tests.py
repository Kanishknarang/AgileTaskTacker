from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class URLtest(TestCase):

    def test_homepage(self):

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_view_renders_correct_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'AgiletaskTracker/home.html')
