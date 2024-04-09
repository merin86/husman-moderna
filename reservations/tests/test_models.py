from django.test import TestCase
from django.contrib.auth.models import User
from reservations.models import Reservation
from datetime import date, time

# Defines a test case for the Reservation model to ensure its behavior
class ReservationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # This method sets up a user and a reservation instance used across different tests
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_user.save()

        # Create a reservation instance for testing
        Reservation.objects.create(
            user=test_user,
            date=date.today(),
            time=time(18, 0),
            guests=4,
            first_name='Martin',
            last_name='Liljenroth',
            phone='123456789',
            email='martinliljenroth@example.com',
            message='Test message'
        )

    def test_reservation_string_representation(self):
        # Tests that the string representation of a Reservation instance is as expected
        reservation = Reservation.objects.get(id=1)
        expected_reservation_str = f"Reservation for {reservation.first_name} {reservation.last_name} on {reservation.date}"
        self.assertEqual(str(reservation), expected_reservation_str)

    def test_reservation_fields(self):
        # Verifies that each field in a Reservation instance contains the correct data
        reservation = Reservation.objects.get(id=1)
        self.assertEqual(reservation.guests, 4)
        self.assertEqual(reservation.first_name, 'Martin')
        self.assertEqual(reservation.last_name, 'Liljenroth')
        self.assertEqual(reservation.phone, '123456789')
        self.assertEqual(reservation.email, 'martinliljenroth@example.com')
        self.assertEqual(reservation.message, 'Test message')