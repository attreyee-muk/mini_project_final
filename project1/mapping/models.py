from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mapping(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    class_data=models.CharField(max_length=150)
    course_data=models.CharField(max_length=150)
    room_data=models.IntegerField()
    staff_data=models.CharField(max_length=150)
    time_data=models.IntegerField()

    