# Generated by Django 2.1.2 on 2018-11-12 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_profile_ug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='test',
        ),
    ]
