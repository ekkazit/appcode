from django.db import models
from tinymce.models import HTMLField
from taggit.managers import TaggableManager

from app.models import Teacher, Category, Member


def get_course_file(instance, filename):
    return 'upload/course/%s/%s' % (instance.code, filename)


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
    image = models.FileField(upload_to=get_course_file, null=True, blank=True)
    published = models.BooleanField(default=True)
    tags = TaggableManager()

    class Meta:
        db_table = 'course'
        verbose_name_plural = 'Course'

    def __unicode__(self):
        return self.name


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
