from flask import Flask, render_template 
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/') 
def index(): 
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name) #render_template function from flask

@app.route('/500') # idk the actual route yet
def err500():
    return render_template('500.html')

@app.route('/400')
def err400():
    return render_template('400.html')
