from django.shortcuts import render
from geopy.geocoders import Nominatim
# Create your views here.
from django.http import HttpResponse
from .models import Input,Hospital
from .forms import InputForm
import requests, json
from math import radians, cos, sin, asin, sqrt


hospital_names = []
def input(request):
    global hospital_names
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            geolocator = Nominatim(user_agent="maps")
            user_address_input = form.cleaned_data['location']
            location_address = geolocator.geocode(user_address_input)
            #source = ((location_address.latitude, location_address.longitude))
            source_lat = radians(location_address.latitude)
            source_lon = radians(location_address.longitude)
            #print(source_lat, source_lon)
            items = Hospital.objects.all()
            filter_citites = Hospital.objects.filter(City = user_address_input)
            print(filter_citites.iterator())
            #print(filter_citites)
            # hospital_names = []
            for item in filter_citites.iterator():
                #print(item.Name)
                dest_address = geolocator.geocode(item.Locality)
                #print(dest_address)
                dest_lat = radians(dest_address.latitude)
                dest_lon = radians(dest_address.longitude)
                #print(dest_lon)
                dlon = dest_lon - source_lon
                dlat = dest_lat - source_lat
                a = sin(dlat / 2)**2 + cos(source_lat) * cos(dest_lat) * sin(dlon / 2)**2
                c = 2 * asin(sqrt(a))
                r = 6371
                if c * r <= 200 :
                    hospital_names.append(item)
            return render(request,'maps/hospital_name.html', {'form': hospital_names} )    
    # Radius of earth in kilometers. Use 3956 for miles 
                #url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
                #r = requests.get(url + 'origins = ' + source +'&destinations = ' + dest +'&key = ' + api_key)
                #if distance.text <= '2.5 km' :
                #    print(items.Name)
    else:
        form = InputForm()
    return render(request, 'maps/input.html', {'form': form})

# def person_list(request):
#     table = PersonTable(Hospital.objects.all())

#     return render(request, "maps/hospital_list.html", {"table": table})

def list(request,pk):
    items = Hospital.objects.get(pk = pk)

    return render(request, 'maps/hospital_list.html', {'items': items})