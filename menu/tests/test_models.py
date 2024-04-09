from decimal import Decimal
from django.test import TestCase
from menu.models import Dish

class DishModelTest(TestCase):
    def setUp(self):
        # Creates an instance of Dish to use in the tests
        Dish.objects.create(
            name='Test Dish',
            description='Test description',
            price=Decimal('10'),
            category='Appetizer'
        )

    def test_dish_creation(self):
        # Tests that a Dish instance was created correctly
        dish = Dish.objects.get(name='Test Dish')
        self.assertTrue(isinstance(dish, Dish))
        self.assertEqual(dish.__str__(), 'Test Dish')
        self.assertEqual(dish.description, 'Test description')
        self.assertEqual(dish.price, Decimal('10'))
        self.assertEqual(dish.category, 'Appetizer')

    def test_string_representation(self):
        # Tests that the string representation of the Dish instance is correct
        dish = Dish.objects.get(name='Test Dish')
        self.assertEqual(str(dish), 'Test Dish')