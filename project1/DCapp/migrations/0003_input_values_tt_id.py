# Generated by Django 3.2.9 on 2023-04-27 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DCapp', '0002_rename_no_classes_input_values_no_periods'),
    ]

    operations = [
        migrations.AddField(
            model_name='input_values',
            name='tt_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
