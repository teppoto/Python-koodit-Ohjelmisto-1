from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/kentta/<icao>')
def get_airport_by_icao(icao):
    sql = 'SELECT name, municipality FROM airport WHERE ident = %s'
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    airport_data = cursor.fetchone()

    if airport_data:
        vastaus = {
            "ICAO": icao,
            "Name": airport_data["name"],
            "Municipality": airport_data["municipality"],
        }
    else:
        vastaus = {"error": "Airport not found"}

    return jsonify(vastaus)

db_connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database='flight_game',
    user='teppo',
    password='k1ssa',
    autocommit=True,
)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)

