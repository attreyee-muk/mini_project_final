# Generated by Django 3.2.16 on 2023-03-12 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Program', '0005_remove_program_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
