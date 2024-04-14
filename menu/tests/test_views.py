from django.test import TestCase
from django.urls import reverse
from menu.models import Dish


class MenuViewTests(TestCase):
    def setUp(self):
        """
        Create test data for each dish category
        """
        Dish.objects.create(name="Test Appetizer",
                            description="A test appetizer.",
                            price=5.00, category="Appetizer")
        Dish.objects.create(name="Test Main Course",
                            description="A test main course.",
                            price=15.00, category="Main Course")
        Dish.objects.create(name="Test Dessert",
                            description="A test dessert.",
                            price=7.00, category="Dessert")

    def test_menu_view_status_code(self):
        """
        Test that the menu view returns a 200 status code when accessed
        """
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)

    def test_menu_view_uses_correct_template(self):
        """
        Test that the menu view uses the correct template
        """
        response = self.client.get(reverse('menu'))
        self.assertTemplateUsed(response, 'menu/menu.html')

    def test_menu_view_context(self):
        """
        Test that the menu view passes the correct categories
        of dishes to the template's context
        """
        response = self.client.get(reverse('menu'))
        self.assertTrue('appetizers' in response.context)
        self.assertTrue('main_courses' in response.context)
        self.assertTrue('desserts' in response.context)
