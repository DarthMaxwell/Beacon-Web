from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Beacons(models.Model):
    station_id = models.IntegerField()
    beacon_id = models.IntegerField()
    beacon_uuid = models.CharField(max_length=200)
    beacon_string = models.CharField(max_length=200)

class Beacon_Reading(models.Model):
    beacon_reading_id = models.IntegerField()
    beacon_id = models.IntegerField()
    user_id = models.IntegerField()
    distance = models.CharField(max_length=200)

class Stations(models.Model):
    station_id = models.IntegerField()
    station_name = models.CharField(max_length=200)
