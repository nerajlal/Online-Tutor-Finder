# Generated by Django 3.2.7 on 2021-12-23 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('phone', models.IntegerField()),
                ('password', models.CharField(max_length=200)),
                ('account', models.CharField(choices=[('Teacher', 'Teacher'), ('Parent', 'Parent')], max_length=10, null=True)),
            ],
        ),
    ]
