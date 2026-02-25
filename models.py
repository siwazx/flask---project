from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'))
    quantity = db.Column(db.Integer)

    menu = db.relationship('Menu')