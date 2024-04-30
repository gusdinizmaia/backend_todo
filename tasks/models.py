from django.db import models


# Create your models here.
class STATUS_CHOICES(models.TextChoices):
    CONCLUDE = "conclude"
    PENDANT = "pendant"


class Task(models.Model):

    title = models.CharField()
    description = models.CharField()
    date = models.DateField()
    duration = models.TimeField()
    status = models.CharField(choices=STATUS_CHOICES, default=STATUS_CHOICES.PENDANT)
