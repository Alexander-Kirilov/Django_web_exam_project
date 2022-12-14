from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models

from ff_tickets.auth_app.managers import AppUserManager
from ff_tickets.core.validators import validate_only_letters


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    MIN_LEN_USERNAME_NAME = 2
    MAX_LEN_USERNAME_NAME = 30

    username = models.CharField(
        max_length=MAX_LEN_USERNAME_NAME,
        blank=True,
        null=True,
        validators=(
            validators.MinLengthValidator(MIN_LEN_USERNAME_NAME),
        ),
        unique=True
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    is_active = models.BooleanField(
        default=True
    )
    USERNAME_FIELD = 'username'
    objects = AppUserManager()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def first_name(self):
        return self.profile.first_name

    @property
    def last_name(self):
        return self.profile.last_name

    @property
    def position(self):
        return self.profile.position

    @property
    def address(self):
        return self.profile.address

    @property
    def email(self):
        return self.profile.email

    @property
    def city(self):
        return self.profile.city

    @property
    def country(self):
        return self.profile.country


class Profile(models.Model):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30
    MIN_LEN_POSITION = 2
    MAX_LEN_POSITION = 30
    MIN_LEN_ADDRESS = 2
    MAX_LEN_ADDRESS = 30
    MIN_LEN_CITY = 2
    MAX_LEN_CITY = 30
    MIN_LEN_COUNTRY = 2
    MAX_LEN_COUNTRY = 30

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        blank=True,
        null=True,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        blank=True,
        null=True,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        )
    )

    position = models.CharField(
        max_length=MAX_LEN_POSITION,
        blank=True,
        null=True,
        validators=(
            validators.MinLengthValidator(MIN_LEN_POSITION),
            validate_only_letters,
        )
    )

    email = models.EmailField(

        blank=True,
        null=True,
        unique=True,
    )

    address = models.CharField(
        max_length=MAX_LEN_ADDRESS,
        blank=True,
        null=True,
        validators=(
            validators.MinLengthValidator(MIN_LEN_ADDRESS),
        )
    )

    city = models.CharField(
        max_length=MAX_LEN_CITY,
        blank=True,
        null=True,
        validators=(
            validators.MinLengthValidator(MIN_LEN_CITY),
            validate_only_letters,
        )
    )

    country = models.CharField(
        max_length=MAX_LEN_COUNTRY,
        blank=True,
        null=True,
        validators=(
            validators.MinLengthValidator(MIN_LEN_COUNTRY),
            validate_only_letters,
        )
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.user)




