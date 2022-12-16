from django.contrib.auth import get_user_model
from django.db import models

from ff_tickets.core.model_mixins import StoresName, ProblemType, ProblemStatusChoice

UserModel = get_user_model()


class Ticket(models.Model):
    MAX_LEN_NAME = 10
    MAX_LEN_SENDER_NAME = 20

    store_name = models.CharField(
        max_length=MAX_LEN_NAME,
        choices=StoresName.choices(),
        null=False,
        blank=False,
        verbose_name='Обект',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Подал',
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Обновен'
    )

    created_by = models.ForeignKey(
        UserModel,
        null=True,
        on_delete=models.CASCADE
    )

    problem_type = models.CharField(
        max_length=30,
        choices=ProblemType.choices(),
        null=True,
        blank=False,
        verbose_name='Вид проблем',
        default="other"
    )

    problem_description = models.TextField(
        max_length=400,
        null=False,
        blank=False,
        verbose_name='Описание',
    )

    date_of_submit = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
        verbose_name='Дата на подаване',
    )

    problem_status = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        choices=ProblemStatusChoice.choices(),
        verbose_name="Статус",
        default='a_posted',

    )

    comments = models.TextField(
        max_length=800,
        default='',
        verbose_name='Коментар',
        blank=True,
        null=True,

    )

    assignee = models.ForeignKey(
        UserModel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Назначен',
        related_name='assignee_user'

    )

    class Meta:
        ordering = ["problem_status", "date_of_submit"]
