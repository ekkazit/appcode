# -*- coding: utf-8 -*-
from django import forms

from .models import CourseBooking, CourseRegister, Quotation


class CourseBookingForm(forms.ModelForm):
    persons = forms.ChoiceField(choices=[(x, x) for x in range(1, 20)])

    class Meta:
        model = CourseBooking
        exclude = ['course', 'completed']

    def __init__(self, *args, **kwargs):
        super(CourseBookingForm, self).__init__(*args, **kwargs)
        self.fields['name'].error_messages = {
            'required': u'กรุณากรอกชื่อ-นามสกุล',
        }
        self.fields['phone'].error_messages = {
            'required': u'กรุณากรอกเบอร์โทรศัพท์',
        }
        self.fields['email'].error_messages = {
            'required': u'กรุณากรอกอีเมล์',
            'invalid': u'รูปแบบของอีเมล์ไม่ถูกต้อง',
        }
        self.fields['persons'].error_messages = {
            'required': u'กรุณาระบุจำนวนผู้เข้าอบรม',
        }


class QuotationForm(forms.ModelForm):
    persons = forms.ChoiceField(choices=[(x, x) for x in range(1, 20)])

    class Meta:
        model = Quotation
        exclude = ['course', 'completed']

    def __init__(self, *args, **kwargs):
        super(QuotationForm, self).__init__(*args, **kwargs)
        self.fields['name'].error_messages = {
            'required': u'กรุณากรอกชื่อ-นามสกุล',
        }
        self.fields['phone'].error_messages = {
            'required': u'กรุณากรอกเบอร์โทรศัพท์',
        }
        self.fields['email'].error_messages = {
            'required': u'กรุณากรอกอีเมล์',
            'invalid': u'รูปแบบของอีเมล์ไม่ถูกต้อง',
        }
        self.fields['company'].error_messages = {
            'required': u'กรุณากรอกชื่อหน่วยงาน',
        }


class CourseRegisterForm(forms.ModelForm):
    persons = forms.ChoiceField(choices=[(x, x) for x in range(1, 20)])

    class Meta:
        model = CourseRegister
        exclude = ['course_open', 'paid', 'completed']

    def __init__(self, *args, **kwargs):
        super(CourseRegisterForm, self).__init__(*args, **kwargs)
        self.fields['name'].error_messages = {
            'required': u'กรุณากรอกชื่อ-นามสกุล',
        }
        self.fields['phone'].error_messages = {
            'required': u'กรุณากรอกเบอร์โทรศัพท์',
        }
        self.fields['email'].error_messages = {
            'required': u'กรุณากรอกอีเมล์',
            'invalid': u'รูปแบบของอีเมล์ไม่ถูกต้อง',
        }
        self.fields['persons'].error_messages = {
            'required': u'กรุณาระบุจำนวนผู้เข้าอบรม',
        }
