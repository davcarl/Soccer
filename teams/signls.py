from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Coach

@receiver(post_save, sender=User)
def create_coach(sender, instance, created, **kwargs):
    if created:
        Coach.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_coach(sender, instance, **kwargs):
    instance.profile.save()


