from bson.json_util import dumps
from flask import render_template, request

from app import app, Carrello
from complements.db import SearchIntoDb, SearchviaAttributesRAM
from complements.forms import RAMSelect, Searchfor


@app.route('/ram', methods=['POST', 'GET'])
def ram():
    form1 = Searchfor()
    form2 = RAMSelect()
    quer = list()

    if request.method == 'POST':
        if request.form.get('submit'):
            query = SearchIntoDb("RAM", request.form.get('search')).findquery()

            for x in query:
                quer.insert(1, [dumps(x['name']), dumps(x['marca']), dumps(x['COSTO']), dumps(x['_id'])])
            return render_template("ram.html", form=form1, queri=quer, form2=form2)

        if request.form.get('val'):
            x = str(request.form.get('val'))
            x = x.split('"$oid": "', 1)[1]
            x = x.split('"', 1)[0]
            Carrello.Insert(x, 2, "RAM")

        if request.form.get('submitf'):
            clock = list()
            marca = list()
            qt = list()

            if request.form.get('Col'):
                marca.append("Cooler Master")
            if request.form.get('Cruc'):
                marca.append("Crucial")

            if request.form.get('treetwo'):
                clock.append("3200")
            if request.form.get('treesix'):
                clock.append("3600")

            if request.form.get('six'):
                qt.append("16")
            if request.form.get('tree'):
                qt.append("32")

            if request.form.get('minmonet'):
                min = request.form.get('minmonet')
            else:
                min = "0"
            if request.form.get('maxmonet'):
                max = request.form.get('maxmonet')
            else:
                max = "10000"
            query = SearchviaAttributesRAM("CASE", " ".join(marca), min, max, " ".join(clock), " ".join(qt)
                                           ).findqueryattr()
            for x in query:
                quer.insert(1, [dumps(x['name']), dumps(x['marca']), dumps(x['COSTO']), dumps(x['_id'])])
            return render_template("case.html", form=form1, form2=form2, queri=quer)

    return render_template("ram.html", form=form1, form2=form2)
