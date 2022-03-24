from pyexpat import model
from re import T
from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title