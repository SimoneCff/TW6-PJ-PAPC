from flask import Flask, render_template
from extensions import client

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def index():
    return render_template("templates/index.html")

@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')

if __name__ == '__name__':
    app.run(debug=True)






