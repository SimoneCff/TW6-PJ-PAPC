from flask import request, render_template

from app import Carrello, app


@app.route('/checkout', methods=['POST', 'GET'])
def checkout():
    right = False
    if request.method == 'POST':
        if request.form.get('remove'):
            x = request.form.get('remove')
            Carrello.Remove(int(x))
        else:
            right = True
            return render_template("checkout.html", trolley=Carrello.returnList(), right=right, psu=Carrello.SeeWatt(),
                                   case=Carrello.SeeCompatibiltyCase(), ram=Carrello.SeeCompatibiltyRAM(),
                                   cpu=Carrello.SeeCompatibiltyCPU())
    return render_template("checkout.html", trolley=Carrello.returnList(), right=right)
