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

    return render_template("memory.html", form=form1, form2=form2)
