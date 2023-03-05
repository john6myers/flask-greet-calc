from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "Welcome"

@app.route('/welcome/honme')
def welcome_home():
    return "Welcome Home"

@app.route('/welcome/back')
def welcome_back():
    return "Welcome back"

# test