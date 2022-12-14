from django.urls import reverse_lazy
from django.views import generic as views

from ff_tickets.instructions.forms import InstructionForm
from ff_tickets.instructions.models import Instruction


class InstructionListView(views.ListView):
    template_name = 'instruction/instructions_all.html'
    forms_model = InstructionForm
    queryset = Instruction.objects.all()


class InstructionCreateView(views.CreateView):
    template_name = 'instruction/instruction_create.html'
    model = Instruction
    fields = ('instruction_name', 'instruction_text')
    success_url = reverse_lazy('instructions_all')
