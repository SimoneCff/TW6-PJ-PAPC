from bson.json_util import dumps
from flask import request, render_template

from app import Carrello, app
from complements.db import SearchIntoDb, SearchviaAttributesCASE
from complements.forms import Searchfor, CaseSelect


@app.route('/case', methods=['POST', 'GET'])
def case():
    form1 = Searchfor()
    form2 = CaseSelect()
    qir = list()
    if request.method == 'POST':
        if request.form.get('submit'):
            query = SearchIntoDb("CASE", request.form.get('search')).findquery()
            for x in query:
                qir.insert(1, [dumps(x['name']), dumps(x['marca']), dumps(x['COSTO']), dumps(x['_id'])])
            return render_template("case.html", form=form1, form2=form2, queri=qir)
        if request.form.get('val'):
            x = str(request.form.get('val'))
            x = x.split('"$oid": "', 1)[1]
            x = x.split('"', 1)[0]
            Carrello.Insert(x, 6, "CASE")
        if request.form.get("submitf"):
            marche = list()
            model = list()
            if request.form.get("Col"):
                marche.append("Cooler Master")
            if request.form.get("Shark"):
                marche.append("Sharkoon")
            if request.form.get("Therm"):
                marche.append("Thermaltake")

            if request.form.get("ATX"):
                model.append("ATX")
            if request.form.get("mATX"):
                model.append("mATX")

            if request.form.get('minmonet'):
                min = request.form.get('minmonet')
            else:
                min = "0"
            if request.form.get('maxmonet'):
                max = request.form.get('maxmonet')
            else:
                max = "10000"
            query = SearchviaAttributesCASE("CASE", " ".join(marche), min, max, " ".join(model)
                                            ).findqueryattr()
            for x in query:
                qir.insert(1, [dumps(x['name']), dumps(x['marca']), dumps(x['COSTO']), dumps(x['_id'])])
            return render_template("case.html", form=form1, form2=form2, queri=qir)

    return render_template("case.html", form=form1, form2=form2)
