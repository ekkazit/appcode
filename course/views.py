from django.shortcuts import render, get_object_or_404

from app.models import Account, Category
from .models import Course

def index(request):

    courses = Course.objects.filter(published=True).order_by('code')
    categories = Category.objects.all()

    return render(request, 'course/index.html', {
        'menu': 'course',
        'courses': courses,
        'categories': categories,
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
