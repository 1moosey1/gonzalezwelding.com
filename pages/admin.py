from django.contrib import admin
from pages.models import Testimonial, Project, Image

# Register testimonial and project model
admin.site.register(Testimonial)
admin.site.register(Project)
admin.site.register(Image)
