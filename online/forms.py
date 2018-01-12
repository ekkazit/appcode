# -*- coding: utf-8 -*-
from django import forms

from .models import VideoRegister


class VideoRegisterForm(forms.ModelForm):
    class Meta:
        model = VideoRegister
        exclude = ['video', 'paid', 'paid_date', 'paid_via', 'authorized']

    def __init__(self, *args, **kwargs):
        super(VideoRegisterForm, self).__init__(*args, **kwargs)
        self.fields['name'].error_messages = {
            'required': u'กรุณากรอกชื่อของท่าน',
        }
        self.fields['email'].error_messages = {
            'required': u'กรุณากรอกอีเมล์',
            'invalid': u'รูปแบบของอีเมล์ไม่ถูกต้อง',
        }
