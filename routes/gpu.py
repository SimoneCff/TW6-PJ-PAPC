from bson.json_util import dumps
from flask import request, render_template

from app import Carrello, app
from complements.db import SearchIntoDb, SearchviaAttributesGPU
from complements.forms import Searchfor, GPUSelect


@app.route('/gpu', methods=['POST', 'GET'])
def gpu():
    form1 = Searchfor()
    form2 = GPUSelect()
    quer = list()

    if request.method == 'POST':
        if request.form.get('submit'):
            query = SearchIntoDb("GPU", request.form.get('search')).findquery()

            for x in query:
                quer.insert(1, [dumps(x['name']), dumps(x['marca']), dumps(x['COSTO']), dumps(x['_id'])])
            return render_template("gpu.html", form=form1, queri=quer, form2=form2)

        if request.form.get('val'):
            x = str(request.form.get('val'))
            x = x.split('"$oid": "', 1)[1]
            x = x.split('"', 1)[0]
            Carrello.Insert(x, 3, "GPU")

        if request.form.get('submitf'):
            marca = list()
            prod = list()
            tipo = list()

            if request.form.get('Asus'):
                marca.append("Asus")
            if request.form.get('xfx'):
                marca.append("XFX")
            if request.form.get('Giga'):
                marca.append("Gigabyte")

            if request.form.get('AMD'):
                prod.append("AMD")
            if request.form.get('Nvidia'):
                prod.append("Nvidia")

            if request.form.get('RX'):
                tipo.append("RX")
            if request.form.get('RTX'):
                tipo.append("RTX")

            if request.form.get('minmonet'):
                min = request.form.get('minmonet')
            else:
                min = "0"
            if request.form.get('maxmonet'):
                max = request.form.get('maxmonet')
            else:
                max = "100000"

            query = SearchviaAttributesGPU("GPU", " ".join(marca), min, max, " ".join(prod),
                                           " ".join(tipo)).findqueryattr()

            for x in query:
                quer.insert(1, [dumps(x['name']), dumps(x['marca']), dumps(x['COSTO']), dumps(x['_id'])])
            return render_template("gpu.html", form=form1, queri=quer, form2=form2)

    return render_template("gpu.html",  form=form1, form2=form2)
