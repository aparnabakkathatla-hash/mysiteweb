from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ImageField(upload_to='events/')

    date = models.DateField(null=True, blank=True)

    category = models.CharField(max_length=100, null=True, blank=True)

    capacity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    email = models.EmailField()

    def __str__(self):
        return self.name