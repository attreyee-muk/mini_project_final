# Generated by Django 3.2.16 on 2023-01-31 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_user_details_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user_details',
        ),
    ]
