# Generated by Django 5.0.1 on 2024-03-18 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='deed',
            new_name='action',
        ),
    ]
