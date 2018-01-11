from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^jobs/$', views.jobs, name='jobs'),
    url(r'^login/$', views.login, name='login'),
]
