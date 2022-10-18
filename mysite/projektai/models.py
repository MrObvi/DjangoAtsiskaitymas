from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Projektas(models.Model):
    pavadinimas = models.CharField('Pavadinimas', max_length=20)
    pradzios_data=models.DateField("Pradžios data")
    pabaigos_data = models.DateField("Pabaigos data")
    klientas_id = models.ForeignKey('Klientas',on_delete=models.SET_NULL,null=True)
    vadovas_user= models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    darbuotojas_id = models.ForeignKey("Darbuotojas",on_delete=models.SET_NULL,null=True)
    darbas_id = models.ForeignKey("Darbas",on_delete=models.SET_NULL,null=True)
    saskaita_id = models.ForeignKey("Saskaita",on_delete=models.SET_NULL,null=True)
    nuotrauka = models.ImageField('Viršelis', upload_to='projekto_virseliai', null=True)
    aprasymas = HTMLField('Aprasymas', null=True)
    class Meta:
        verbose_name = "Projektas"
        verbose_name_plural = 'Projektai'

    def __str__(self):
        return f"{self.pavadinimas} {self.klientas_id} {self.vadovas_user} {self.darbuotojas_id} {self.darbas_id}"

class Klientas(models.Model):
    vardas = models.CharField("Vardas", max_length=20)
    pavarde = models.CharField("Pavardė", max_length=20)
    imone = models.CharField("Įmonė", max_length=20)
    kontaktai = models.TextField("Kontaktai", max_length=500)

    class Meta:
        verbose_name = "Klientas"
        verbose_name_plural = 'Klientai'

    def __str__(self):
        return f"{self.vardas} {self.pavarde} {self.imone}"

class Darbuotojas(models.Model):
    vardas = models.CharField("Vardas", max_length=20)
    pavarde = models.CharField("Pavardė", max_length=20)
    pareigos = models.CharField("Pareigos", max_length=20)

    class Meta:
        verbose_name = "Darbuotojas"
        verbose_name_plural = 'Darbuotojai'

    def __str__(self):
        return f"{self.vardas} {self.pavarde} {self.pareigos}"

class Darbas(models.Model):
    pavadinimas = models.CharField("Pavadinimas", max_length=20)
    pastabos = models.CharField("Pastabos", max_length=200)

    class Meta:
        verbose_name = "Darbas"
        verbose_name_plural = 'Darbai'

    def __str__(self):
        return f"{self.pavadinimas} {self.pastabos} "

class Saskaita(models.Model):
    israsymo_data = models.DateField("Išrašymo data")
    suma = models.PositiveIntegerField("Suma")

    class Meta:
        verbose_name = "Saskaita"
        verbose_name_plural = 'Saskaitos'

    def __str__(self):
        return f"{self.israsymo_data} {self.suma} "