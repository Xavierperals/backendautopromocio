# Generated by Django 3.1.2 on 2020-10-20 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autopromotion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='home_page',
            field=models.BooleanField(default=False, verbose_name="Ha d'aparèixer a la pàgina principal?"),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('active', 'Activa'), ('finished', 'Finalitzat')], max_length=20),
        ),
    ]