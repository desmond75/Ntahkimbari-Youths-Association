# Generated by Django 2.0.6 on 2018-07-05 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntakibariapp', '0019_auto_20180704_2305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date',
            new_name='event_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.AddField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default=datetime.time(23, 6, 56, 105503)),
        ),
    ]
