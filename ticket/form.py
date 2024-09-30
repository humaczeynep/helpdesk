from django import forms
from .models import Ticket

class CreatTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']


class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']

