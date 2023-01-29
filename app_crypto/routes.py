from app_crypto import app
from flask import render_template

@app.route("/")
def index():
    return render_template('index.html')

#Aquí se crean también los endpoints 