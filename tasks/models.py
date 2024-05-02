from django.db import models


# Create your models here.
class STATUS_CHOICES(models.TextChoices):
    CONCLUDE = "conclude"
    PENDANT = "pendant"


class Task(models.Model):

    title = models.CharField(max_length=44)
    description = models.CharField(max_length=144)
    date = models.DateField()
    duration = models.TimeField()
    status = models.CharField(
        max_length=8, choices=STATUS_CHOICES, default=STATUS_CHOICES.PENDANT
    )
