# Generated by Django 3.2.16 on 2023-02-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Program', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='prog_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
