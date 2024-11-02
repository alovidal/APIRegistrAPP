from django.db import models

class usuario(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    sede = models.CharField(max_length=100)
    def __str__(self):
        return self.username
    