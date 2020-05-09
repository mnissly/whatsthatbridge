from django.db import models


class Bridge(models.Model):
    name = models.CharField(max_length=600)
    description = models.CharField(max_length=600, default="this bridge has no description")
    year_built = models.CharField(max_length=600, default="unknown year")
    picture = models.CharField(max_length=600, default="../../static/bridge/default_bridge.jpg")


