from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {
        'menu': 'index',
    })


def about(request):
    return render(request, 'about/index.html', {
        'menu': 'about',
    })


def jobs(request):
    return render(request, 'jobs/index.html', {
        'menu': 'jobs',
    })
