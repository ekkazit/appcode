from django.shortcuts import render, get_object_or_404

from .models import Video


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
