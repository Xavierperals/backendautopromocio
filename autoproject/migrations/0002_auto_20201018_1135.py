# Generated by Django 3.1.2 on 2020-10-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formcontact',
            options={'verbose_name': 'Contacte Autoproject', 'verbose_name_plural': 'Contactes Autoproject'},
        ),
        migrations.AlterField(
            model_name='formcontact',
            name='city',
            field=models.CharField(max_length=100, verbose_name='Ciutat'),
        ),
        migrations.AlterField(
            model_name='formcontact',
            name='comment',
            field=models.CharField(max_length=250, verbose_name='Comentari'),
        ),
        migrations.AlterField(
            model_name='formcontact',
            name='house_price',
            field=models.IntegerField(verbose_name='Preu'),
        ),
        migrations.AlterField(
            model_name='formcontact',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='formcontact',
            name='neighborhood',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Barri'),
        ),
        migrations.AlterField(
            model_name='formcontact',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Telf'),
        ),
        migrations.AlterField(
            model_name='formcontact',
            name='size',
            field=models.CharField(choices=[('LESS_THAN_60', 'Menos de 60'), ('BETWEEN_60_AND_80', 'Entre 60 y 80'), ('BETWEEN_80_AND_100', 'Entre 80 y 100'), ('BETWEEN_100_AND_120', 'Entre 100 y 120'), ('MORE_THAN_120', 'Más de 120')], max_length=20, verbose_name='Mida'),
        ),
        migrations.AlterField(
            model_name='formcontact',
            name='wants_contact',
            field=models.BooleanField(verbose_name='Vol ser contactat?'),
        ),
    ]