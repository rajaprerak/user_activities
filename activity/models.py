from django.db import models

# Create your models here.

class User(models.Model):
    userid = models.IntegerField(primary_key=True)
    real_name = models.CharField(max_length=200)
    tz = models.CharField(max_length=200)

class Activity(models.Model):
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)
    userid = models.ForeignKey(User,related_name='activity_periods',on_delete=models.CASCADE)
