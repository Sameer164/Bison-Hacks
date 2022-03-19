from django.shortcuts import render
# import googlemaps
# from googlemaps import client
import requests
# from googleplaces import GooglePlaces, types, lang
import json
# import gmaps




def index(request, *args, **kwargs):
    context = {}
    return render(request, 'gasstation/NextProject.html', context)


def games(request):
    return render(request, 'gasstation/games.html')

def blog(request):
    return render(request, 'gasstation/blog.html')

def home(request):
    return render(request, 'gasstation/home.html')

def contact(request):
    return render(request, 'gasstation/contact.html')

def discussion(request):
    return render(request, 'gasstation/discussion.html')


API_KEY = 'AIzaSyADja9VSAdmvGSz_eH98YbmfkwJAPYq33M'
# Create your views here.
def search(request, *args, **kwargs):
    client_location = googlemaps.Client(API_KEY)
    ip = requests.get("https://api.ipify.org?format=json")
    ip_data = json.loads(ip.text)
    response = requests.get('http://ip-api.com/json/' + ip_data["ip"])
    location_data_one = response.text
    location_data = json.loads(location_data_one)

    print(location_data)
    latitide = location_data['lat']
    longitude = location_data['lon']
    
    nearby_stations = GooglePlaces(API_KEY)
    query_result = nearby_stations.nearby_search(
        lat_lng={'lat': latitide, 'lng': longitude}, 
        radius=1000,
        types=[types.TYPE_GAS_STATION])



    context = {
        'query_list': query_result.places,
        'latitude': latitide,
        'longitude': longitude
    }

   


    
    return render(request, 'gasstation/search.html', context)