from bson.json_util import dumps
from flask import render_template, request
from complements.db import SearchIntoDb, SearchviaAttributesMem
from complements.forms import Searchfor, MEMOSelect
from app import Carrello

from app import app


@app.route('/memory',  methods=['POST', 'GET'])
def memory():
    form1 = Searchfor()
    form2 = MEMOSelect()
    qir = list()

    if request.method == 'POST':
        if request.form.get('submit'):
            query = SearchIntoDb("MEM", request.form.get('search')).findquery()
            for x in query:
                qir.insert(1, [dumps(x['name']), dumps(x['marca']), dumps(x['COSTO']), dumps(x['_id'])])
            return render_template("memory.html", form=form1, form2=form2, queri=qir)
        if request.form.get('val'):
            x = str(request.form.get('val'))
            x = x.split('"$oid": "', 1)[1]
            x = x.split('"', 1)[0]
            Carrello.Insert(x, 7, "MEM")

        if request.form.get('submitf'):
            marca = list()
            type = list()
            size = list()

            if request.form.get('Cruc'):
                marca.append("Crucial")
            if request.form.get('Sam'):
                marca.append("Samsung")
            if request.form.get('Sea'):
                marca.append("Seagate")
            if request.form.get('WD'):
                marca.append("WD")

            if request.form.get('SSD'):
                type.append("SSD")
            if request.form.get('HD'):
                type.append("HD")

            if request.form.get('quattro'):
                size.append("480")
            if request.form.get('cinque'):
                size.append("500")
            if request.form.get('mille'):
                size.append("1000")

            if request.form.get('minmonet'):
                min = request.form.get('minmonet')
            else:
                min = "0"
            if request.form.get('maxmonet'):
                max = request.form.get('maxmonet')
            else:
                max = "10000"

            query = SearchviaAttributesMem("MEM", " ".join(marca), min, max, " ".join(size),
                                           " ".join(type)).findqueryattr()
            for x in query:
                qir.insert(1, [dumps(x['name']), dumps(x['marca']), dumps(x['COSTO']), dumps(x['_id'])])
            return render_template("memory.html", form=form1, queri=qir, form2=form2)

    return render_template("memory.html", form=form1, form2=form2)
