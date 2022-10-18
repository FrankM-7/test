# import Flask
from flask import Flask, render_template, redirect
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin


app = Flask(__name__ ,static_folder='client/build',static_url_path='')
cors = CORS(app)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run()