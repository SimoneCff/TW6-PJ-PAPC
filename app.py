from flask import Flask, render_template, request

from complements.config import Config
from complements.trolley import Trolley

app = Flask(__name__, static_url_path='', template_folder='templates', static_folder='static')
app.config.from_object(Config)
Carrello = Trolley()

import routes.case, routes.checkout, routes.cooling, routes.cpu, routes.idex, routes.memory, routes.mobo, routes.psu, routes.ram

if __name__ == '__name__':
    app.run(debug=True, ssl_contex='adhoc')
