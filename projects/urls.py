from django.conf.urls import url
from . import views

app_name = 'projects'
urlpatterns = [
    url('^create/$', views.create_project, name="create"),
    url('^manager/$', views.manage_projects, name="manager"),
    url('^modify/(?P<project_id>[0-9]{0,4})?$', views.modify_project, name="modify"),
    url('^delete/(?P<project_id>[0-9]{0,4})?$', views.delete_project, name="delete")
]
