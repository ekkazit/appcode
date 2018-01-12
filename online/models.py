from django.db import models
from taggit.managers import TaggableManager

from app.models import Account, Category, Teacher, Member


class Video(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    teachers = models.ManyToManyField(Teacher, blank=True)
    lessons = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    image = models.FileField(upload_to='images/video', null=True, blank=True)
    premium = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    tags = TaggableManager()

    class Meta:
        db_table = 'video'
        verbose_name_plural = 'Video'

    def __unicode__(self):
        return self.name


class VideoOption(models.Model):
    video = models.ForeignKey(Video)
    option = models.CharField(max_length=50)

    class Meta:
        db_table = 'video_option'
        verbose_name_plural = 'VideoOption'

    def __unicode__(self):
        return self.option


class VideoPlaylist(models.Model):
    video = models.ForeignKey(Video)
    no = models.IntegerField()
    chapter = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    time = models.CharField(max_length=20, null=True, blank=True)
    preview = models.BooleanField(default=False)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'video_playlist'
        verbose_name_plural = 'VideoPlaylist'

    def __unicode__(self):
        return self.title


class VideoRegister(models.Model):
    video = models.ForeignKey(Video)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100)
    unit = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    reg_date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    paid_date = models.DateTimeField(null=True, blank=True)
    paid_via = models.CharField(max_length=50, null=True, blank=True)
    authorized = models.BooleanField(default=False)
    authorized_token = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'video_register'
        verbose_name_plural = 'VideoRegister'

    def __unicode__(self):
        return self.name
