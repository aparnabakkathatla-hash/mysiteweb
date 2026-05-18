from django.db import models


class Event(models.Model):

    title = models.CharField(max_length=100)
    date = models.DateField()
    category = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.title