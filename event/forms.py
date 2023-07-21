
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields='__all__'
        widgets ={
            "start_date": forms.TextInput(attrs={"type":"date"}),
            "end_date": forms.TextInput(attrs={"type":"date"})
        }