# Generated by Django 4.0.4 on 2022-05-18 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auditUser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelaksanaan_audit',
            name='date',
        ),
    ]
