from django.db import models

# Create your models here.



class Event(models.Model):
    event_value=models.TextField(max_length=1000)
    event_date=models.CharField(max_length=100)
