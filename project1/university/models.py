from django.db import models
from accounts.models import User


class University(models.Model):
    uni_id=models.AutoField(primary_key=True)
    uni_name=models.CharField(max_length=100)

# Create your models here.
