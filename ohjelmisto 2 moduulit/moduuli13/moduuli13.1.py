from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/alkuluku/<int:aluku>')
def alkuluku(aluku):
    is_prime = True

    if aluku <= 1:
        is_prime = False
    else:
        for luku in range(2, int(aluku**0.5) + 1):
            if aluku % luku == 0:
                is_prime = False
                break

    vastaus = {
        "Number": aluku,
        "isPrime": is_prime
    }

    return jsonify(vastaus)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)