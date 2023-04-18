from flask import Flask, render_template, request

app = Flask(__name__)

subscribers = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/subscribe')
def subscribe():
    return render_template("subscribe.html")

@app.route('/form', methods=["POST"])
def form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    if not first_name or not last_name or not email:
        error_statement = "All Form Fields Required..."
        return render_template("subscribe.html", error_statement=error_statement,
                               first_name=first_name,
                               last_name=last_name,
                               email=email)

    subscribers.append(f"{first_name} {last_name} | {email}")
    return render_template("form.html", first_name=first_name, last_name=last_name, email=email, subscribers=subscribers)