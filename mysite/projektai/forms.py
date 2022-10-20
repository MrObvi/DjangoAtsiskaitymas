from django import forms
from .models import Projektas

class MyForm(forms.ModelForm):
  class Meta:
    model = Projektas
    fields = ["pavadinimas", "pradzios_data","pabaigos_data", "klientas_id","vadovas_user", "darbuotojas_id","darbas_id", "saskaita_id","nuotrauka", "aprasymas",]
    labels = {'pavadinimas': "Pavadinimas", "pradzios_data": "Pradzios data",}
    # widgets = {'saskaita_id': forms.HiddenInput(), 'nuotrauka': forms.HiddenInput()}