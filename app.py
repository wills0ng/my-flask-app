from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import smtplib

app = Flask(__name__)
# TODO: Error with command `db.create_all`
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscribers.db'
# Initialize the database
db = SQLAlchemy(app)

# Create db model
class Subscribers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

# Create a function to return a string when we add something
    def __repr__(self):
        return '<Name %r>' % self.id

subscribers = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/photos')
def photos():
    return render_template("photos.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/subscribe')
def subscribe():
    return render_template("subscribe.html")

@app.route('/blogpost')
def blogpost():
    return render_template("blogpost.html")

@app.route('/form', methods=["POST"])
def form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    message = "You have been subscribed to my email newsletter"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("willsong@email.com", "ENV_VARIABLE PASSWORD")
    server.sendmail("willsong@email.com", email, message)

    if not first_name or not last_name or not email:
        error_statement = "All Form Fields Required..."
        return render_template("subscribe.html", error_statement=error_statement,
                               first_name=first_name,
                               last_name=last_name,
                               email=email)

    subscribers.append(f"{first_name} {last_name} | {email}")
    return render_template("form.html", first_name=first_name, last_name=last_name, email=email, subscribers=subscribers)