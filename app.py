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

if __name__ == "__main__":
    app.run(debug=True)