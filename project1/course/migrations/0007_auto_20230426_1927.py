# Generated by Django 3.2.9 on 2023-04-26 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_course_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='prog_rev_id',
        ),
        migrations.RemoveField(
            model_name='course',
            name='university',
        ),
    ]
