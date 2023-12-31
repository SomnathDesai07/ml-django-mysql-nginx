from django.db import models

class HousePricePredictionModel(models.Model):
    location = models.CharField(null=True, blank=True,max_length=100)
    size = models.IntegerField(null=True, blank=True)
    total_sqf = models.IntegerField(null=True, blank=True)
    bath = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)