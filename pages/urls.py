from django.conf.urls import url
from django.views.generic import RedirectView

from pages.views import IndexView, HomeView, AboutView
from . import views

app_name = 'pages'
urlpatterns = [
    url(r'^$',         IndexView.as_view(),   name='index'),
    url(r'^home/$',    HomeView.as_view(),    name='home'),
    url(r'^about/$',   AboutView.as_view(),   name='about'),
    url(r'^contact/$', views.contact,         name='contact')
]
