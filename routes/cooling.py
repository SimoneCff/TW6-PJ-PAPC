from flask import render_template

from app import app


@app.route('/cooling')
def cooling():
    return render_template("cooling.html")
