# Import related libraries
from pprint import pprint
import requests
import argparse

if __name__ == '__main__':
    # Define parse args for python script
    parser = argparse.ArgumentParser(description='Sunrise Sunset')

    parser.add_argument('-lat', '--latitude', action='store', metavar="LATITUDE",
                        help='Latitude of location', required=True)

    parser.add_argument('-lng', '--longitude', action='store', metavar='LONGITUDE',
                        help='Longitude of location', required=True)

    args = parser.parse_args()

    url = "https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=today"

    params = {
        "lat": args.latitude,
        "lng": args.longitude
    }

    resp = requests.get(url, params=params)

    data_json = resp.json()

    print(f"Sunrise is {data_json['results']['sunrise']}")
    print(f"Sunset is {data_json['results']['sunset']}")
