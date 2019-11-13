# Generated by Django 2.2.7 on 2019-11-13 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_tailor_alternate_days'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tailor',
            old_name='weekends',
            new_name='isOpen',
        ),
        migrations.RemoveField(
            model_name='tailor',
            name='weekdays',
        ),
        migrations.AddField(
            model_name='tailor',
            name='alternate_days',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tailor',
            name='isWeekdays',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='tailor',
            name='isWeekends',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]