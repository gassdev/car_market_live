# Generated by Django 4.1.2 on 2022-10-10 20:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 10, 20, 50, 57, 389445, tzinfo=datetime.timezone.utc)),
        ),
    ]
