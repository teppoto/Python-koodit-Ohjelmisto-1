"""Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina."""
import requests

#paikkakunta = input("Municipality name: ")

API_KEY =

#geo = "http://api.openweathermap.org/geo/1.0/direct?q=paikkakunta,{state code},{country code}&limit={limit}&appid={}"
#saa = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={}"

joku = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={}"

vastaus = requests.get(joku).json()
print(vastaus)