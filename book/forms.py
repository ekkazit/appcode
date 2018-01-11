# -*- coding: utf-8 -*-
from django import forms

from .models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        exclude = ['book', 'paid', 'paid_date', 'paid_via', 'delivered']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['name'].error_messages = {'required': u'กรุณากรอกชื่อ-นามสกุล'}
        self.fields['phone'].error_messages = {'required': u'กรุณากรอกเบอร์โทรศัพท์'}
        self.fields['email'].error_messages = {'required': u'กรุณากรอกอีเมล์', 'invalid': u'รูปแบบของอีเมล์ไม่ถูกต้อง'}
