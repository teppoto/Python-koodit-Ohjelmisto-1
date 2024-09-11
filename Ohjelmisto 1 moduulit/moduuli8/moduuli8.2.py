import mysql.connector

haku = input("Anna maakoodi esim. FI: ")

def get_airport_by_iso_country(iso_country):
    sql = f'select type, count(*) from airport where iso_country = "{iso_country}" group by type'
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute(sql)
    airport_data = cursor.fetchall()
    cursor.close()
    return airport_data

db_connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database='flight_game',
    user='teppo',
    password='k1ssa',
    autocommit=True,
)

airport = get_airport_by_iso_country(haku)

print(airport)




