from flask import Flask, render_template 
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ABCDE'
bootstrap = Bootstrap(app)
moment = Moment(app) # init the flask-moment

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()]) # The StringField class represents an HTML <input> element with a type="text" attribute. And we have an optional validator.
    submit = SubmitField('Submit')


@app.route('/') 
@app.route('/', methods=['GET', 'POST'])
def index(): 
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name) #render_template function from flask

@app.errorhandler(500) # idk the actual route yet
def internal_server_error():
    return render_template('500.html')

@app.errorhandler(404)
def page_not_found():
    return render_template('404.html')

