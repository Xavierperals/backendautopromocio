# Generated by Django 3.1.2 on 2020-10-20 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autopromotion', '0002_auto_20201020_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcontact',
            name='property',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='autopromotion.project'),
            preserve_default=False,
        ),
    ]
