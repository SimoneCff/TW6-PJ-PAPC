from bson.json_util import dumps

from flask import request, render_template

from app import app, Carrello
from complements.db import SearchIntoDb, SearchviaAttributesCool
from complements.forms import Searchfor, CoolSelect


@app.route('/cooling', methods=['POST', 'GET'])
def cooling():
    form1 = Searchfor()
    form2 = CoolSelect()
    quer = list()

    if request.method == 'POST':
        if request.form.get('submit'):
            query = SearchIntoDb("COOL", request.form.get('search')).findquery()

            for x in query:
                quer.insert(1, [dumps(x['name']), dumps(x['marca']), dumps(x['COSTO']), dumps(x['_id'])])
            return render_template("cooling.html", form=form1, queri=quer, form2=form2)

        if request.form.get('submitf'):
            marca = list()
            socket = list()
            watt = list()
            type = list()

            if request.form.get(""):
                marca.append("")
            if request.form.get(""):
                marca.append("")
            if request.form.get(""):
                marca.append("")


            if request.form.get():
                type.append("air")
            if request.form.get():
                type.append("liquido")

            if request.form.get('minmonet'):
                min = request.form.get('minmonet')
            else:
                min = "0"
            if request.form.get('maxmonet'):
                max = request.form.get('maxmonet')
            else:
                max = "10000"

            query = SearchviaAttributesCool("COOL", " ".join(marca), min, max,
                                           " ".join(watt)).findqueryattr()
            for x in query:
                quer.insert(1, [dumps(x['name']), dumps(x['marca']), dumps(x['COSTO']), dumps(x['_id'])])
            return render_template("cooling.html", form=form1, queri=quer, form2=form2)
        if request.form.get('val'):
            x = str(request.form.get('val'))
            x = x.split('"$oid": "', 1)[1]
            x = x.split('"', 1)[0]
            Carrello.Insert(x, 4, "COOL")
    quer.clear()
    return render_template("cooling.html", form=form1, form2=form2)
