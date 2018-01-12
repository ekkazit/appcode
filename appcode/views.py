from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.utils.http import is_safe_url


def home(request):
    return render(request, 'index.html', {
        'menu': 'index',
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            next_url = request.GET.get('next', '')
            if is_safe_url(url=next_url, host=request.get_host()):
                return HttpResponseRedirect(next_url)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {
        'form': form,
        'menu': request.GET.get('menu'),
    })
