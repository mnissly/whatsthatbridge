from django.db import models


class Bridge(models.Model):
    name = models.CharField(max_length=600)
    description = models.CharField(max_length=600, default="this bridge has no description")
    year_built = models.CharField(max_length=600, default="unknown year")
    # purpose of defaults is to make sure if bridge location is unknown, app doesn't find it as the closest to someone.
    lat = models.FloatField(default=-32.6536)  # default lat is that of Mt. Aconcogua, highest peak in South America
    long = models.FloatField(default=-70.0115)  # default long is that of Mt. Aconcogua, highest peak in South America
    picture = models.CharField(max_length=600, null=True, blank=True)


