# Generated by Django 3.2.16 on 2023-02-07 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('prog_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('prog_name', models.CharField(max_length=150)),
                ('prog_duration', models.CharField(max_length=50)),
                ('prog_desc', models.CharField(max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]