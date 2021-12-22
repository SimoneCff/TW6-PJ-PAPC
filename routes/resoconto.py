from flask import render_template

from app import app


@app.route('/resoconto', methods=['POST', 'GET'])
def resoconto():
    return render_template('resoconto.html')