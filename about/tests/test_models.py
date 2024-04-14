from django.test import TestCase
from about.models import AboutPage

# Test for the AboutPage model to ensure it behaves as expected


class AboutPageModelTest(TestCase):

    # Test the string representation of AboutPage
    def test_string_representation(self):
        about_page = AboutPage(content="Test About Page Content")
        self.assertEqual(str(about_page), "About Page Content")
