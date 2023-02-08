# Create your models here.
from django.db import models
from accounts.models import User

class Course_Deliverables(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    cd_id=models.AutoField(primary_key=True)
    cd_name=models.CharField(max_length=100)
    cd_desc=models.CharField(max_length=1000)
    cd_duration_min=models.IntegerField() #convert into integer

    def __str__(self):
        return self.cd_id

    

