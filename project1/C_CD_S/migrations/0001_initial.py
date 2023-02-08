# Generated by Django 3.2.16 on 2023-02-07 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('course_deliverables', '0009_course_deliverables'),
        ('Staff', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='C_CD_S',
            fields=[
                ('c_cd_s_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('course_no_of_units', models.IntegerField(default=1)),
                ('course_used_no_of_units', models.IntegerField()),
                ('cd_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course_deliverables.course_deliverables')),
                ('course_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('staff_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Staff.staff')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
