# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404

from app.models import Account
from .models import Book, Register
from .forms import RegisterForm


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
    course_tags_ids = Book.tags.values_list('id', flat=True)
    if request.method == 'POST':
        form = RegisterForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            if Register.objects.filter(name=form.cleaned_data['name']).count() > 0:
                pass
            else:
                register = form.save(commit=False)
                register.book_id = request.POST.get('id')
                register.save()
            messages.success(request, u'ลงทะเบียนเรียบร้อยแล้ว กรุณาแจ้งโอนเงิน จากนั้นเราจะดำเนินการส่งหนังสือต่อไป ขอบคุณครับ')
            return HttpResponseRedirect(reverse('book:detail', kwargs={'slug': book.slug}))
    else:
        form = RegisterForm(use_required_attribute=False)
    return render(request, 'book/checkout.html', {
        'menu': 'book',
        'book': book,
        'form': form,
    })
