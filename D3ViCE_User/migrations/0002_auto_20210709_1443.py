# Generated by Django 3.1.1 on 2021-07-09 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('D3ViCE_User', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelTable(
            name='profile',
            table=None,
        ),
    ]
