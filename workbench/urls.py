from django.conf.urls import url, include
from . import views

app_name = 'workbench'
urlpatterns = [
    url('^$', views.workbench, name='workbench')
]
