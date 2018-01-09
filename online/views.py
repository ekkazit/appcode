from django.shortcuts import render


def index(request):
    return render(request, 'online/index.html', {
        'menu': 'online',
    })


def detail(request, slug):
    return render(request, 'online/detail.html', {
        'menu': 'online',
    })
