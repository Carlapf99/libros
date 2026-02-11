from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from apps.books.models import Book

from .forms import ContactForm
from .models import AuthorProfile


def home(request):
    profile = AuthorProfile.objects.first()
    featured_book = Book.objects.filter(is_featured=True).order_by('-created_at').first()
    return render(
        request,
        'core/home.html',
        {'profile': profile, 'featured_book': featured_book},
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
