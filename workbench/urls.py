from django.conf.urls import url
from . import views

app_name = 'workbench'
urlpatterns = [
    url('^$', views.workbench, name='workbench'),
    url('^newproject/$', views.NewProjectView.as_view(), name="newproject")
]
