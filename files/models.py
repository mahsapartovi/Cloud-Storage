from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserFiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_size = models.IntegerField(default=0)
    file = models.FileField()
    