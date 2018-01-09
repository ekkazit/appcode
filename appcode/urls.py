from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
    url(r'^', include('app.urls', namespace='app')),
    url(r'^course/', include('course.urls', namespace='course')),
    url(r'^online/', include('online.urls', namespace='online')),
    url(r'^book/', include('book.urls', namespace='book')),
    url(r'^robots.txt$', lambda r: HttpResponse('User-agent: *\nDisallow: /', content_type='text/plain')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = 'AppCode'
admin.site.site_header = 'AppCode Technology'
