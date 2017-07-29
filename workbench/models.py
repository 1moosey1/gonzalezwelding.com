from django.db import models
from gonzalezwelding import settings


# Model for all testimonials
class Testimonial(models.Model):

    text = models.TextField(max_length=1024)
    quotee = models.CharField(max_length=64)
    company = models.CharField(max_length=64)
    display = models.BooleanField(default=True)


# Model for work/project information
class Project(models.Model):

    title = models.CharField(primary_key=True, max_length=64)
    description = models.TextField(max_length=512)

    def __str__(self):
        return 'Project: {}'.format(self.title)


# Linked to a project
class Image(models.Model):

    image = models.ImageField(upload_to=settings.MEDIA_ROOT)
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return 'Image: {}'.format(self.image.name)
