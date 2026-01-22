from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from patients.models import Patient
from doctors.models import Doctor


# Create your tests here.
class DoctorViewSetTests(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            first_name="Ángel",
            last_name="Arreola",
            date_of_birth="2002-04-08",
            contact_number="4341390091",
            email="angelarreolagg@gmail.com",
            address="Sebastian de la Madrid N.13",
            medical_history="",
        )
        self.doctor = Doctor.objects.create(
            first_name="Luis",
            last_name="Martinez",
            qualification="Django Developer",
            contact_number="=123456789",
            email="luismart.platzi@gmail.com",
            address="Test #113",
            start_date="2021-08-16",
            biography="No bio yet.",
            is_on_vacation=False,
        )
        self.client = APIClient()

    def test_list_should_return_200(self):
        url = reverse("doctors-appointments", kwargs={"pk": self.doctor.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
