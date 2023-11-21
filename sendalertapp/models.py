# alert_app/models.py

from django.db import models

class Alert(models.Model):
    sender_name = models.CharField(max_length=255)
    source_app = models.CharField(max_length=255)
    amount = models.IntegerField()
    sender_message = models.TextField(blank=True, null=True)
    is_test = models.BooleanField()

    def __str__(self):
        return f"{self.sender_name} - {self.source_app}"
from django.db import models

# Create your models here.
