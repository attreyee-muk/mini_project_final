# Generated by Django 3.2.16 on 2023-02-07 02:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course_deliverables', '0006_course_deliverables'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_deliverables',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]