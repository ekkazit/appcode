from django.db import models
from tinymce.models import HTMLField
from taggit.managers import TaggableManager

from app.models import Teacher, Category, Member


def get_course_file(instance, filename):
    return 'upload/course/%s/%s' % (instance.code, filename)


def get_course_outline_file(instance, filename):
    return 'upload/course/%s/outline/%s' % (instance.code, filename)


def get_course_slider_file(instance, filename):
    return 'upload/course/%s/slides/%s' % (instance.course.code, filename)


class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    content = HTMLField(null=True, blank=True)
    promotion = models.CharField(max_length=50, null=True, blank=True)
    remark = models.CharField(max_length=50, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    teachers = models.ManyToManyField(Teacher, blank=True)
    days = models.IntegerField(default=0)
    hours = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    outline = models.FileField(upload_to=get_course_outline_file, null=True, blank=True)
    image = models.FileField(upload_to=get_course_file, null=True, blank=True)
    published = models.BooleanField(default=True)
    tags = TaggableManager()

    class Meta:
        db_table = 'course'
        verbose_name_plural = 'Course'

    def __unicode__(self):
        return self.name

    def get_course_opens(self):
        return self.courseopen_set.filter(published=True)


class CourseSlider(models.Model):
    course = models.ForeignKey(Course)
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to=get_course_slider_file, null=True, blank=True)

    class Meta:
        db_table = 'course_slider'
        verbose_name_plural = 'CourseSlider'

    def __unicode__(self):
        return self.name


class CourseOption(models.Model):
    course = models.ForeignKey(Course)
    option = models.CharField(max_length=50)

    class Meta:
        db_table = 'course_option'
        verbose_name_plural = 'CourseOption'

    def __unicode__(self):
        return self.option


class CourseOpen(models.Model):
    course = models.ForeignKey(Course)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150, null=True, blank=True)
    times = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    promotion = models.CharField(max_length=50, null=True, blank=True)
    published = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)

    class Meta:
        db_table = 'course_open'
        verbose_name_plural = 'CourseOpen'

    def __unicode__(self):
        return self.name


class CourseBooking(models.Model):
    course = models.ForeignKey(Course)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    persons = models.IntegerField(default=0)
    booking_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'course_booking'
        verbose_name_plural = 'CourseBooking'

    def __unicode__(self):
        return self.name


class CourseRegister(models.Model):
    course_open = models.ForeignKey(CourseOpen)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    persons = models.IntegerField(default=0)
    reg_date = models.DateTimeField(null=True, blank=True)
    paid = models.BooleanField(default=False)
    paid_date = models.DateTimeField(null=True, blank=True)
    paid_via = models.CharField(max_length=50, null=True, blank=True)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'course_register'
        verbose_name_plural = 'CourseRegister'

    def __unicode__(self):
        return self.name


class Quotation(models.Model):
    course = models.ForeignKey(Course)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    company = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    persons = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'quotation'
        verbose_name_plural = 'Quotation'

    def __unicode__(self):
        return self.name
