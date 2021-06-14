from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
