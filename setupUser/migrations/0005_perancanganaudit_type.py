# Generated by Django 4.0.4 on 2022-08-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setupUser', '0004_rename_element_sejarahaudit_pp'),
    ]

    operations = [
        migrations.AddField(
            model_name='perancanganaudit',
            name='type',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
