from django.urls import path

from ff_tickets.instructions.views import InstructionListView, InstructionCreateView

urlpatterns = [
    path('', InstructionListView.as_view(), name='instructions_all'),
    path('create/', InstructionCreateView.as_view(), name='instruction_create'),
]
