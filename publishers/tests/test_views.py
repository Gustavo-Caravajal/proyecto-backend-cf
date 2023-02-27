from rest_framework.test import APIClient
from django.test import TestCase
from rest_framework import status
from publishers.models import Publisher
from django.urls import reverse

# Create your tests here.


class PublishersTestCaseGet(TestCase):
    def setUp(self):
        self.client = APIClient()
        Publisher.objects.create(name='Publisher 1', founded_year=1980)
        
    
    def test_get_publishers(self):
        publisher_id = Publisher.objects.first().id  # Obtener el ID del primer autor creado
        response = self.client.get(f'/api/v2/publishers/{publisher_id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PublishersTestCaseDelete(TestCase):
    def setUp(self):
        self.publisher = Publisher.objects.create(
            name='Publisher 1',
            founded_year=1980
        )
        self.url = reverse('detail_publishers', args=[self.publisher.pk])

    def test_delete_publisher(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)