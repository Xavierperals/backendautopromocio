# Generated by Django 3.1.2 on 2020-10-23 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autopromotion', '0003_projectcontact_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='amenties',
            field=models.CharField(default='', help_text='Escriu, separat per comes, les caracteristiques del projecte.', max_length=500, verbose_name='Caracteristiques'),
        ),
    ]
