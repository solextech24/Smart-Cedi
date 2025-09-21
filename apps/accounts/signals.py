from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def handle_user_profile(sender, instance, created, **kwargs):
    """
    Handle UserProfile creation and updates for User instances
    Consolidates profile management into a single receiver to prevent race conditions
    Uses Django's recommended approach for checking related object existence
    """
    if created:
        # Create profile for new users
        UserProfile.objects.create(user=instance)
    else:
        # For existing users, safely check if profile exists
        try:
            # Try to access the profile
            instance.profile.save()
        except UserProfile.DoesNotExist:
            # Profile doesn't exist, create it
            UserProfile.objects.create(user=instance)