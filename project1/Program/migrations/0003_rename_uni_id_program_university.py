# Generated by Django 3.2.16 on 2023-03-07 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Program', '0002_program_uni_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='uni_id',
            new_name='university',
        ),
    ]
