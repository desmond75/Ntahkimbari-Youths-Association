# Generated by Django 2.0.6 on 2018-06-30 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntakibariapp', '0006_auto_20180630_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.DateField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
    ]
