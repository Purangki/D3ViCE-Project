# Generated by Django 3.1.1 on 2021-07-16 02:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('D3ViCE_User', '0008_auto_20210715_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='date',
            field=models.DateField(default=datetime.date(2021, 7, 16)),
        ),
    ]