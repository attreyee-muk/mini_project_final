# Generated by Django 3.2.16 on 2023-02-07 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course_deliverables', '0005_delete_course_deliverables'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Deliverables',
            fields=[
                ('cd_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('cd_name', models.CharField(max_length=100)),
                ('cd_desc', models.CharField(max_length=1000)),
                ('cd_duration_min', models.IntegerField()),
            ],
        ),
    ]