# Generated by Django 3.2.7 on 2022-02-15 06:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=200, null=True)),
                ('reciever', models.CharField(max_length=200, null=True)),
                ('message', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]