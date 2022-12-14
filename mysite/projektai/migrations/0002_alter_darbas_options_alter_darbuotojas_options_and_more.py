# Generated by Django 4.1.2 on 2022-10-18 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projektai', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='darbas',
            options={'verbose_name': 'Darbas', 'verbose_name_plural': 'Darbai'},
        ),
        migrations.AlterModelOptions(
            name='darbuotojas',
            options={'verbose_name': 'Darbuotojas', 'verbose_name_plural': 'Darbuotojai'},
        ),
        migrations.AlterModelOptions(
            name='klientas',
            options={'verbose_name': 'Klientas', 'verbose_name_plural': 'Klientai'},
        ),
        migrations.AlterModelOptions(
            name='projektas',
            options={'verbose_name': 'Projektas', 'verbose_name_plural': 'Projektai'},
        ),
        migrations.AlterModelOptions(
            name='saskaita',
            options={'verbose_name': 'Saskaita', 'verbose_name_plural': 'Saskaitos'},
        ),
        migrations.AddField(
            model_name='projektas',
            name='nuotrauka',
            field=models.ImageField(null=True, upload_to='projekto_virseliai', verbose_name='Viršelis'),
        ),
        migrations.AlterField(
            model_name='darbas',
            name='pastabos',
            field=models.CharField(max_length=200, verbose_name='Pastabos'),
        ),
        migrations.AlterField(
            model_name='saskaita',
            name='suma',
            field=models.PositiveIntegerField(verbose_name='Suma'),
        ),
    ]
