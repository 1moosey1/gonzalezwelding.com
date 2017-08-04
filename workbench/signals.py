from django.db.models.signals import post_delete
from django.dispatch import receiver
from workbench.models import Image


# Erase image on disk after model is erased
@receiver(post_delete, sender=Image)
def delete_image(sender, **kwargs):

    instance = kwargs['instance']
    storage, path = instance.image_field.storage, instance.image_field.path
    storage.delete(path)
