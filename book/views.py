# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

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
    if request.method == 'POST':
        form = RegisterForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            register = form.save(commit=False)
            register.book_id = request.POST.get('id')
            register.save()
            messages.success(request, u'สั่งซื้อหนังสือเรียบร้อยแล้ว โปรดตรวจสอบรายละเอียดได้ทางอีเมลของท่าน!')
            return HttpResponseRedirect(reverse('book:finish', kwargs={'slug': book.slug}) + '?regid=' + str(register.id))
    else:
        form = RegisterForm(use_required_attribute=False)
    return render(request, 'book/checkout.html', {
        'menu': 'book',
        'book': book,
        'form': form,
    })


def finish(request, slug):
    regid = request.GET.get('regid')
    book = get_object_or_404(Book, slug=slug)
    register = Register.objects.get(pk=regid)
    accounts = Account.objects.all()

    return render(request, 'book/finish.html', {
        'menu': 'book',
        'book': book,
        'register': register,
        'accounts': accounts,
    })
