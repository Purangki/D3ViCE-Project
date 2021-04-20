# Generated by Django 3.1.1 on 2021-04-06 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('description', models.CharField(max_length=255)),
                ('is_created', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('status', models.CharField(default='Not Started', max_length=50)),
            ],
            options={
                'db_table': 'Conference',
            },
        ),
    ]
