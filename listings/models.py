from django.db import models
from datetime import datetime
from django.contrib.auth.models import User 


class Listing(models.Model):
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  price = models.CharField(max_length=200)
  quantity = models.IntegerField()
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title