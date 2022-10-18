# import Flask
from flask import Flask, render_template, redirect
from flask.helpers import send_from_directory

app = Flask(__name__, static_folder='frontend/build', static_url_path='/')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')
