from django.conf.urls import url

from . import views

app_name = 'pages'
urlpatterns = [
    url(r'^$',         views.index,   name='index'),
    url(r'^home/$',    views.home,    name='home'),
    url(r'^about/$',   views.about,   name='about'),
    url(r'^contact/$', views.contact, name='contact')
]
