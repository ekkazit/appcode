# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import EmailMultiAlternatives, EmailMessage

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

    is_locked = False
    if video.price:
        is_locked = True

    if request.user.is_authenticated():
        register = VideoRegister.objects.filter(email=request.user.email, video_id=video.id).first()
        if register and register.authorized:
            is_locked = False

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
        'is_locked': is_locked,
    })


def checkout(request, slug):
    video = get_object_or_404(Video, slug=slug)
    accounts = Account.objects.all()

    if request.method == 'POST':
        form = VideoRegisterForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            register = form.save(commit=False)
            register.video_id = request.POST.get('id')
            register.save()

            banks = ''
            for b in accounts:
                banks += u"""%s บัญชี <strong>%s</strong> %s %s %s<br>""" % (b.bank, b.acc_code, b.acc_type, b.branch, b.acc_name)

            subject, from_email, to = '[APPCODE] สั่งซื้อคอร์สออนไลน์', 'appcodetraining@gmail.com', form.cleaned_data['email']
            text_content = u'คุณได้สั่งซื้อหนังสือ %s เรียบร้อยแล้ว' % video.name
            html_content = u'เรียนคุณ %s<br><br>คุณได้สั่งซื้อคอร์สออนไลน์ <strong>[%s] %s</strong> เรียบร้อยแล้ว<br>กรุณาโอนเงินจำนวน <strong>%s</strong> บาท โดยโอนผ่านธนาคารบัญชีใดบัญชีหนึ่งดังนี้<br><br><br>%s<br><br>หลังจากโอนแล้วกรุณาแจ้งหลักฐานการชำระเงินมาที่อีเมล appcodetraining@gmail.com หรือ LINE: appcodetraining<br><br>ขอบคุณครับ<br>AppCode Team' % (form.cleaned_data['name'], video.code, video.name, register.amount, banks)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, 'text/html')
            msg.send()

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
