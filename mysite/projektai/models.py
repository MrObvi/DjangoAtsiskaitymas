from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Projektas(models.Model):
    pavadinimas = models.CharField(_('Pavadinimas'), max_length=20)
    pradzios_data=models.DateField(_("Pradžios data"))
    pabaigos_data = models.DateField(_("Pabaigos data"))
    klientas_id = models.ForeignKey('Klientas',on_delete=models.SET_NULL,null=True)
    vadovas_user= models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    darbuotojas_id = models.ForeignKey("Darbuotojas",on_delete=models.SET_NULL,null=True)
    darbas_id = models.ForeignKey("Darbas",on_delete=models.SET_NULL,null=True)
    saskaita_id = models.ForeignKey("Saskaita",on_delete=models.SET_NULL,null=True)
    nuotrauka = models.ImageField(_('Viršelis'), upload_to='projekto_virseliai', null=True)
    aprasymas = HTMLField(_('Aprasymas'), null=True)
    class Meta:
        verbose_name = _("Projektas")
        verbose_name_plural = _('Projektai')
        ordering = ['pradzios_data',]

    def __str__(self):
        return f"{self.pavadinimas} {self.klientas_id} {self.vadovas_user} {self.darbuotojas_id} {self.darbas_id}"

class Klientas(models.Model):
    vardas = models.CharField(_("Vardas"), max_length=20)
    pavarde = models.CharField(_("Pavardė"), max_length=20)
    imone = models.CharField(_("Įmonė"), max_length=20)
    kontaktai = models.TextField(_("Kontaktai"), max_length=500)

    class Meta:
        verbose_name = _("Klientas")
        verbose_name_plural = _('Klientai')

    def __str__(self):
        return f"{self.vardas} {self.pavarde} {self.imone}"

class Darbuotojas(models.Model):
    vardas = models.CharField(_("Vardas"), max_length=20)
    pavarde = models.CharField(_("Pavardė"), max_length=20)
    pareigos = models.CharField(_("Pareigos"), max_length=20)

    class Meta:
        verbose_name = _("Darbuotojas")
        verbose_name_plural = _('Darbuotojai')

    def __str__(self):
        return f"{self.vardas} {self.pavarde} {self.pareigos}"

class Darbas(models.Model):
    pavadinimas = models.CharField(_("Pavadinimas"), max_length=20)
    pastabos = models.CharField(_("Pastabos"), max_length=200)

    class Meta:
        verbose_name = _("Darbas")
        verbose_name_plural = _('Darbai')

    def __str__(self):
        return f"{self.pavadinimas} {self.pastabos} "

class Saskaita(models.Model):
    israsymo_data = models.DateField(_("Išrašymo data"))
    suma = models.PositiveIntegerField(_("Suma"))

    class Meta:
        verbose_name = _("Saskaita")
        verbose_name_plural = _('Saskaitos')

    def __str__(self):
        return f"{self.israsymo_data} {self.suma} "