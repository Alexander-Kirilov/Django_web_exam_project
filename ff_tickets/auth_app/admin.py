from django.contrib import admin
from django.contrib.auth import get_user_model

from ff_tickets.auth_app.models import Profile

UserModel = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


@admin.register(UserModel)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]
    exclude = ['password']
    list_display = ("id", "username", "first_name", "last_name", "date_joined", "is_active", "is_staff",)
    ordering = ["-is_staff"]
    list_filter = ["is_active", "is_staff"]
    search_fields = ("username", "id")

