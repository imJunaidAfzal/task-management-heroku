# Generated by Django 3.2.9 on 2021-11-09 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageTask', '0002_auto_20211109_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 9, 40, 52, 234742)),
        ),
    ]
