"""Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina."""
import requests

#paikkakunta = input("Municipality name: ")

API_KEY = "d67faaf3b5b316fa5f56784009ac06ef"

#geo = "http://api.openweathermap.org/geo/1.0/direct?q=paikkakunta,{state code},{country code}&limit={limit}&appid={d10b1e5c8f49ac3289bb0c1e29bbb096}"
#saa = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={d10b1e5c8f49ac3289bb0c1e29bbb096}"

joku = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={d67faaf3b5b316fa5f56784009ac06ef}"

vastaus = requests.get(joku).json()
print(vastaus)