from django.db import models
from datetime import time

class CalendarEvent(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField(default=time(9, 0))

    def __str__(self):
        return self.title

