from django.db import models
from accounts.models import User
# Create your models here.
class TF_Min(models.Model):
  user_id=models.ForeignKey(User, on_delete=models.CASCADE)
  tf_id=models.AutoField(primary_key=True)
  tf_name=models.CharField(max_length=100)
  tf_minutes=models.IntegerField()