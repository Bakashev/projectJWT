from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class EventPlace(models.Model):
    city = models.CharField(max_length=100)
    event_time = models.DateTimeField()

    class Meta:
        db_table = 'eventPlace'


class Event(models.Model):
    event = models.CharField(max_length=130)
    description = models.TextField()
    user = models.ManyToManyField(User)
    places = models.ManyToManyField(EventPlace)

    class Meta:
        db_table = 'event'



