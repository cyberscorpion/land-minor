from django.db import models

class LandData(models.Model):
    address = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    land_address = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

    def __str__(self):
        return self.name
