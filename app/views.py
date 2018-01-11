import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth

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


def login(request):
    response_data = {}
    username= request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            response_data['result'] = 'success'
            return HttpResponse(json.dumps(response_data), content_type='application/json')
    response_data['result'] = 'failed'
    return HttpResponse(json.dumps(response_data), content_type='application/json')
