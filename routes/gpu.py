from flask import request, render_template

from app import Carrello, app

@app.route('/gpu', methods=['POST', 'GET'])
def gpu():
    return render_template("gpu.html")
