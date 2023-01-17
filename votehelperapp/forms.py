from django import forms
from django.forms import TextInput, Textarea
from .models import Voter

CHOICES=[('1','Support'),
         ('2',"Do Not Support"),
         ('3',"Undecided"),
         ('4',"Unavailable")
         ]
 
class VoterForm(forms.ModelForm):
    decision = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Voter
        exclude = ['id', 'name', 'address']
        widgets = {
            "title": TextInput(attrs={
                "class": "form-group form",
            }),   
        }

class CreateForm(forms.ModelForm):
    class Meta:
        model = Voter
        exclude = ['id', 'decision', 'notes', 'assignedEmp']
        widgets = {
        'name': forms.Textarea(attrs={'cols': 40, 'rows': 2}),
        'address': forms.Textarea(attrs={'cols': 40, 'rows': 4}),
        'email': forms.Textarea(attrs={'cols': 40, 'rows': 2}),
        'phone': forms.Textarea(attrs={'cols': 40, 'rows': 2}),
        'group': forms.Textarea(attrs={'cols': 40, 'rows': 2}),
        }


