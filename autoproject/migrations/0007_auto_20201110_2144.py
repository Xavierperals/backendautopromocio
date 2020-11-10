# Generated by Django 3.1.2 on 2020-11-10 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoproject', '0006_auto_20201110_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formcontact',
            name='browser',
            field=models.CharField(max_length=150, null=True, verbose_name='Navegador'),
        ),
        migrations.AlterField(
            model_name='formcontact',
            name='browser_version',
            field=models.CharField(max_length=150, null=True, verbose_name='Versió de navegador'),
        ),
        migrations.AlterField(
            model_name='formcontact',
            name='device_brand',
            field=models.CharField(max_length=150, null=True, verbose_name='Marca del dispositiu'),
        ),
        migrations.AlterField(
            model_name='formcontact',
            name='device_family',
            field=models.CharField(max_length=150, null=True, verbose_name='Familia de dispositiu'),
        ),
        migrations.AlterField(
            model_name='formcontact',
            name='device_model',
            field=models.CharField(max_length=150, null=True, verbose_name='Model del dispositiu'),
        ),
        migrations.AlterField(
            model_name='formcontact',
            name='os',
            field=models.CharField(max_length=150, null=True, verbose_name='Sistema Operatiu'),
        ),
        migrations.AlterField(
            model_name='formcontact',
            name='os_version',
            field=models.CharField(max_length=150, null=True, verbose_name='Versió de sistema operatiu'),
        ),
        migrations.AlterField(
            model_name='formcontact',
            name='raw_user_agent',
            field=models.CharField(max_length=256, verbose_name='User Agent'),
        ),
    ]
