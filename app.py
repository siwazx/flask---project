from flask import Flask, render_template, request, redirect
from models import db, Menu, Order

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secretkey"

db.init_app(app)

with app.app_context():
    db.create_all()
    
@app.route("/")
def home():
    menus = Menu.query.all()
    return render_template("index.html", menus=menus)

@app.route("/add")
def add_menu():

    menus = [
        # ข้าวผัด
        Menu(name="ข้าวผัดหมู", price=50),
        Menu(name="ข้าวผัดไก่", price=50),
        Menu(name="ข้าวผัดทะเล", price=60),
        Menu(name="ข้าวผัดหมูกรอบ", price=60),

        # กระเพรา
        Menu(name="กระเพราหมู", price=50),
        Menu(name="กระเพราไก่", price=50),
        Menu(name="กระเพราทะเล", price=60),
        Menu(name="กระเพราหมูกรอบ", price=60),

        # เครื่องแกง
        Menu(name="เครื่องแกงหมู", price=55),
        Menu(name="เครื่องแกงไก่", price=55),
        Menu(name="เครื่องแกงทะเล", price=65),
        Menu(name="เครื่องแกงหมูกรอบ", price=65),
    ]

    for menu in menus:
        db.session.add(menu)

    db.session.commit()

    return "เพิ่มเมนูเรียบร้อยแล้ว"

if __name__ == "__main__":
    app.run(debug=True)
    
@app.route("/order/<int:menu_id>")
def order(menu_id):
    new_order = Order(menu_id=menu_id, quantity=1)
    db.session.add(new_order)
    db.session.commit()

    return redirect("/")

@app.route("/orders")
def show_orders():
    orders = Order.query.all()
    return render_template("orders.html", orders=orders)