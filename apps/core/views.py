from django.conf import settings
from django.contrib import messages
from django.contrib.sitemaps import Sitemap
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from apps.blog.models import Post
from apps.books.models import Book

from .forms import ContactForm
from .models import AuthorProfile


class StaticViewSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'

    def items(self):
        return ['home', 'about', 'contact', 'book_list', 'post_list']

    def location(self, item):
        return reverse(item)


class BookSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return Book.objects.all()


class PostSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return Post.objects.filter(is_published=True)


def robots_txt(_request):
    lines = [
        'User-agent: *',
        'Allow: /',
        'Disallow: /admin/',
        'Sitemap: /sitemap.xml',
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')


def home(request):
    profile = AuthorProfile.objects.first()
    featured_book = Book.objects.filter(is_featured=True).order_by('-created_at').first()
    latest_posts = Post.objects.filter(is_published=True)[:3]
    stats = {
        'books': Book.objects.count(),
        'posts': Post.objects.filter(is_published=True).count(),
    }
    return render(
        request,
        'core/home.html',
        {
            'profile': profile,
            'featured_book': featured_book,
            'latest_posts': latest_posts,
            'stats': stats,
        },
    )


def about(request):
    profile = AuthorProfile.objects.first()
    return render(request, 'core/about.html', {'profile': profile})


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        content = (
            f"Mensaje desde formulario web\n\n"
            f"Nombre: {data['name']}\n"
            f"Email: {data['email']}\n\n"
            f"{data['message']}"
        )
        send_mail(
            subject=f"[Web Autor] {data['subject']}",
            message=content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_RECIPIENT_EMAIL],
            fail_silently=False,
        )
        messages.success(request, 'Tu mensaje fue enviado correctamente.')
        return redirect('contact')

    return render(request, 'core/contact.html', {'form': form})


def error_404(request, exception):
    return render(request, 'errors/404.html', status=404)


def error_500(request):
    return render(request, 'errors/500.html', status=500)
