from flask import render_template

from app import app


@app.route('/mobo')
def mobo():
    return render_template("mobo.html")