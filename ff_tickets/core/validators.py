from django.core import exceptions


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha() and not ch == " ":
            raise exceptions.ValidationError('Only letters are allowed')
