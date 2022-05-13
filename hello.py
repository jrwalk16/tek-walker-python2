from flask import Flask, render_template



app = Flask(__name__)


@app.route('/')

def index():
    return render_template('basic.html')

@app.route('/puppies')

def puppies():
    return render_template('puppies.html')