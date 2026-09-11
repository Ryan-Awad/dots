#!/usr/sbin/python3
# NOTE: this currently works well with a free API key from OpenWeather
import http.client
import json
import os
import xml.etree.ElementTree as ET
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

MENU_XML_PATH = "/home/rawad/.config/waybar/menus/weather_menu.xml"

def get_location() -> dict:
    endpoint = f"/?api-key={os.getenv('ipdata_api_key')}"
    conn = http.client.HTTPSConnection("api.ipdata.co")
    conn.request("GET", endpoint)
    res = conn.getresponse()
    data = json.loads(res.read().decode())
    conn.close()
    return data


def get_weather(lon: float, lat: float) -> dict:
    endpoint = f"/data/2.5/weather?lat={lat}&lon={lon}&appid={os.getenv('openweather_api_key')}&units=metric"
    conn = http.client.HTTPSConnection("api.openweathermap.org:443")
    conn.request("GET", endpoint)
    res = conn.getresponse()
    data = json.loads(res.read().decode())
    conn.close()
    if res.status == 200:
        return data
    else:
        raise Exception(f"API responded with {res.status}")


def update_menu_xml(path: str, values: dict) -> None:
    # Update the <property name="label"> text for each GtkMenuItem id in `values`.
    pass
    ET.register_namespace("", "")
    tree = ET.parse(path)
    root = tree.getroot()

    for obj in root.iter("object"):
        obj_id = obj.get("id")
        if obj_id in values:
            label_prop = obj.find("./property[@name='label']")
            if label_prop is not None:
                label_prop.text = str(values[obj_id])
    tree.write(path, encoding="UTF-8", xml_declaration=True)


def main() -> None:
    load_dotenv()
    location_data = get_location()
    weather_data = get_weather(location_data["longitude"], location_data["latitude"])

    location_name = weather_data["name"]
    temp = round(weather_data["main"]["temp"])
    feels_like = round(weather_data["main"]["feels_like"])
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    icon_code = weather_data["weather"][0]["icon"]

    if icon_code[:-1] == "01":
        icon = ICONS[icon_code]
    else:
        icon = ICONS[icon_code[:-1]]

    update_menu_xml(
        MENU_XML_PATH,
        {
            "location": f"Location: {location_name}",
            "wind_speed": f"Wind Spped: {wind_speed} m/s",
            "humidity": f"Humidity: {humidity}%",
            "temp": f"Temperature: {temp}°C",
            "temp_feels": f"Feels Like: {feels_like}°C",
        },
    )

    print(f'{icon} {temp}°C ({feels_like}°C)')


if __name__ == "__main__":
    main()
