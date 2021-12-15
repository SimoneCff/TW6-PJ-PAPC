from flask import Flask, render_template, request
from forms import Searchfor
from config import Config
from db import SearchIntoDb
from bson.json_util import dumps
from flask_caching import Cache

app = Flask(__name__, static_url_path='', template_folder='templates', static_folder='static')
app.config.from_object(Config)
app.config['CACHE_TYPE'] = 'simple'

cache = Cache(app)


@app.route('/')
@cache.cached(timeout=10)
def index():
    return render_template("index.html")


@app.route('/cpu', methods=['GET', 'POST'])
def cpu():
    form = Searchfor()
    if form.validate_on_submit():
        query = SearchIntoDb("CPU", request.form.get('search')).findquery()
        quer = list()
        for x in query:
            quer.insert(1,[dumps(x['name']), dumps(x['marca']), dumps(x['COSTO'])])
        return render_template("cpu.html", form=form, queri=quer)

    return render_template("cpu.html", form=form)


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


@app.route('/sw.js', methods=['GET'])
def sw():
    return app.send_static_file('sw.js')


if __name__ == '__name__':
    app.run(debug=True, ssl_contex='adhoc')
