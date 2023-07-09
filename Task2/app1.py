#Approach 1: SQLAlchemy

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ambitama01@localhost:5432/housing_db'
db = SQLAlchemy(app)

class house(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Float(precision='double'))
    square_footage = db.Column(db.Integer)
    location = db.Column(db.String)
    sale_price = db.Column(db.Integer)

    def __init__(self,id, bedrooms, bathrooms, square_footage, location, sale_price):
        self.id=id
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.square_footage = square_footage
        self.location = location
        self.sale_price = sale_price

@app.route('/housing_data', methods=['POST'])
def create_housing_data():
    data = request.json['data']
    j=1
    for i in data:
        id=j
        j=j+1
        bedrooms = i['Bedrooms']
        bathrooms = i['Bathrooms']
        square_footage = i['SquareFootage']
        location = i['Location']
        sale_price = i['SalePrice']
        new_data = house(id=id,bedrooms=bedrooms, bathrooms=bathrooms, square_footage=square_footage, location=location, sale_price=sale_price) 
        db.session.add(new_data)
    db.session.commit()

    return jsonify({'message': 'Housing data created successfully'}), 201

@app.route('/average_sale_price', methods=['GET'])
def get_average_sale_price():
    result = db.session.query(func.avg(house.sale_price)).scalar()
    return jsonify({'average_sale_price': result})

@app.route('/average_sale_price_per_location', methods=['GET'])
def get_average_sale_price_per_location():
    result = db.session.query(house.location, func.avg(house.sale_price)).group_by(house.location).all()
    average_sale_prices = {location: avg_sale_price for location, avg_sale_price in result}
    return jsonify({'average_sale_price_per_location': average_sale_prices})

@app.route('/max_sale_price', methods=['GET'])
def get_max_sale_price():
    result = db.session.query(func.max(house.sale_price)).scalar()
    return jsonify({'max_sale_price': result})

@app.route('/min_sale_price', methods=['GET'])
def get_min_sale_price():
    result = db.session.query(func.min(house.sale_price)).scalar()
    return jsonify({'min_sale_price': result})

if __name__ == '__main__':
    app.run(debug=True)
