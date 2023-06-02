from django.forms import ModelForm
from .models import Participants_Form
from django import forms




class Participant_Forms(forms.ModelForm):
    
    class Meta:
        model = Participants_Form
        fields = ['nom_du_participant',
                  'prenom_du_participant',
                  'numero_du_participant',
                 'email_du_participant',
        ]
        
        widgets = {'numero_du_participant': forms.NumberInput}
        


