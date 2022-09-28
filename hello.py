from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/') 
def index(): 
    return render_template('index.html', time=1)
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name) #render_template function from flask

# bootstrap = Bootstrap(app)
