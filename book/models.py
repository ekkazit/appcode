from django.db import models
from taggit.managers import TaggableManager

from app.models import Teacher, Category


BOOK_TYPE_CHOICE = (
    ('B', 'Both'),
    ('E', 'e-Book'),
    ('P', 'Paperback'),
)


def get_book_file(instance, filename):
    return 'upload/book/%s/%s' % (instance.code, filename)


def get_book_exam_file(instance, filename):
    return 'upload/book/exam/%s/%s' % (instance.code, filename)


class Book(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    preview = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, null=True, blank=True)
    type = models.CharField(max_length=1, choices=BOOK_TYPE_CHOICE)
    pages = models.IntegerField(default=0)
    years = models.IntegerField(default=0)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    price_ebook = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    example = models.FileField(upload_to=get_book_exam_file, null=True, blank=True)
    image = models.FileField(upload_to=get_book_file, null=True, blank=True)
    published = models.BooleanField(default=True)
    tags = TaggableManager()

    class Meta:
        db_table = 'book'
        verbose_name_plural = 'Book'

    def __unicode__(self):
        return self.name


class BookOption(models.Model):
    book = models.ForeignKey(Book)
    option = models.CharField(max_length=50)

    class Meta:
        db_table = 'book_option'
        verbose_name_plural = 'BookOption'

    def __unicode__(self):
        return self.option


class Register(models.Model):
    book = models.ForeignKey(Book)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100)
    address = models.TextField(null=True, blank=True)
    unit = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    reg_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    paid = models.BooleanField(default=False)
    paid_date = models.DateTimeField(null=True, blank=True)
    paid_via = models.CharField(max_length=50, null=True, blank=True)
    delivered = models.BooleanField(default=False)

    class Meta:
        db_table = 'book_register'
        verbose_name_plural = 'Register'
        ordering = ['reg_date']

    def __unicode__(self):
        return self.book.name
