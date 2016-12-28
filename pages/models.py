from django.db import models


# Model for all testimonials
class Testimonial(models.Model):

    text = models.TextField(max_length=1024)
    quotee = models.CharField(max_length=64)
    company = models.CharField(max_length=64)
    display = models.BooleanField(default=True)
