# Generated by Django 3.2.9 on 2023-04-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_new_course_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_course_model',
            name='id',
        ),
        migrations.AddField(
            model_name='new_course_model',
            name='no_course_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]