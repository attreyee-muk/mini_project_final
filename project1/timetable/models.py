from django.db import models
from accounts.models import User

class Timetable(models.Model):
    user_id=models.ForeignKey(User , on_delete=models.CASCADE)
    tt_id=models.AutoField(primary_key=True)
    tt_name=models.CharField(max_length=100)
    tt_desc=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()

    class Meta:
        get_latest_by='tt_id'

# Create your models here.
