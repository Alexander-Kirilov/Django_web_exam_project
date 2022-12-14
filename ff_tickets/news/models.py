from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import get_user_model

from cloudinary import models as cloudinary_models
from ff_tickets.tickets.models import Ticket

UserModel = get_user_model()


class News(models.Model):
    title = models.CharField(
        max_length=50
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    is_private = models.BooleanField(
        default=True,
    )

    news_photos = cloudinary_models.CloudinaryField(
        null=True,
        blank=True,
        # upload_to="images/"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "news"
