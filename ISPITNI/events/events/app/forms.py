from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    bands = forms.CharField()

    class Meta:
        model = Event
        fields =['name','datetime','poster','outdoor']