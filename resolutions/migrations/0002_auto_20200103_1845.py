# Generated by Django 3.0.2 on 2020-01-03 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourusers', '0001_initial'),
        ('resolutions', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Resolutions',
            new_name='Resolution',
        ),
    ]
