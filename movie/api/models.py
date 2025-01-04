from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="image")
    director = models.CharField(max_length=50)
    rating =models.CharField(max_length=10)
    duration = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10,decimal_places=2)
