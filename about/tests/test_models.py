from django.test import TestCase
from about.models import AboutPage


class AboutPageModelTest(TestCase):
    """
    Test for the AboutPage model to ensure it behaves as expected
    """

    def test_string_representation(self):
        """
        Test the string representation of AboutPage
        """
        about_page = AboutPage(content="Test About Page Content")
        self.assertEqual(str(about_page), "About Page Content")
