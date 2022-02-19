from django.db import models

# Create your models here.
class Newuser(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=80)
    confirmpassword=models.CharField(max_length=80)
    phonenumber=models.IntegerField()


