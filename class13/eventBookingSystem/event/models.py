from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    venue = models.CharField(max_length=200)
    organizer = models.CharField(max_length=200)
    max_tickets = models.PositiveIntegerField()

    def __str__(self):
        return self.title

