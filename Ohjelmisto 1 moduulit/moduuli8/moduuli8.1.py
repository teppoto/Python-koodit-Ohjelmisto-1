import mysql.connector

haku = input("Anna ICAO-koodi: ")

def get_airport_by_icao(icao):
    sql = f'select name, municipality from airport where ident = "{icao}"' #select ident, name from airport where municipality = "{municipality}"
    #print(sql)
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute(sql)
    airport_data = cursor.fetchall()
    return airport_data

db_connection = mysql.connector.connect(
    host="localhost",  # host '127.0.0.1'
    port=3306,
    database='flight_game',
    user='teppo',
    password='k1ssa',
    autocommit=True,
)

airport = get_airport_by_icao(haku)
print(airport[0])