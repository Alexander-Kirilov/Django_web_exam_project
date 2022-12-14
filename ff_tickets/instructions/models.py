from django.db import models

from ff_tickets.auth_app.models import Profile


class Instruction(models.Model):
    instruction_name = models.CharField(
        max_length=50,

    )

    instruction_text = models.TextField(
        null=True,
        blank=True,
        max_length=300
    )
