from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.text import slugify

from apps.blog.models import Post
from apps.books.models import Book
from apps.core.models import AuthorProfile


class Command(BaseCommand):
    help = 'Crea contenido inicial para poder previsualizar la web rápidamente.'

    def handle(self, *args, **options):
        biography_text = (
            'Nací entre estanterías y cuadernos. Desde muy joven entendí que la literatura '\
            'era una manera de conservar el asombro y, al mismo tiempo, dialogar con el dolor '\
            'y la memoria. He publicado novela y relato corto, y participo en encuentros '\
            'de lectura y talleres de escritura en distintos espacios culturales.\n\n'
            'En esta web comparto nuevas publicaciones, artículos sobre el proceso creativo '\
            'y noticias de presentaciones. Gracias por estar aquí y leer.'
        )

        profile, created = AuthorProfile.objects.get_or_create(
            pk=1,
            defaults={
                'full_name': 'Ariadna del Valle',
                'hero_quote': 'Escribir es escuchar la respiración del mundo.',
                'biography': biography_text,
            },
        )
        if not created and ('Biografía inicial' in profile.biography or not profile.biography.strip()):
            profile.biography = biography_text
            profile.full_name = profile.full_name or 'Ariadna del Valle'
            profile.hero_quote = profile.hero_quote or 'Escribir es escuchar la respiración del mundo.'
            profile.save(update_fields=['biography', 'full_name', 'hero_quote', 'updated_at'])
            self.stdout.write(self.style.SUCCESS('Perfil de autor actualizado con biografía ampliada.'))
        elif created:
            self.stdout.write(self.style.SUCCESS('Perfil de autor creado.'))
        else:
            self.stdout.write('Perfil de autor ya existía.')

        books = [
            ('La casa de las mareas', 'Una novela intimista sobre memoria, familia y silencio.', Decimal('18.90'), True),
            ('Cartas al invierno', 'Relatos breves sobre amor, pérdida y reconciliación.', Decimal('16.50'), False),
            ('Los días de ámbar', 'Crónica emocional de una ciudad costera y sus secretos.', Decimal('17.40'), False),
            ('Atlas de despedidas', 'Historias cruzadas sobre lo que dejamos atrás.', Decimal('19.20'), False),
            ('El rumor de la nieve', 'Una trama pausada sobre duelo y reconstrucción.', Decimal('18.10'), False),
            ('Antes del alba', 'Novela sobre vocación, juventud y primeras renuncias.', Decimal('15.90'), False),
            ('Luz en los patios', 'Relatos urbanos con mirada poética y social.', Decimal('14.80'), False),
            ('El cuarto de papel', 'Ficción literaria sobre una escritora y su archivo íntimo.', Decimal('20.00'), False),
            ('Mapa de cenizas', 'Narrativa de viajes interiores y retorno al origen.', Decimal('18.70'), False),
            ('Verano en tinta', 'Novela breve sobre amistad, arte y paso del tiempo.', Decimal('16.90'), False),
        ]
        created_books = 0
        for title, synopsis, price, is_featured in books:
            _, was_created = Book.objects.get_or_create(
                slug=slugify(title),
                defaults={
                    'title': title,
                    'synopsis': synopsis,
                    'price': price,
                    'purchase_url': f'https://example.com/{slugify(title)}',
                    'is_featured': is_featured,
                },
            )
            created_books += int(was_created)
        self.stdout.write(self.style.SUCCESS(f'Libros creados: {created_books}. Total actual: {Book.objects.count()}'))

        posts = [
            ('Bienvenidos al blog oficial', 'Nuevo espacio para novedades y reflexiones.', 'Este blog será un diario de publicaciones, eventos y proceso creativo.'),
            ('Cómo nace una novela', 'Del cuaderno en blanco al manuscrito final.', 'Cada libro tiene su ritmo. En este artículo comparto mi método de trabajo.'),
            ('Lecturas que me formaron', 'Cinco autores que cambiaron mi escritura.', 'Repaso de obras que marcaron mis decisiones narrativas y de estilo.'),
            ('Detrás de mi último libro', 'Notas sobre documentación y estructura.', 'Comparto la investigación, los borradores y las dudas del proceso.'),
            ('Agenda de presentaciones', 'Próximas firmas, ferias y clubes de lectura.', 'Calendario actualizado con ciudades, fechas y actividades de encuentro.'),
        ]
        created_posts = 0
        for title, excerpt, content in posts:
            _, was_created = Post.objects.get_or_create(
                slug=slugify(title),
                defaults={
                    'title': title,
                    'excerpt': excerpt,
                    'content': content,
                    'is_published': True,
                    'published_at': timezone.now(),
                },
            )
            created_posts += int(was_created)
        self.stdout.write(self.style.SUCCESS(f'Posts creados: {created_posts}. Total actual: {Post.objects.count()}'))

        self.stdout.write(self.style.SUCCESS('Bootstrap completado.'))
