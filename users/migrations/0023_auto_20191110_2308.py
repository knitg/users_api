# Generated by Django 2.2.7 on 2019-11-10 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_remove_tailor_myfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tailor',
            name='image',
        ),
        migrations.RemoveField(
            model_name='tailor',
            name='image_size',
        ),
    ]
