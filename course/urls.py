from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/booking/$', views.booking, name='booking'),
    url(r'^(?P<slug>[\w-]+)/quotation/$', views.quotation, name='quotation'),
    url(r'^(?P<slug>[\w-]+)/complete/$', views.complete, name='complete'),
]
