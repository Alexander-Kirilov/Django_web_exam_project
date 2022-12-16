from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.http import HttpResponse

from ff_tickets.tickets.models import Ticket


class TicketBaseView(views.View):
    model = Ticket
    fields = ['store_name', 'problem_type', 'problem_description', 'problem_status', 'comments', 'assignee']
    success_url = reverse_lazy('tickets:all')


class TicketListView(TicketBaseView, views.ListView):
    template_name = 'tickets/ticket_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        pattern = self.__get_pattern()

        if pattern:
            queryset = queryset.filter(store_name__icontains=pattern)
        return queryset

    def __get_pattern(self):
        pattern = self.request.GET.get('pattern', None)
        return pattern.lower() if pattern else None


class TicketDetailView(auth_mixins.UserPassesTestMixin, views.DetailView):
    template_name = 'tickets/ticket_detail.html'
    raise_exception = True
    model = Ticket
    fields = ['store_name', 'problem_type', 'problem_description', 'problem_status', 'comments', 'assignee']
    success_url = reverse_lazy('tickets:all')
    permission_required = ('tickets.view_ticket', 'ticket.delete_ticket', 'tickets.change_ticket')


class TicketCreateView(TicketBaseView, views.CreateView):
    template_name = 'tickets/ticket_form.html'
    fields = ('store_name', 'problem_type', 'problem_description', 'assignee',)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TicketEditView(auth_mixins.PermissionRequiredMixin, views.UpdateView):
    raise_exception = True
    model = Ticket
    fields = ['store_name', 'problem_type', 'problem_description', 'problem_status', 'comments', 'assignee']
    success_url = reverse_lazy('tickets:all')
    permission_required = ('tickets.view_ticket', 'tickets.delete_ticket', 'tickets.change_ticket')


class TicketDeleteView(TicketBaseView, views.DeleteView):
    template_name = 'tickets/ticket_confirm_delete.html'
