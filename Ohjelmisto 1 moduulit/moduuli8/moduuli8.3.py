import geopy
from geopy import distance
import mysql.connector

icao1 = input("Anna 1. ICAO: ")
icao2 = input("Anna 2. ICAO: ")

def get_airport_coords(icao):
    sql = f'select latitude_deg, longitude_deg from airport where ident = "{icao}"'
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute(sql)
    airport_data = cursor.fetchone() #en saanut toimimaan fetchall:illa
    cursor.close()
    return (airport_data['latitude_deg'], airport_data['longitude_deg'])

db_connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database='flight_game',
    user='teppo',
    password='k1ssa',
    autocommit=True,
)

airport1 = get_airport_coords(icao1)
airport2 = get_airport_coords(icao2)

print(f"{icao1} ja {icao2} etäisyys toisistaan on {distance.distance(airport1, airport2).km} km")