# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from app.models import Account, Category

from .models import (
    Course,
    CourseOpen,
    CourseBooking,
    CourseRegister,
    Quotation,
)

from .forms import (
    CourseBookingForm,
    CourseRegisterForm,
    QuotationForm,
)


def index(request):
    categories = Category.objects.all()
    courses = Course.objects.all()

    if request.GET.get('id'):
        courses = courses.filter(category=request.GET.get('id'))

    return render(request, 'course/index.html', {
        'menu': 'course',
        'categories': categories,
        'courses': courses,
    })


def detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    ids = course.tags.values_list('id', flat=True)
    related_courses = Course.objects.filter(tags__in=ids).distinct().exclude(id=course.id)[:5]
    accounts = Account.objects.all()

    return render(request, 'course/detail.html', {
        'menu': 'course',
        'course': course,
        'related_courses': related_courses,
        'accounts': accounts,
    })


def booking(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.method == 'POST':
        form = CourseBookingForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.course_id = request.POST.get('id')
            booking.save()
            return HttpResponseRedirect(reverse('course:complete', kwargs={'slug': course.slug}) + '?name=booking')
    else:
        form = CourseBookingForm(initial={'booking_date': datetime.now()}, use_required_attribute=False)
    return render(request, 'course/booking.html', {
        'menu': 'course',
        'form': form,
        'course': course,
    })


def quotation(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.method == 'POST':
        form = QuotationForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            quotation = form.save(commit=False)
            quotation.course_id = request.POST.get('id')
            quotation.save()
            return HttpResponseRedirect(reverse('course:complete', kwargs={'slug': course.slug}) + '?name=quotation')
    else:
        form = QuotationForm(initial={'training_date': datetime.now()}, use_required_attribute=False)
    return render(request, 'course/quotation.html', {
        'menu': 'course',
        'course': course,
        'form': form,
    })


def complete(request, slug):
    course = get_object_or_404(Course, slug=slug)

    return render(request, 'course/complete.html', {
        'menu': 'course',
        'course': course,
        'name': request.GET.get('name'),
    })
