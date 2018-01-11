from django.shortcuts import render, get_object_or_404

from app.models import Account
from .models import Book


def index(request):
    books = Book.objects.filter(published=True)
    return render(request, 'book/index.html', {
        'menu': 'book',
        'books': books,
    })


def detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    ids = book.tags.values_list('id', flat=True)
    related_books = Book.objects.filter(tags__in=ids).distinct().exclude(id=book.id)[:5]
    accounts = Account.objects.all()

    return render(request, 'book/detail.html', {
        'menu': 'book',
        'book': book,
        'related_books': related_books,
        'accounts': accounts,
    })


def checkout(request, slug):
    book = get_object_or_404(Book, slug=slug)

    return render(request, 'book/checkout.html', {
        'menu': 'book',
        'book': book,
    })
