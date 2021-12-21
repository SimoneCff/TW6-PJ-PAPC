from flask import render_template

from app import app


@app.route('/psu')
def psu():
    return render_template("psu.html")