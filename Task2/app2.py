from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

def connect_to_db():
    conn = psycopg2.connect(
        host="localhost",
        database="housing_db",
        user="postgres",
        password="ambitama01"
    )
    return conn

@app.route('/housing_data', methods=['POST'])
def create_housing_data():
    data = request.json['data']
    conn = connect_to_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    j = 1
    for i in data:
        id = j
        j += 1
        bedrooms = i['Bedrooms']
        bathrooms = i['Bathrooms']
        square_footage = i['SquareFootage']
        location = i['Location']
        sale_price = i['SalePrice']
        cur.execute("INSERT INTO house (id, bedrooms, bathrooms, square_footage, location, sale_price) VALUES (%s, %s, %s, %s, %s, %s)",
                    (id, bedrooms, bathrooms, square_footage, location, sale_price))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'message': 'Housing data created successfully'}), 201

@app.route('/average_sale_price', methods=['GET'])
def get_average_sale_price():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT AVG(sale_price) FROM house")
    result = cur.fetchone()[0]
    cur.close()
    conn.close()
    return jsonify({'average_sale_price': result})

@app.route('/average_sale_price_per_location', methods=['GET'])
def get_average_sale_price_per_location():
    conn = connect_to_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT location, AVG(sale_price) as average_sale_price FROM house GROUP BY location")
    result = cur.fetchall()
    cur.close()
    conn.close()
    average_sale_prices = {row['location']: row['average_sale_price'] for row in result}
    return jsonify({'average_sale_price_per_location': average_sale_prices})

@app.route('/max_sale_price', methods=['GET'])
def get_max_sale_price():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT MAX(sale_price) FROM house")
    result = cur.fetchone()[0]
    cur.close()
    conn.close()
    return jsonify({'max_sale_price': result})

@app.route('/min_sale_price', methods=['GET'])
def get_min_sale_price():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT MIN(sale_price) FROM house")
    result = cur.fetchone()[0]
    cur.close()
    conn.close()
    return jsonify({'min_sale_price': result})

if __name__ == '__main__':
    app.run(debug=True)
