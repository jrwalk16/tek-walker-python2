


from ast import Sub
from flask import Flask, redirect, url_for, session
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///puppies.db'

db = SQLAlchemy(app)

class Dogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    breed = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name


class DbPuppyForm(FlaskForm):
    name = StringField("Puppy Name", validators=[DataRequired()])
    breed = StringField("Puppy Breed", validators=[DataRequired()])
    submit = SubmitField("Submit")




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
    name = None
    breed = None
    form = DbPuppyForm()
    if form.validate_on_submit():
        dog = Dogs(name=form.name.data, breed=form.breed.data)
        db.session.add(dog)
        db.session.commit()
    name = form.name.data
    breed = form.breed.data
    form.name.data = ''
    form.breed.data = ''

        #  return redirect(url_for('thankyou'))

    our_dogs = Dogs.query.order_by(Dogs.date_added)
    return render_template('puppy.html', form=form, name=name, breed=breed, our_dogs=our_dogs)

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