from django.db import models

class Bridge(models.Model):
    name = models.CharField(max_length=200)
    year_built = models.IntegerField(default=0)



