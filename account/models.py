from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.



class Brofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=100)
    state = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    local_goverment = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    dob = models.DateTimeField(blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    def __str__(self):
        return self.fullname

    
