# Generated by Django 3.2.9 on 2023-04-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Class', '0005_new_class_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_class_model',
            name='id',
        ),
        migrations.AddField(
            model_name='new_class_model',
            name='no_classes_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
