# Generated by Django 3.2.16 on 2023-02-07 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TF_Min', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tf_min',
            name='tf_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]