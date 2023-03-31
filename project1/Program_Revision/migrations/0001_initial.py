# Generated by Django 3.2.16 on 2023-03-02 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Program', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Program_Revision',
            fields=[
                ('prog_rev_id', models.AutoField(primary_key=True, serialize=False)),
                ('prog_rev_start_dt', models.DateField()),
                ('prog_rev_end_dt', models.DateField()),
                ('prog_rev_name', models.CharField(max_length=300)),
                ('prog_rev_desc', models.CharField(max_length=300)),
                ('prog_rev_status', models.BooleanField()),
                ('prog_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Program.program')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
