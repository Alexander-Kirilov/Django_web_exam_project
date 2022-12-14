from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver

from ff_tickets.auth_app.models import Profile

UserModel = get_user_model()


@receiver(signals.post_save, sender=UserModel)
def create_profile_on_user_created(instance, created, *args, **kwargs):
    if not created:
        return
    Profile.objects.create(
        user_id=instance.pk,
    )
