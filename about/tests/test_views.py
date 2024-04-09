from django.test import TestCase
from django.urls import reverse
from about.models import AboutPage

class AboutViewTests(TestCase):

    def setUp(self):
        # Set up an instance of the AboutPage model for testing
        AboutPage.objects.create(content="Test content for About Page")

    def test_about_view_status_code(self):
        # Test that the about view returns a 200 status code when accessed
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_view_uses_correct_template(self):
        # Test that the about view uses the correct template
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about/about.html')

    def test_about_view_context(self):
        # Test that the about view passes the AboutPage instance to the template's context
        response = self.client.get(reverse('about'))
        self.assertTrue('about_page' in response.context)
        about_page = response.context['about_page']
        self.assertEqual(about_page.content, "Test content for About Page")