from rest_framework.test import APIClient
from django.test import TestCase
from rest_framework import status
from genres.models import Genre

from django.urls import reverse
# Create your tests here.


class GenresTestCaseGet(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.genre1 = Genre.objects.create(name="Genre1")
        
    
    def test_get_genres(self):
        genre_id = Genre.objects.first().id  # Obtener el ID del primer autor creado
        response = self.client.get(f'/api/v4/genres/{genre_id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GenresTestCaseDelete(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name='Test Genre',)
        self.url = reverse('detail_genres', args=[self.genre.pk])

    def test_delete_genre(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)