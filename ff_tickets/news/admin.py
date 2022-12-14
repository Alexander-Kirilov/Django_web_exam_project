from django.contrib import admin

from ff_tickets.news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'created_by', 'is_private']
