# Generated by Django 3.2.16 on 2023-03-02 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Class_Schedule', '0001_initial'),
        ('C_CD_S', '0001_initial'),
        ('Room', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TT_Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_cd_s_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='C_CD_S.c_cd_s')),
                ('cs_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Class_Schedule.class_schedule')),
                ('room_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Room.room')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
