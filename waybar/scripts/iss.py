#!/usr/sbin/python3

import http.client
import json

def main() -> None:
    conn = http.client.HTTPConnection("api.open-notify.org")
    
    conn.request("GET", "/iss-now.json")
    res = conn.getresponse()
    data = json.loads(res.read().decode())
    conn.close()

    if res.status == 200:
        lon = float(data['iss_position']['longitude'])
        lat = float(data['iss_position']['latitude'])
        print(f'Lat: {lat}, Lon: {lon}')
    else:
        print('Error')

if __name__ == '__main__':
    main()

