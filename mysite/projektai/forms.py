from django import forms
from .models import Projektas

class DateInput(forms.DateInput):
  input_type = 'date'
class MyForm(forms.ModelForm):
  class Meta:
    model = Projektas
    fields = ["pavadinimas", "pradzios_data","pabaigos_data", "klientas_id","vadovas_user", "darbuotojas_id","darbas_id", "saskaita_id","nuotrauka", "aprasymas",]
    labels = {'pavadinimas': "Pavadinimas", "pradzios_data": "Pradzios data",}
    widgets = {'pradzios_data': DateInput(), "pabaigos_data": DateInput()}