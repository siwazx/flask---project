from flask import Flask, render_template, request, redirect
from models import db, Menu, Order, OrderHistory

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secretkey"

db.init_app(app)

with app.app_context():
    db.create_all()

# ----------------------
# หน้าแรก
# ----------------------
@app.route("/")
def home():
    menus = Menu.query.all()
    return render_template("index.html", menus=menus)

# ----------------------
# เพิ่มเมนูเริ่มต้น (seed)
# ----------------------
@app.route("/seed")
def seed_data():

    if Menu.query.first():
        return "มีเมนูอยู่แล้ว"

    menus = [
        Menu(name="ข้าวผัดหมู", price=50),
        Menu(name="กระเพราหมู", price=50),
        Menu(name="เครื่องแกงหมู", price=55),
    ]

    db.session.add_all(menus)
    db.session.commit()

    return "เพิ่มเมนูเรียบร้อยแล้ว"

# ----------------------
# สั่งอาหาร
# ----------------------
@app.route("/order/<int:menu_id>")
def order(menu_id):

    existing_order = Order.query.filter_by(menu_id=menu_id).first()

    if existing_order:
        existing_order.quantity += 1
    else:
        menu = Menu.query.get_or_404(menu_id)
        new_order = Order(
            menu_id=menu.id,
            quantity=1
        )
        db.session.add(new_order)

    db.session.commit()
    return redirect("/orders")

# ----------------------
# ดูตะกร้า
# ----------------------
@app.route("/orders")
def show_orders():
    orders = Order.query.all()

    total_price = 0
    for order in orders:
        total_price += order.menu.price * order.quantity

    return render_template(
        "orders.html",
        orders=orders,
        total_price=total_price
    )

# ----------------------
# ลบรายการ
# ----------------------

@app.route("/decrease/<int:order_id>")
def decrease(order_id):
    order = Order.query.get_or_404(order_id)

    if order.quantity > 1:
        order.quantity -= 1
    else:
        db.session.delete(order)

    db.session.commit()
    return redirect("/orders")

@app.route("/delete_order/<int:order_id>")
def delete_order(order_id):
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    return redirect("/orders")

# ----------------------
# Checkout
# ----------------------
@app.route("/checkout")
def checkout():
    orders = Order.query.all()

    total_price = 0
    for order in orders:
        total_price += order.menu.price * order.quantity

    if total_price > 0:
        history = OrderHistory(total_price=total_price)
        db.session.add(history)

    for order in orders:
        db.session.delete(order)

    db.session.commit()

    return render_template(
        "success.html",
        total_price=total_price
    )

# ----------------------
# ประวัติ
# ----------------------
@app.route("/history")
def history():
    histories = OrderHistory.query.order_by(
        OrderHistory.created_at.desc()
    ).all()

    return render_template(
        "history.html",
        histories=histories
    )

# ----------------------
# Static pages
# ----------------------
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/menu")
def menu():
    menus = Menu.query.all()
    return render_template("menu.html", menus=menus)

@app.route("/admin")
def admin():
    menus = Menu.query.all()
    return render_template("admin.html", menus=menus)

# ----------------------
# CRUD Menu
# ----------------------

@app.route("/add-menu", methods=["GET", "POST"])
def add_menu():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]

        new_menu = Menu(name=name, price=price)
        db.session.add(new_menu)
        db.session.commit()

        return redirect("/admin")

    return render_template("add_menu.html")

@app.route("/delete-menu/<int:id>")
def delete_menu(id):
    menu = Menu.query.get_or_404(id)
    db.session.delete(menu)
    db.session.commit()
    return redirect("/admin")

@app.route("/edit-menu/<int:id>", methods=["GET", "POST"])
def edit_menu(id):
    menu = Menu.query.get_or_404(id)

    if request.method == "POST":
        menu.name = request.form["name"]
        menu.price = request.form["price"]

        db.session.commit()
        return redirect("/admin")

    return render_template("edit_menu.html", menu=menu)

# ----------------------
# Run
# ----------------------
if __name__ == "__main__":
    app.run(debug=True)