from django.urls import path

from Appregistration.views import participant, Liste_Formulaire

app_name = 'Appregistration'


urlpatterns = [
    
    path('', participant, name="participants"),
    path('Liste_des_participants/', Liste_Formulaire.as_view(), name='part')
]
