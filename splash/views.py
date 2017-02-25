from django.shortcuts import render
from django.http import HttpResponse
from splash.models import Beacons

beacons = Beacons.objects.all()

beaconlist = "<table>"
for beacon in beacons:
    beaconlist = beaconlist + "<tr><td>" + str(beacon.beacon_id) + "</td>"
    beaconlist = beaconlist + "<td>" + beacon.beacon_string + "</td></tr>"
beaconlist =  beaconlist + "</table>"

hello = "<link rel=\"shortcut icon\" type=\"image/png\" href=\"/favicon.ico\"/>Hello, world.<br>"

def index(request):
    return HttpResponse(beaconlist)
