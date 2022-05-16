

# from tkinter.messagebox import RETRY
from flask import Flask, redirect, url_for, session
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

app.config['SECRET_KEY'] = 'mysecretkey'


class PuppyForm(FlaskForm):

    name = StringField("What is your puppys name?")
    breed = StringField("What is your puppys breed?")
    submit = SubmitField('Submit')

class OwnerForm(FlaskForm):
    owner_name = StringField("What is the owners name?")
    submit = SubmitField('Submit')

@app.route('/puppies',methods=['GET','POST'])
def puppy():
    form = PuppyForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['breed'] = form.breed.data

        return redirect(url_for('thankyou'))

    
    return render_template('puppy.html', form=form)

@app.route('/owners',methods=['GET','POST'])
def owner():
    form = OwnerForm()
    if form.validate_on_submit():
        session['owner_name'] = form.owner_name.data

        return redirect(url_for('thankyou'))

    return render_template('owner.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run()