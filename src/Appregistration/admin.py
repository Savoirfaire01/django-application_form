from django.contrib import admin
from Appregistration.models import Participants_Form

# Register your models here.




class Participant_FormModelAdmin(admin.ModelAdmin):
    list_display = ('nom_du_participant','prenom_du_participant', 'numero_du_participant', 'email_du_participant')
    
    
admin.site.register(Participants_Form, Participant_FormModelAdmin)

admin.site.site_title = "Participants"
admin.site.site_header = "Participants"
admin.site.index_title = "Participants"

