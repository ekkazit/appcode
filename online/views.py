from django.shortcuts import render

from .models import Video


def index(request):
    videos = Video.objects.filter(published=True).order_by('-premium')

    return render(request, 'online/index.html', {
        'menu': 'online',
        'videos': videos,
    })


def detail(request, slug):
    return render(request, 'online/detail.html', {
        'menu': 'online',
    })
