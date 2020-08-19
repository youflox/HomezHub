from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings

class Requests(models.Model):
    user = models.CharField(max_length=50, null=False)
    date  = models.DateTimeField(default=datetime.now, null=False)
    type = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=250, null=False)
    city = models.CharField(max_length=20, null=False)
    state = models.CharField(max_length=20, null=False)
    pin = models.CharField(max_length=10, null=False)
    phone = models.CharField(max_length=20, null=False)

    status_choices = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )

    status = models.CharField(max_length=100,choices=status_choices, blank=True)

    remarks = models.CharField(max_length=200, blank=True)

    updated = models.ForeignKey(User,
                null=True,
                on_delete=models.CASCADE,
                limit_choices_to={'is_staff': True})

    def __str__(self):
        return self.description+'---'+ self.status