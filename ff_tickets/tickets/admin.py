from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_of_submit'
    list_filter = ('problem_status',)
    list_display = ('id', 'created_by', 'problem_description', 'date_of_submit',
                    'problem_status', 'comments', 'assignee', 'updated_at')
    search_fields = ['problem_status', 'store_name', 'assignee', 'sender_name']
