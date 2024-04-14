from django.test import TestCase
from django.contrib.auth.models import User
from reservations.models import Reservation
from datetime import date, time


# Defines a test case for the Reservation model
class ReservationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up user and reservation instance for tests
        test_user = User.objects.create_user(username='testuser',
                                             password='12345')
        test_user.save()

        # Create a reservation instance for testing purposes
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
        # Test the string representation of a Reservation instance
        reservation = Reservation.objects.get(id=1)
        expected_str = (
            f"Reservation for {reservation.first_name} "
            f"{reservation.last_name} on {reservation.date}"
        )
        self.assertEqual(str(reservation), expected_str)

    def test_reservation_fields(self):
        # Verify correct data in each field of a Reservation instance
        reservation = Reservation.objects.get(id=1)
        self.assertEqual(reservation.guests, 4)
        self.assertEqual(reservation.first_name, 'Martin')
        self.assertEqual(reservation.last_name, 'Liljenroth')
        self.assertEqual(reservation.phone, '123456789')
        self.assertEqual(reservation.email, 'martinliljenroth@example.com')
        self.assertEqual(reservation.message, 'Test message')
