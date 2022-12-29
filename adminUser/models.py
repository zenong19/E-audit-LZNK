from django.db import models

# Create your models here.
class setup_user(models.Model):
    userid = models.CharField(max_length=100, default=None)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    access1 = models.CharField(max_length=100, default=None) 
    access2 = models.CharField(max_length=100, default=None) 
    access3 = models.CharField(max_length=100, default=None) 
    access4 = models.CharField(max_length=100, default=None)
    date = models.CharField(max_length=100)