# Generated by Django 5.0.2 on 2024-02-28 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productaccess',
            old_name='user',
            new_name='student',
        ),
    ]
