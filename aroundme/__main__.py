import sys
import argparse
import requests
import googlemaps

class bcolors:
    HEADER = '\033[95m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def show(data, query):
    print("\n\n\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print('\n', bcolors.OKBLUE, bcolors.BOLD, bcolors.HEADER, "Here's a list of {} near you".format(query), bcolors.ENDC, '\n')
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print('\n')
    for item in data:
        print('  - ', bcolors.BOLD, item['name'], bcolors.ENDC, '\n')
        print(bcolors.OKGREEN, '    * ', bcolors.ENDC,
              bcolors.DARKCYAN ,'Address: ' , bcolors.ENDC,
              item['formatted_address'], '\n',
              bcolors.OKGREEN, '   * ', bcolors.ENDC,
              bcolors.DARKCYAN ,'Rating: ' , bcolors.ENDC,
              item['rating'], '\n',
              )
    return 'Hope to see you again :)'


def get_loc():
    response = requests.get('http://api.ipstack.com/103.87.58.6?access_key=f42c4374d0ef9c61749c6c0e1671f200').json()
    lat = response['latitude']
    long = response['longitude']
    return lat, long


def get_places(placeType):
    lat, long = get_loc()
    gmaps = googlemaps.Client(key='AIzaSyBmm69zn5d5KfDNAct9DHTVs9CR0EKq_Ro')
    response = gmaps.places(query=placeType ,location=(lat,long))
    return show(response['results'], placeType)


def main():
    parser = argparse.ArgumentParser(description='Find places around you, default place is hotel')
    parser.add_argument('--near', type=str, default='hotel', help='What type of place you are looking for?')
    args = parser.parse_args()
    return get_places(args.near)


if __name__ == "__main__":
    main()
