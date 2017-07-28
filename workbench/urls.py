from django.conf.urls import url
from . import views

app_name = 'workbench'
urlpatterns = [
    url('^$', views.workbench, name='workbench')
]
