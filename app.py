from array import array

from flask import Flask, render_template, request
from forms import Searchfor, CPUSelect
from config import Config
from db import SearchIntoDb, SearchviaAttributesCPU
from bson.json_util import dumps
from trolley import Trolley

app = Flask(__name__, static_url_path='', template_folder='templates', static_folder='static')
app.config.from_object(Config)
Carrello = Trolley()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST', 'GET'])
def checkout():
    if request.method == 'POST':
        if request.form.get('remove'):
            x = request.form.get('remove')
            Carrello.Remove(int(x))

    return render_template("checkout.html", trolley=Carrello.returnList())


@app.route('/cpu', methods=['POST', 'GET'])
def cpu():
    form1 = Searchfor()
    form2 = CPUSelect()
    quer = list()

    if request.method == 'POST':
        if request.form.get('submit'):
            query = SearchIntoDb("CPU", request.form.get('search')).findquery()

            for x in query:
                quer.insert(1, [dumps(x['name']), dumps(x['marca']), dumps(x['COSTO']), dumps(x['_id'])])
            return render_template("cpu.html", form=form1, queri=quer, form2=form2)

        if request.form.get('submitf'):
            marca = list()
            socket = list()
            watt = list()

            if request.form.get("AMD") or request.form.get("INTEL"):
                if request.form.get("AMD"):
                    marca.append("AMD")
                if request.form.get("INTEL"):
                    marca.append("INTEL")

            if request.form.get("AM4") or request.form.get('LGA 1151'):
                if request.form.get("AM4"):
                    socket.append("AM4")
                if request.form.get('LGA 1151'):
                    socket.append("LGA1151")

            if request.form.get("sixfive"):
                watt.append("65")
            if request.form.get("onehunfive"):
                watt.append("105")

            if request.form.get('minmonet'):
                min = request.form.get('minmonet')
            else:
                min = "0"
            if request.form.get('maxmonet'):
                max = request.form.get('maxmonet')
            else:
                max = "10000"

            query = SearchviaAttributesCPU("CPU", " ".join(marca), min, max, " ".join(socket),
                                        " ".join(watt)).findqueryattr()
            for x in query:
                quer.insert(1, [dumps(x['name']), dumps(x['marca']), dumps(x['COSTO']), dumps(x['_id'])])
            return render_template("cpu.html", form=form1, queri=quer, form2=form2)
        if request.form.get('val'):
            x = str(request.form.get('val'))
            x = x.split('"$oid": "', 1)[1]
            x = x.split('"', 1)[0]
            Carrello.Insert(x, 0, "CPU")
    quer.clear()
    return render_template("cpu.html", form=form1, form2=form2)


@app.route('/case', methods=['POST', 'GET'])
def case():
    form1 = Searchfor()
    quer = list()
    if request.method == 'POST':
        if request.form.get('submit'):
            query = SearchIntoDb("CASE", request.form.get('search')).findquery()
            for x in query:
                quer.insert(1, [dumps(x['name']), dumps(x['marca']), dumps(x['COSTO']), dumps(x['_id'])])
                return render_template("case.html", form=form1, queri=quer)
        if request.form.get('val'):
            x = str(request.form.get('val'))
            x = x.split('"$oid": "', 1)[1]
            x = x.split('"', 1)[0]
            Carrello.Insert(x, 6, "CASE")

    return render_template("case.html", form=form1)


@app.route('/cooling')
def cooling():
    return render_template("cooling.html")


@app.route('/memory')
def memory():
    return render_template("memory.html")


@app.route('/mobo')
def mobo():
    return render_template("mobo.html")


@app.route('/psu')
def psu():
    return render_template("psu.html")


@app.route('/ram')
def ram():
    return render_template("ram.html")


if __name__ == '__name__':
    app.run(debug=True, ssl_contex='adhoc')
