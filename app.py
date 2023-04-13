from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = "Will Song's Portfolio"
    return render_template("index.html", title=title)

@app.route('/about')
def about():
    return render_template("about.html")