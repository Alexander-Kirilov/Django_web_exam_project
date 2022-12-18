from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from ff_tickets.auth_app.models import Profile

UserModel = get_user_model()


class UserCreateForm(auth_forms.UserCreationForm):

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'position', 'address', 'city', 'country')

