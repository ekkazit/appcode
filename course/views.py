# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives, EmailMessage

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
    accounts = Account.objects.all()

    if request.method == 'POST':
        form = CourseBookingForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.course_id = request.POST.get('id')
            booking.save()

            banks = ''
            for b in accounts:
                banks += u"""%s บัญชี <strong>%s</strong> %s %s %s<br>""" % (b.bank, b.acc_code, b.acc_type, b.branch, b.acc_name)

            subject, from_email, to = '[APPCODE] สมัครเรียนหลักสูตรเรียบร้อยแล้ว', 'appcodetraining@gmail.com', form.cleaned_data['email']
            text_content = u'คุณได้สมัครเรียนหลักสูตร %s เรียบร้อยแล้ว' % course.name
            html_content = u'เรียนคุณ %s<br><br>คุณได้สมัครเรียนหลักสูตร <strong>[%s] %s</strong> เรียบร้อยแล้ว<br>คุณสามารถชำระเงินค่าอบรมล่วงหน้าได้ โดยโอนผ่านธนาคารบัญชีใดบัญชีหนึ่งดังนี้<br><br><br>%s<br><br><br><br>ขอบคุณครับ<br>AppCode Team' % (form.cleaned_data['name'], course.code, course.name, banks)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, 'text/html')
            msg.send()

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

            subject, from_email, to = '[APPCODE] ได้รับคำขอใบเสนอราคาแล้ว', 'appcodetraining@gmail.com', form.cleaned_data['email']
            text_content = u'ระบบได้รับคำขอใบเสนอราคาสำหรับหลักสูตร %s เป็นที่เรียบร้อยแล้ว' % course.name
            html_content = u'เรียนคุณ %s<br><br>ระบบได้รับคำขอใบเสนอราคาสำหรับหลักสูตร<strong>[%s] %s</strong> เป็นที่เรียบร้อย<br>ทางบริษัทฯจะดำเนินการจัดส่งใบเสนอราคาให้ท่านต่อไป<br><br><br><br>ขอบคุณครับ<br>AppCode Team' % (form.cleaned_data['name'], course.code, course.name)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, 'text/html')
            msg.send()

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
    accounts = Account.objects.all()

    return render(request, 'course/complete.html', {
        'menu': 'course',
        'course': course,
        'accouts': accounts,
    })


def register(request, slug, open_id):
    course = get_object_or_404(Course, slug=slug)
    course_open = get_object_or_404(CourseOpen, id=open_id)
    accounts = Account.objects.all()

    if request.method == 'POST':
        form = CourseRegisterForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            register = form.save(commit=False)
            register.course_open_id = request.POST.get('id')
            register.reg_date = datetime.now()
            register.save()

            banks = ""
            for b in accounts:
                banks += u"""%s บัญชี <strong>%s</strong> %s %s %s<br>""" % (b.bank, b.acc_code, b.acc_type, b.branch, b.acc_name)

            subject, from_email, to = '[APPCODE] ลงทะเบียนเรียบร้อยแล้ว', 'addcodetraining@gmail.com', form.cleaned_data['email']
            text_content = u'คุณได้ลงทะเบียนหลักสูตร %s เรียบร้อยแล้ว' % course.name
            html_content = u'เรียนคุณ %s<br><br>คุณได้ลงทะเบียนในหลักสูตร <strong>[%s] %s</strong> เป็นที่เรียบร้อยแล้ว<br>กรุณาชำระเงินโดยโอนผ่านธนาคารบัญชีใดบัญชีหนึ่งดังนี้<br><br><br>%s<br>หลังจากโอนแล้วกรุณาแจ้งหลักฐานการชำระเงินมาที่อีเมล appcodetraining@gmail.com หรือ LINE: appcodetraining<br><br>ขอบคุณครับ<br>AppCode Team' % (form.cleaned_data['name'], course.code, course.name, banks)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, 'text/html')
            msg.send()

            return HttpResponseRedirect(reverse('course:complete', kwargs={'slug': course.slug}) + '?name=register')
    else:
        form = CourseRegisterForm(initial={'register_date': datetime.now()}, use_required_attribute=False)
    return render(request, 'course/register.html', {
        'menu': 'course',
        'course': course,
        'course_open': course_open,
        'form': form,
    })
