from flask import Flask, render_template

app = Flask(__name__, static_url_path='', template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/cpu')
def cpu():
    return render_template("cpu.html")

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

@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')


if __name__ == '__name__':
    app.run(debug=True)






