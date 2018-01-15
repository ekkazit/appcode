from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.http import HttpResponse

from . import views

urlpatterns = [
    url(r'^home/',views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
    url(r'^', include('app.urls', namespace='app')),
    url(r'^course/', include('course.urls', namespace='course')),
    url(r'^online/', include('online.urls', namespace='online')),
    url(r'^book/', include('book.urls', namespace='book')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^robots.txt$', lambda r: HttpResponse('User-agent: *\nDisallow: /', content_type='text/plain')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_title = 'AppCode'
admin.site.site_header = 'AppCode Technology'
