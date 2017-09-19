from django.db import models


# Model for work/project information
class Project(models.Model):

    class Meta:
        ordering = ['-last_modified']

    title = models.CharField(unique=True, max_length=64)
    description = models.TextField(max_length=512)
    last_modified = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=True)

    def __str__(self):
        return 'Project: {}'.format(self.title)


# Linked to a project
class Image(models.Model):

    image_field = models.ImageField(upload_to="")
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return 'Image: {}'.format(self.image_field.url)
