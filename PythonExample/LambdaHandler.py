import json
import base64
import googlemaps
S_RATIO = 1.5
vV = 230
from datetime import datetime

def lambda_handler(event, context):
    gmaps = googlemaps.Client(key='xxxxxxxxxxxx')
    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions("Avenida de Burgos 16B",
                                         "Avenida de los Toreros 75, Madrid",
                                     mode=event['mode'],
                                     departure_time=now,
                                     alternatives=True)
    print directions_result
    return directions_result

if __name__ == '__main__':
    lambda_handler({'mode': "driving"},1)