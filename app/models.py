from django.db import models
from tinymce.models import HTMLField


class Account(models.Model):
    name = models.CharField(max_length=50)
    bank = models.CharField(max_length=50, null=True, blank=True)
    branch = models.CharField(max_length=50, null=True, blank=True)
    acc_code = models.CharField(max_length=50, null=True, blank=True)
    acc_name = models.CharField(max_length=50, null=True, blank=True)
    acc_type = models.CharField(max_length=50, null=True, blank=True)
    image = models.FileField(upload_to='images/bank', null=True, blank=True)

    class Meta:
        db_table = 'account'
        verbose_name_plural = 'Account'

    def __unicode__(self):
        return self.name


class Category(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Category'

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50, null=True, blank=True)
    fullname = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=150, null=True, blank=True)
    profile = HTMLField(null=True, blank=True)
    image = models.FileField(upload_to='images/teacher', null=True, blank=True)

    class Meta:
        db_table = 'teacher'
        verbose_name_plural = 'Teacher'

    def __unicode__(self):
        return self.name


class Member(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50, null=True, blank=True)
    fullname = models.CharField(max_length=100, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    image = models.FileField(upload_to='images/member', null=True, blank=True)

    class Meta:
        db_table = 'member'
        verbose_name_plural = 'Member'

    def __unicode__(self):
        return self.name
