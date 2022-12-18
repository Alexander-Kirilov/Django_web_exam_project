from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views

from ff_tickets.instructions.forms import InstructionForm
from ff_tickets.instructions.models import Instruction


class InstructionListView(auth_mixins.PermissionRequiredMixin, views.ListView):
    template_name = 'instruction/instructions_all.html'
    forms_model = InstructionForm
    queryset = Instruction.objects.all()
    permission_required = 'instructions.view_instruction'


class InstructionCreateView(auth_mixins.PermissionRequiredMixin, views.CreateView):
    template_name = 'instruction/instruction_create.html'
    model = Instruction
    fields = ('instruction_name', 'instruction_text')
    success_url = reverse_lazy('instructions_all')
    permission_required = 'instructions.create_instruction'
