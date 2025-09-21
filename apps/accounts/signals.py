from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def handle_user_profile(sender, instance, created, **kwargs):
    """
    Handle UserProfile creation and updates for User instances
    Consolidates profile management into a single receiver to prevent race conditions
    """
    if created or not hasattr(instance, 'profile'):
        # Create profile for new users or if profile doesn't exist
        UserProfile.objects.create(user=instance)
    else:
        # Save existing profile
        instance.profile.save()