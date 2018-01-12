# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from app.models import Account
from .models import Video, VideoRegister
from .forms import VideoRegisterForm


def index(request):
    videos = Video.objects.filter(published=True).order_by('-premium')

    return render(request, 'online/index.html', {
        'menu': 'online',
        'videos': videos,
    })


def detail(request, slug):
    video = get_object_or_404(Video, slug=slug)
    ids = video.tags.values_list('id', flat=True)
    related_videos = Video.objects.filter(tags__in=ids).distinct().exclude(id=video.id)[:5]

    autoplay = False
    player= None
    pl = request.GET.get('pl')
    active_pl = -1
    if pl:
        autoplay = True
        player= video.videoplaylist_set.filter(id=int(pl)).first()
    else:
        player = video.videoplaylist_set.first()
        if player:
            active_pl = player.id

    return render(request, 'online/detail.html', {
        'menu': 'online',
        'video': video,
        'related_videos': related_videos,
        'player': player,
        'autoplay': autoplay,
        'active_pl': active_pl,
    })


def checkout(request, slug):
    video = get_object_or_404(Video, slug=slug)

    if request.method == 'POST':
        form = VideoRegisterForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            register = form.save(commit=False)
            register.video_id = request.POST.get('id')
            register.save()
            messages.success(request, u'สั่งซื้อคอร์สออนไลน์เรียบร้อยแล้ว โปรดตรวจสอบรายละเอียดได้ทางอีเมลของท่าน!')
            return HttpResponseRedirect(reverse('online:finish', kwargs={'slug': video.slug}) + '?regid=' + str(register.id))
    else:
        form = VideoRegisterForm(use_required_attribute=False)
    return render(request, 'online/checkout.html', {
        'menu': 'online',
        'video': video,
        'form': form,
    })


def finish(request, slug):
    regid = request.GET.get('regid')
    video = get_object_or_404(Video, slug=slug)
    register = VideoRegister.objects.get(pk=regid)
    accounts = Account.objects.all()

    return render(request, 'online/finish.html', {
        'menu': 'online',
        'video': video,
        'register': register,
        'accounts': accounts,
    })
