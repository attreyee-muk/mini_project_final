# Generated by Django 3.2.9 on 2023-04-26 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_remove_university_user_id'),
        ('course', '0007_auto_20230426_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='prog_rev_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='university.university'),
        ),
    ]