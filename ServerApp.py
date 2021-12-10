from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__, template_folder='', static_folder='')


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__name__':
    app.run(debug=True)

client = MongoClient("mongodb+srv://admin:admin@papc.q16vr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

