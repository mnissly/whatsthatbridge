from django.db import models


class Bridge(models.Model):
    name = models.CharField(max_length=600)
    description = models.CharField(max_length=600, default="this bridge has no description")
    year_built = models.CharField(max_length=600, default="unknown year")
    lat = models.FloatField(default=-32.6536)
    long = models.FloatField(default=-70.0115)
    picture = models.CharField(max_length=600, null=True, blank=True)


