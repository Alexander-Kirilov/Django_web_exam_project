from django.urls import path, include

from ff_tickets.tickets.views import TicketCreateView, TicketEditView, TicketListView, TicketDetailView, \
    TicketDeleteView

app_name = 'tickets'

urlpatterns = (
    path('', TicketListView.as_view(), name='all'),
    path('', include([
        path('<int:pk>/detail/', TicketDetailView.as_view(), name='ticket detail'),
        path('create/', TicketCreateView.as_view(), name='ticket create'),
        path('<int:pk>/edit/', TicketEditView.as_view(), name='ticket edit'),
        path('<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket delete')
    ])),
)
