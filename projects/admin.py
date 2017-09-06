from django.contrib import admin

from projects.models import Project, Image

# Register app(projects) models
admin.site.register(Project)
admin.site.register(Image)