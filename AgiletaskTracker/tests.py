from django.test import TestCase

# Create your tests here.

class URLtest(TestCase):

    def test_homepage(self):

        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_create_card(self):

        response = self.client.get('')
        self.assertEqual(response.status_code, 404)



    def test_view_renders_correct_template(self):
        response = self.client.get("/home/")
        self.assertTemplateUsed(response, 'AgiletaskTracker/home.html')
