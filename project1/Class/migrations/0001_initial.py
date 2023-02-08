# Generated by Django 3.2.16 on 2023-02-07 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Program', '0001_initial'),
        ('Program_Revision', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=100)),
                ('class_desc', models.CharField(max_length=100)),
                ('class_parent_id', models.IntegerField()),
                ('course_semester', models.IntegerField()),
                ('prog_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Program.program')),
                ('prog_rev_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Program_Revision.program_revision')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
