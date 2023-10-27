from flask import Flask
# from flask_security import Security, SQLAlchemyUserDatastore
from flask_admin import Admin
from celery import Celery
from flask import request, jsonify
import jsonrpcserver
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/db'
app.config['SECURITY_PASSWORD_SALT'] = 'salt'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

admin = Admin(app)

celery = Celery(app.name, broker='redis://localhost:6379/0')


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    color = db.Column(db.String(20))
    weight = db.Column(db.Float)
    price = db.Column(db.Float)

    def __init__(self, name, color, weight, price):
        self.name = name
        self.color = color
        self.weight = weight
        self.price = price


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(50))
    city = db.Column(db.String(50))
    street = db.Column(db.String(100))

    def __init__(self, country, city, street):
        self.country = country
        self.city = city
        self.street = street


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    products = db.relationship('Product', secondary='order_product', backref='orders')
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    quantity = db.Column(db.Integer)
    status = db.Column(db.String(20))

    def __init__(self, products, address_id, quantity, status):
        self.products = products
        self.address_id = address_id
        self.quantity = quantity
        self.status = status


@app.route('/')
def home():
    return "Welcome to the e-commerce app!"


@app.route('/json-rpc', methods=['POST'])
def json_rpc_endpoint():
    request_data = request.data.decode('utf-8')
    response = jsonrpcserver.dispatch(request_data)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
