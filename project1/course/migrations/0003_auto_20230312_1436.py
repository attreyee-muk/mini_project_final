# Generated by Django 3.2.16 on 2023-03-12 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_university'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='prog_rev_id',
        ),
        migrations.RemoveField(
            model_name='course',
            name='user_id',
        ),
    ]
