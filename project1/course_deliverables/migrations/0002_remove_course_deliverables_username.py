# Generated by Django 3.2.16 on 2023-02-07 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_deliverables', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_deliverables',
            name='username',
        ),
    ]