from bson.json_util import dumps
from flask import request, render_template

from app import Carrello, app
from complements.db import SearchIntoDb, SearchviaAttributesCASE
from complements.forms import Searchfor, CaseSelect


@app.route('/gpu', methods=['POST', 'GET'])
def gpu():
    render_template("gpu.html")