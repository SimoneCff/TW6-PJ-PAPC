from flask import render_template

from app import app


@app.route('/ram')
def ram():
    return render_template("ram.html")