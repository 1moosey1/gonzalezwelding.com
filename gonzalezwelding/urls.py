from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [

    # Core app to serve regular pages
    url(r'^', include('pages.urls')),

    # Workbench provides visitor statics and serves as an umbrella app
    url(r'^workbench/', include('workbench.urls')),

    # Project app for managing work showcase - navigation through workbench
    url(r'^workbench/project/', include('projects.urls')),

    # Admin plugin
    url(r'^admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
