# Generated by Django 5.0.1 on 2024-10-29 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userrequest',
            name='experience',
        ),
    ]
