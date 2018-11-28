import sys
import argparse
import requests
import googlemaps

def get_loc():
    response = requests.get('http://api.ipstack.com/103.87.58.6?access_key=f42c4374d0ef9c61749c6c0e1671f200').json()
    lat = response['latitude']
    long = response['longitude']
    return lat, long

def get_places(placeType):
    lat, long = get_loc()
    gmaps = googlemaps.Client(key='MyGoogleKey')
    response = gmaps.places(location=(lat,long), type=placeType)
    print(response.json())
    # print(lat, long)

def main():
    parser = argparse.ArgumentParser(description='Find places around you')
    parser.add_argument('--near', type=str, default='atm', help='What type of place you are looking for?')
    args = parser.parse_args()
    # print(args.near)
    get_places(args.near)

if __name__ == "__main__":
    main()








