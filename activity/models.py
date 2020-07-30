from django.db import models


# Create your models here.

class User(models.Model):
    """
    User Model:- Contains 3 fields(id(Primary Key), name, timezone)
    """
    userid = models.IntegerField(primary_key=True)
    real_name = models.CharField(max_length=200)
    tz = models.CharField(max_length=200)


class Activity(models.Model):
    """
    Activity Model:- Contains 3 fields(id(Foreign Key), activity start time, activity end time)
    """
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)
    userid = models.ForeignKey(User, related_name='activity_periods', on_delete=models.CASCADE)
