from django import forms

from ff_tickets.instructions.models import Instruction


class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ('instruction_name', 'instruction_text')

