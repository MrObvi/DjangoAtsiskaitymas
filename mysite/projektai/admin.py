from django.contrib import admin
from .models import Projektas, Klientas, Darbuotojas, Darbas, Saskaita


# Register your models here.

class ProjektasAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas','pradzios_data','pabaigos_data','klientas_id','vadovas_user','darbas_id')
    search_fields = ('pavadinimas', 'klientas_id__vardas')

class DarbuotojasAdmin (admin.ModelAdmin):
    list_display = ('vardas','pavarde','pareigos')
    search_fields = ('vardas', 'pavarde')
    list_filter = ('pareigos',)

class KlientasAdmin(admin.ModelAdmin):
    list_display = ('vardas','pavarde')

class DarbasAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas','pastabos')

admin.site.register(Projektas, ProjektasAdmin)
admin.site.register(Klientas, KlientasAdmin)
admin.site.register(Darbuotojas, DarbuotojasAdmin)
admin.site.register(Darbas,DarbasAdmin)
admin.site.register(Saskaita)
