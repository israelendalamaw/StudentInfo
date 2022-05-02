from django.db import models


# Create your models here.
class Athletes(models.Model):
    name = models.CharField(max_length=100)
    sport = models.TextField()
    nationality = models.CharField(max_length=100)
    age = models.IntegerField(null='')
    weight = models.CharField(max_length=100)
    height = models.CharField(max_length=100)

    def __str__(self):
        return self.name
