# Generated by Django 2.2.7 on 2019-11-10 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_tailor_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tailor',
            name='myfile',
        ),
    ]
