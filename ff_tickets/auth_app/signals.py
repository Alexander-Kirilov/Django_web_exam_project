from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver

from ff_tickets.auth_app.models import Profile

UserModel = get_user_model()


@receiver(signals.post_save, sender=UserModel)
def create_profile_on_user_created(instance, created, *args, **kwargs):
    if not created:
        return
    Profile.objects.create(
        user_id=instance.pk,
    ),
    instance.groups.add(Group.objects.get(name='users'))

