from django.db import models
from django.forms import ValidationError







class Participants_Form(models.Model):
    nom_du_participant = models.CharField(max_length=100)
    prenom_du_participant = models.CharField(max_length=100, blank=True)
    numero_du_participant = models.CharField(max_length=10)
    email_du_participant = models.EmailField()
    
    def __str__(self):
        return self.nom_du_participant
    
   
    