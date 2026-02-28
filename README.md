# 🍔 Food Ordering Website (Flask Project)

## 📌 Project Description
This project is a web-based food ordering system developed using **Flask (Python)**.  
Users can browse menu items, add products to cart, checkout, and view order history.  
The system stores order data in a SQLite database.

This project was created as part of a Web Development assignment.

---

## 🚀 Features

- View food menu
- Add items to cart
- Calculate total price automatically
- Checkout and save order history
- View past purchase history
- Admin can add or delete menu items
- Database integration using SQLite

---

## 🛠 Technologies Used

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- Bootstrap 5 (CSS Framework)
- HTML / CSS

---

## 📂 Project Structure

flask-project/
│
├── app.py
├── database.db
├── README.md
│
├── templates/
│ ├── index.html
│ ├── orders.html
│ ├── checkout.html
│ ├── history.html
│ ├── about.html
│ ├── contact.html
│ ├── menu.html
│ ├── add-menu.html
│ └── ...
│
└── static/
└── (CSS / images if any)


---

## ⚙ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone <YOUR_GIT_URL>
cd flask-project
2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install flask flask_sqlalchemy
4️⃣ Run the Application
python app.py

Then open your browser and go to:

http://127.0.0.1:5000
🗄 Database

The project uses SQLite as the database.
Tables are created using SQLAlchemy models inside app.py.

Main tables:

Menu

Order

OrderHistory

📝 Git Workflow

This project follows:

Commit Early

Commit Often

More than 50 commits
Work completed across at least 10 days

📸 Screenshots

(Add screenshots of your website here)

Example:

![Homepage](screenshots/home.png)
👨‍💻 Author

Student Name: (Siwakorn Sangkaew)
Course: Web Development
Year: 2026