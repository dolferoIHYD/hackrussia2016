from __future__ import unicode_literals

from django.db import models

class Truck(models.Model):
    token = models.CharField(max_length=20)
    driver = models.CharField(max_length=50)
    state_number = models.CharField(max_length=6)
    at_poligon = models.BooleanField(default=False)


class Arrival(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    truck = models.ForeignKey(Truck)


class Deport(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    truck = models.ForeignKey(Truck)
