# Generated by Django 2.1.2 on 2018-10-13 13:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20181013_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerprofile',
            name='va_type',
        ),
        migrations.AddField(
            model_name='registerprofile',
            name='Profession',
            field=models.CharField(choices=[('Job', 'job'), ('Buisness', 'buisness')], default=datetime.datetime(2018, 10, 13, 13, 19, 46, 780833, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
    ]
