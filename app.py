from flask import Flask, render_template

app = Flask(__name__, static_url_path='', template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template("index.html");

@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')

if __name__ == '__name__':
    app.run(debug=True)






