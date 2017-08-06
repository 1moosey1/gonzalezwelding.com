from django.conf.urls import url
from . import views

app_name = 'pages'
urlpatterns = [
    url(r'^$',              views.IndexView.as_view(), name='index'),
    url(r'^home/$',         views.home,                name='home'),
    url(r'^about/$',        views.about, name='about'),
    url(r'^contact/$',      views.contact,             name='contact'),
    url(r'^work/$',         views.work,                name='work'),
    url(r'^testimonials/$', views.testimonials,        name='testimonials')
]
