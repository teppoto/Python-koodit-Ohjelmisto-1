"""Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina."""
import requests

paikkakunta = input("Municipality name: ")
API_KEY = "" #Laita tähän oma API_KEY, koska en jaksunut tehdä git.ignore:a

def get_coordinates(paikkakunta):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": paikkakunta,
        "limit": 1,
        "appid": API_KEY
    }
    data = requests.get(url, params=params).json()
    return (data[0]["lat"], data[0]["lon"]) if data else (None, None)

lat, lon = get_coordinates(paikkakunta)

def get_weather(paikkakunta):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    }
    data = requests.get(url, params=params).json()
    return (data["main"]["temp"], data["weather"][0]["main"])

print(f"Lämpötila ja säätila ovat: {get_weather(paikkakunta)}")