from flask import request, render_template

from app import Carrello, app


@app.route('/checkout', methods=['POST', 'GET'])
def checkout():
    if request.method == 'POST':
        if request.form.get('remove'):
            x = request.form.get('remove')
            Carrello.Remove(int(x))

    return render_template("checkout.html", trolley=Carrello.returnList())