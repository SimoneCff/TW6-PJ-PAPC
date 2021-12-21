from flask import render_template

from app import app


@app.route('/memory')
def memory():
    return render_template("memory.html")
