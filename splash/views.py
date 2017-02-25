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
<<<<<<< HEAD
    return HttpResponse("<link rel=\"shortcut icon\" type=\"image/png\" href=\"/favicon.ico\"/>https://images-na.ssl-images-amazon.com/images/G/01/img15/pet-products/small-tiles/23695_pets_vertical_store_dogs_small_tile_8._CB312176604_.jpg")
=======
    return HttpResponse(beaconlist)
>>>>>>> ce4a3b07c4488f95bf592e675cb58813c5fe8e8f
