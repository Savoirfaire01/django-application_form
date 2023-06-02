from django.shortcuts import render
from django.http import  HttpResponseRedirect
from .forms import Participant_Forms
from .models import Participants_Form
from django.views.generic import ListView




class Liste_Formulaire(ListView):
    model = Participants_Form
    
    template_name = 'list_des_participants.html'
    context_object_name = 'forms'
    


def participant(request):

    if request.method == "POST":
        form = Participant_Forms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = Participant_Forms
    
    return render(request, 'formulaire.html', {'form':form})






'''
def Vue_des_participants(request):
    
 
    forms = Participant_Forms()
    
    return render(request, 'list_des_participants.html', {'forms':forms})
  '''
  
  
  
  

