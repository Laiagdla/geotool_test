import folium
import requests


def geotranslator(address):
    '''geotranslator("an der filmfabrik")'''

    params = {
        "q": address,
        "format": "json"
    }
    places = requests.get("https://nominatim.openstreetmap.org/search?", params=params).json()
    return [float(places[0]["lat"]), float(places[0]["lon"])]


def map_drawer(coords):
    '''map_drawer(geotranslator("an der filmfabrik"))'''

    m = folium.Map(location=coords)

    folium.Marker(coords, tooltip="You are here").add_to(m)

    folium.Circle(coords, radius=100*1000).add_to(m)

    return m
