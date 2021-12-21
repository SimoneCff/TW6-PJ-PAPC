from bson.json_util import dumps
from flask import render_template, request

from app import app, Carrello
from complements.db import SearchIntoDb
from complements.forms import Searchfor, MoboSelect


@app.route('/mobo',  methods=['POST', 'GET'])
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

    return render_template("mobo.html", form=form1, form2=form2)