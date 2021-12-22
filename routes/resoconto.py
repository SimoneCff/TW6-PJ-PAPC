from flask import render_template, request

from app import app, Carrello


@app.route('/resoconto', methods=['POST', 'GET'])
def resoconto():
    quer = Carrello.returnList()
    psuis = Carrello.SeeWatt()
    cpuis = Carrello.SeeCompatibiltyCPU()
    ramis = Carrello.SeeCompatibiltyRAM()
    if request.method == 'POST':
        if request.method.get('Check'):
            return render_template('resoconto.html', quer=quer, psu=psuis, cpu=cpuis, ram=ramis)
    return render_template('resoconto.html', quer=quer)
