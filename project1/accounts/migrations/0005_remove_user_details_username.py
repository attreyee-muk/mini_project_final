# Generated by Django 3.2.16 on 2023-01-22 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='username',
        ),
    ]