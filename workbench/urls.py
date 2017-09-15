from django.conf.urls import url, include
from . import views

app_name = 'workbench'
urlpatterns = [
    url('^$', views.workbench, name='workbench'),
    url('^login/$', views.login_view, name='login'),
    url('^logout/$', views.logout_view, name='logout')
]
