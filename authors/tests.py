
from rest_framework.test import APIClient
from django.test import TestCase
from rest_framework import status
from authors.models import Author

from django.urls import reverse
# Create your tests here.


class AuthorsTestCaseGet(TestCase):
    def setUp(self):
        self.client = APIClient()

      
        Author.objects.create(full_name='Autor 1', birth_year=1980, country_origin='México', years_experience=10)
        
    
    def test_get_authors(self):
        author_id = Author.objects.first().id  # Obtener el ID del primer autor creado
        response = self.client.get(f'/api/v1/authors/{author_id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AuthorsTestCaseDelete(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            full_name='Test Author',
            birth_year=1990,
            country_origin='Test Country',
            years_experience=5,
        )
        self.url = reverse('detail_authors', args=[self.author.pk])

    def test_delete_author(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)