#!/usr/sbin/python3

# NOTE: this currently works well with a free API key from OpenWeather

import http.client
import json
import os
from dotenv import load_dotenv

ICONS = {
    "01d": "󰖙",
    "01n": "󰖔",
    "02": "󰖕",
    "03": "󰖐",
    "04": "󰖐",
    "09": "󰖗",
    "10": "󰖖",
    "11": "󰖓",
    "13": "󰼶",
    "50": "",
}

def get_location() -> dict:
    # https://ip-api.com/docs/api:json#:~:text=Your%20implementation%20should%20always%20check%20the%20value%20of%20the%20X%2DRl%20header%2C%20and%20if%20its%20is%200%20you%20must%20not%20send%20any%20more%20requests%20for%20the%20duration%20of%20X%2DTtl%20in%20seconds
    endpoint = f"/json"
    conn = http.client.HTTPConnection("ip-api.com:80") # https endpoints are not free
    conn.request("GET", endpoint)
    res = conn.getresponse()
    data = json.loads(res.read().decode())
    conn.close()
    return data

def get_weather(lon: float, lat: float, api_key: str) -> dict:
    endpoint = f"/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    conn = http.client.HTTPSConnection("api.openweathermap.org:443")
    conn.request("GET", endpoint)
    res = conn.getresponse()
    data = json.loads(res.read().decode())
    conn.close()

    if res.status == 200:
        return data
    else:
        raise Exception(f"API responded with {res.status}")

def main() -> None:
    load_dotenv()

    location_data = get_location()
    weather_data = get_weather(location_data['lon'], location_data['lat'], os.getenv('openweather_api_key'))
    location_name = weather_data['name']
    temp = round(weather_data['main']['temp'])
    feels_like = round(weather_data['main']['feels_like'])
    icon_code = weather_data['weather'][0]['icon']
    icon = ''
    if icon_code[:-1] == "01":
        icon = ICONS[icon_code]
    else:
        icon = ICONS[icon_code[:-1]]

    print(f'{icon}   {temp}°C ({feels_like}°C)')

if __name__ == '__main__':
    main()
