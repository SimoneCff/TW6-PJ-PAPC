from bson.json_util import dumps
from flask import render_template, request

from app import app, Carrello
from complements.db import SearchIntoDb
from complements.forms import Searchfor, MoboSelect


@app.route('/mobo', methods=['POST', 'GET'])
def mobo():
    form1 = Searchfor()
    form2 = MoboSelect()
    quer = list()
    if request.method == 'POST':
        if request.form.get('submit'):
            query = SearchIntoDb("MOBO", request.form.get('search')).findquery()

            for x in query:
                quer.insert(1, [dumps(x['name']), dumps(x['marca']), dumps(x['COSTO']), dumps(x['_id'])])
            return render_template("mobo.html", form=form1, queri=quer, form2=form2)

    if request.form.get('val'):
        x = str(request.form.get('val'))
        x = x.split('"$oid": "', 1)[1]
        x = x.split('"', 1)[0]
        Carrello.Insert(x, 1, "MOBO")

    if request.form.get('submitf'):
        socket = list()
        model = list()
        watt = list()
        clock = list()
        marca = list()

        if request.form.get("Asus"):
            marca.append("Asus")
        if request.form.get("MSI"):
            marca.append("MSI")
        if request.form.get("Giga"):
            marca.append("Gigabyte")

        if request.form.get("AM4"):
            socket.append("AM4")
        if request.form.get('LGA 1200'):
            socket.append("LGA 1200")

        if request.form.get("twofive"):
            clock.append("2500")
        if request.form.get("fourfive"):
            clock.append("4500")
        if request.form.get("fivetre"):
            clock.append("5300")

        if request.form.get("ATX"):
            model.append("ATX")
        if request.form.get("mATX"):
            model.append("mATX")

        if request.form.get("seventy"):
            watt.append("70")
        if request.form.get("fifty"):
            watt.append("50")

        if request.form.get('minmonet'):
            min = request.form.get('minmonet')
        else:
            min = "0"
        if request.form.get('maxmonet'):
            max = request.form.get('maxmonet')
        else:
            max = "10000"

        query = SearchviaAttributesMobo("MOBO", " ".join(marca), min, max, " ".join(socket),
                                        " ".join(watt), " ".join(model), " ".join(clock)).findqueryattr()

    return render_template("mobo.html", form=form1, form2=form2)
