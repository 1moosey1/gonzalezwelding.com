from django.conf.urls import url
from . import views

app_name = 'workbench'
urlpatterns = [
    url('^$', views.workbench, name='workbench'),
    url('^create/project/$', views.create_project, name="createproject"),
    url('^manage/projects/$', views.manage_projects, name="manageprojects"),
    url('^modify/project/(?P<project_id>[0-9]{0,4})?$', views.modify_project, name="modifyproject"),
    url('^delete/project/(?P<project_id>[0-9]{0,4})?$', views.delete_project, name="deleteproject")
]
