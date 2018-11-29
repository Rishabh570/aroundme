import sys
import argparse
import requests
import googlemaps
from viewer import views

def get_loc():
    response = requests.get('http://api.ipstack.com/103.87.58.6?access_key=f42c4374d0ef9c61749c6c0e1671f200').json()
    lat = response['latitude']
    long = response['longitude']
    return lat, long

def get_places(placeType):
    lat, long = get_loc()
    gmaps = googlemaps.Client(key='AIzaSyBmm69zn5d5KfDNAct9DHTVs9CR0EKq_Ro')
    response = gmaps.places(query=placeType ,location=(lat,long))
    views.show(response['results'], placeType)

def main():
    parser = argparse.ArgumentParser(description='Find places around you, default place is hotel')
    parser.add_argument('-n', type=str, default='hotel', help='What type of place you are looking for?')
    args = parser.parse_args()
    get_places(args.near)

if __name__ == "__main__":
    main()








