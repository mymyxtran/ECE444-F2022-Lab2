from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError

from flask_caching import Cache

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ABCDE'
cache = Cache(config={'CACHE_TYPE': 'null'})
bootstrap = Bootstrap(app)
# some time later
cache.init_app(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()]) # The StringField class represents an HTML <input> element with a type="text" attribute. And we have an optional validator.
    email = EmailField('What is your UofT email address?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

@app.route('/') 
@app.route('/', methods=['GET', 'POST']) 
def index(): 
    form = NameForm() 
    if form.validate_on_submit(): 
        old_name = session.get('name')
        old_email = session.get('email')
        if old_name is not None and old_name != form.name.data:
            flash("Looks like you have changed your name!")
        if old_email is not None and old_email != form.email.data:
            flash("Looks like you have changed your email!")
        session['name'] = form.name.data 
        session['email'] = form.email.data
        return redirect(url_for('index')) 

    email_message = ''
    email_message =  "Your UofT email is "+ session.get('email')
    if 'utoronto' not in  session.get('email'):
        email_message = "Please use your UofT email."

    return render_template('index.html', form=form, name=session.get('name'), email_message=email_message)

@app.errorhandler(500)
def internal_server_error():
    return render_template('500.html')

@app.errorhandler(404)
def page_not_found():
    return render_template('404.html')
