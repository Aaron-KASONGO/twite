from .models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def save_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=User)