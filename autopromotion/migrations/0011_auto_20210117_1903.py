# Generated by Django 3.1.2 on 2021-01-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autopromotion', '0010_auto_20210117_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='location',
        ),
        migrations.AlterField(
            model_name='project',
            name='grid_image',
            field=models.ImageField(upload_to='project_images', verbose_name='Imatge Principal'),
        ),
    ]
