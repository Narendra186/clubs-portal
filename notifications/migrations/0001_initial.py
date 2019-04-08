# Generated by Django 2.1.2 on 2018-12-12 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100)),
                ('sender', models.CharField(default='', max_length=100)),
                ('notifications', models.CharField(max_length=1000, null=True)),
                ('date', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
