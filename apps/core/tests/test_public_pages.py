from django.test import TestCase
from django.urls import reverse

from apps.core.models import AuthorProfile


class PublicPagesTests(TestCase):
    def setUp(self):
        AuthorProfile.objects.create(
            full_name='Autor Test',
            hero_quote='Una frase de prueba',
            biography='Biografía de prueba',
        )

    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_loads(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_loads(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_robots_txt(self):
        response = self.client.get(reverse('robots_txt'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'User-agent: *')

    def test_sitemap_xml(self):
        response = self.client.get('/sitemap.xml')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<urlset')
