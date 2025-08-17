from flask import Flask
import os 
app = Flask(__name__)

@app.route('/') 
def home ():
    return '<h1>Welcome</h1>'

@app.route('/about')
def about():
    return '<h1>About us</h1>'