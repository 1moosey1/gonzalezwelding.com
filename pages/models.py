from django.db import models


# Model for all testimonials
class Testimonial(models.Model):

    text = models.TextField(max_length=1024)
    quotee = models.CharField(max_length=64)
    company = models.CharField(max_length=64)
    display = models.BooleanField(default=True)


# Model for project information used in a click carousel
class Project(models.Model):

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    folder = models.CharField(max_length=32)

    def __str__(self):
        return 'Project: {}'.format(self.title)


# Model for every image name that can be linked to a project
class Image(models.Model):

    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)

    def __str__(self):
        return 'Image: {}'.format(self.name)
