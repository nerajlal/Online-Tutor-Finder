# Generated by Django 3.2.7 on 2022-02-07 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0017_alter_studentdata_proimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmedList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.CharField(max_length=200, null=True)),
                ('appliedby', models.CharField(max_length=200, null=True)),
                ('appliedname', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
