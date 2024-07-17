# models.py
from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=191)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
