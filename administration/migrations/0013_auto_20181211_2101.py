# Generated by Django 2.1.2 on 2018-12-11 15:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0012_auto_20181211_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onpollclub',
            name='release_date',
            field=models.TimeField(default=datetime.datetime(2018, 12, 11, 21, 1, 45, 429434)),
        ),
    ]
