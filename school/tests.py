from rest_framework.test import APITestCase
from rest_framework import status
from .models import School

class SchoolAPITestCase(APITestCase):
    def setUp(self):
        # Create a test school object
        self.school = School.objects.create(
            school_name="Test School",
            location="Test Location",
            contact_email="test@school.com",
            contact_number="123456789"
        )
        self.create_url = '/api/schools/'
        self.update_url = f'/api/schools/{self.school.id}/update/'
        self.delete_url = f'/api/schools/{self.school.id}/delete/'

    def test_create_school(self):
        data = {
            "school_name": "New School",
            "location": "New Location",
            "contact_email": "new@school.com",
            "contact_number": "987654321"
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(School.objects.count(), 2)
        self.assertEqual(School.objects.last().school_name, "New School")

    def test_update_school(self):
        data = {
            "school_name": "Updated School",
            "location": "Updated Location",
            "contact_email": "updated@school.com",
            "contact_number": "1122334455"
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.school.refresh_from_db()
        self.assertEqual(self.school.school_name, "Updated School")
        self.assertEqual(self.school.location, "Updated Location")

    def test_delete_school(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(School.objects.count(), 0)

    def test_update_nonexistent_school(self):
        response = self.client.put('/api/schools/999/update/', {
            "school_name": "Nonexistent School",
            "location": "Nowhere",
            "contact_email": "nonexistent@school.com",
            "contact_number": "0000000000"
        })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_nonexistent_school(self):
        response = self.client.delete('/api/schools/999/delete/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
