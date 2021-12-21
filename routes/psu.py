from bson.json_util import dumps
from flask import render_template, request

from app import app, Carrello
from complements.db import SearchIntoDb, SearchviaAttributesPSU
from complements.forms import Searchfor, PSUSelect


@app.route('/psu', methods=['POST', 'GET'])
def psu():
    form1 = Searchfor()
    form2 = PSUSelect()
    qir = list()
    if request.method == 'POST':
        if request.form.get('submit'):
            query = SearchIntoDb("PSU", request.form.get('search')).findquery()
            for x in query:
                qir.insert(1, [dumps(x['name']), dumps(x['marca']), dumps(x['COSTO']), dumps(x['_id'])])
            return render_template("psu.html", form=form1, form2=form2, queri=qir)

        if request.form.get('val'):
            x = str(request.form.get('val'))
            x = x.split('"$oid": "', 1)[1]
            x = x.split('"', 1)[0]
            Carrello.Insert(x, 5, "PSU")

        if request.form.get("submitf"):
            marche = list()
            watt = list()
            if request.form.get("Col"):
                marche.append("Cooler Master")
            if request.form.get("Shark"):
                marche.append("Sharkoon")
            if request.form.get("Therm"):
                marche.append("Thermaltake")
            if request.form.get("Cors"):
                marche.append("Corsair")

            if request.form.get("sixfive"):
                watt.append("650")
            if request.form.get("sevenfive"):
                watt.append("750")
            if request.form.get("eightfive"):
                watt.append("850")

            if request.form.get('minmonet'):
                min = request.form.get('minmonet')
            else:
                min = "0"
            if request.form.get('maxmonet'):
                max = request.form.get('maxmonet')
            else:
                max = "10000"

            query = SearchviaAttributesPSU("PSU", " ".join(marche), min, max,
                                           " ".join(watt)).findqueryattr()
            for x in query:
                qir.insert(1, [dumps(x['name']), dumps(x['marca']), dumps(x['COSTO']), dumps(x['_id'])])
            return render_template("psu.html", form=form1, queri=qir, form2=form2)

    return render_template("psu.html", form=form1, form2=form2)
