# Generated by Django 2.1.2 on 2018-12-08 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='date_of_event_to',
            new_name='datetime_of_event_from',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='date_of_event_from',
            new_name='datetime_of_event_to',
        ),
        migrations.RemoveField(
            model_name='events',
            name='time_of_event_from',
        ),
        migrations.RemoveField(
            model_name='events',
            name='time_of_event_to',
        ),
    ]
