# Generated by Django 2.1.2 on 2018-11-21 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propose_join', '0003_auto_20181121_0854'),
        ('forum', '0004_replies'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='in_club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propose_join.ExistingClub'),
            preserve_default=False,
        ),
    ]
