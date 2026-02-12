from django.shortcuts import get_object_or_404, render

from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'books/book_detail.html', {'book': book})
