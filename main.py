from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generic")
def generic():
    return render_template("generic.html")

if __name__ == "__main__":
    app.run(debug=True)  