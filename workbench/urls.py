from django.conf.urls import url
from . import views

app_name = 'workbench'
urlpatterns = [
    url('^$', views.workbench, name='workbench'),
    url('^project/new/$', views.create_project, name="createproject"),
    url('^project/manage/$', views.manage_projects, name="manageprojects"),
    url('^project/modify/(?P<project_id>[0-9]{0,4})?$', views.modify_project, name="modifyproject")
]
