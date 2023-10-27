from app import db


# db = SQLAlchemy(app)



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


# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(255), unique=True)
#     password = db.Column(db.String(255))
#     active = db.Column(db.Boolean)
#     roles = db.relationship('Role', secondary='user_roles',
#                             backref=db.backref('users', lazy='dynamic'))
#
#     def __init__(self, username, email, password, active=True):
#         self.username = username
#         self.email = email
#         self.password = password
#         self.active = active
#
#
# class Role(db.Model, RoleMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True)
#     description = db.Column(db.String(255))
#
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description
