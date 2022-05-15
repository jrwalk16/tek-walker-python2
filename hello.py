from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://puppies.db'

@app.route('/')

def index():
    return render_template('basic.html')

@app.route('/puppies')

def puppies():
    return render_template('puppies.html')

@app.route('/owners')

def owners():
     return render_template('owners.html')