# Generated by Django 3.2.7 on 2022-02-19 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CHAT', '0002_alter_chat_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='sendername',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
