from flask import Flask, render_template 
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app) # init the flask-moment

@app.route('/') 
def index(): 
    return render_template('index.html', current_time=datetime.utcnow()) # Moment library renders timestamp, 
    
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name) #render_template function from flask

@app.errorhandler(500) # idk the actual route yet
def internal_server_error():
    return render_template('500.html')

@app.errorhandler(404)
def page_not_found():
    return render_template('404.html')
