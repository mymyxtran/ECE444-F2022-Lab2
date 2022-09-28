from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ABCDE'
bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()]) # The StringField class represents an HTML <input> element with a type="text" attribute. And we have an optional validator.
    submit = SubmitField('Submit')

@app.route('/') 
@app.route('/', methods=['GET', 'POST']) 
def index(): 
    form = NameForm() 
    if form.validate_on_submit(): 
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash("Looks like you have changed your name!")
        session['name'] = form.name.data 
        return redirect(url_for('index')) 
    return render_template('index.html', form=form, name=session.get('name'))

@app.errorhandler(500)
def internal_server_error():
    return render_template('500.html')

@app.errorhandler(404)
def page_not_found():
    return render_template('404.html')
