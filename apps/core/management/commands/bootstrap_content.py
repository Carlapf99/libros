from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.utils import timezone

from apps.blog.models import Post
from apps.books.models import Book
from apps.core.models import AuthorProfile


class Command(BaseCommand):
    help = 'Crea contenido inicial para poder previsualizar la web rápidamente.'

    def handle(self, *args, **options):
        profile, created = AuthorProfile.objects.get_or_create(
            pk=1,
            defaults={
                'full_name': 'Nombre del Autor',
                'hero_quote': 'Escribir es escuchar la respiración del mundo.',
                'biography': 'Biografía inicial del autor. Edita este texto en el panel admin.',
            },
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Perfil de autor creado.'))
        else:
            self.stdout.write('Perfil de autor ya existía.')

        if not Book.objects.exists():
            books = [
                {
                    'title': 'La casa de las mareas',
                    'synopsis': 'Una novela intimista sobre memoria, familia y silencio.',
                    'price': Decimal('18.90'),
                    'purchase_url': 'https://example.com/libro-1',
                    'is_featured': True,
                },
                {
                    'title': 'Cartas al invierno',
                    'synopsis': 'Relatos breves sobre amor, pérdida y reconciliación.',
                    'price': Decimal('16.50'),
                    'purchase_url': 'https://example.com/libro-2',
                    'is_featured': False,
                },
            ]
            for item in books:
                Book.objects.create(slug=slugify(item['title']), **item)
            self.stdout.write(self.style.SUCCESS('Libros de ejemplo creados.'))
        else:
            self.stdout.write('Ya hay libros, no se crearon ejemplos.')

        if not Post.objects.exists():
            posts = [
                {
                    'title': 'Bienvenidos al blog oficial',
                    'excerpt': 'Nuevo espacio para novedades y reflexiones.',
                    'content': 'Este blog será un diario de publicaciones, eventos y proceso creativo.',
                },
                {
                    'title': 'Cómo nace una novela',
                    'excerpt': 'Del cuaderno en blanco al manuscrito final.',
                    'content': 'Cada libro tiene su ritmo. En este artículo comparto mi método de trabajo.',
                },
            ]
            for item in posts:
                Post.objects.create(
                    slug=slugify(item['title']),
                    is_published=True,
                    published_at=timezone.now(),
                    **item,
                )
            self.stdout.write(self.style.SUCCESS('Posts de ejemplo creados.'))
        else:
            self.stdout.write('Ya hay posts, no se crearon ejemplos.')

        self.stdout.write(self.style.SUCCESS('Bootstrap completado.'))
