from flask import Flask, render_template, request
from forms import Searchfor
from config import Config
from db import SearchIntoDb
from bson.json_util import dumps


app = Flask(__name__, static_url_path='', template_folder='templates', static_folder='static')
app.config.from_object(Config)
app.config['CACHE_TYPE'] = 'simple'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/cpu', methods=['POST'])
def cpu():
    form1 = Searchfor()
    quer = list()

    if form1.validate_on_submit():
        query = SearchIntoDb("CPU", request.form.get('search')).findquery()

        for x in query:
            quer.insert(1,[dumps(x['name']), dumps(x['marca']), dumps(x['COSTO']), dumps(x['_id'])])
        return render_template("cpu.html", form=form1, queri=quer)

    return render_template("cpu.html", form=form1)



@app.route('/case')
def case():
    return render_template("case.html")


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
