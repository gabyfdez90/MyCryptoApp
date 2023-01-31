from app_crypto import app
from app_crypto.models import *
from flask import render_template, jsonify, request
from config import VERSION
import sqlite3
from http import HTTPStatus

@app.route("/")
def index():
    return render_template('index.html')

#Aquí se crean también los endpoints 

@app.route(f"/api/{VERSION}/movement",methods=["POST"])
def new_movement():
    registro = request.json
    try:
        add_movement([ registro['date'],registro['concept'],registro['quantity'] ])
        return jsonify(
            {
                "status": "OK"
            }
        ),HTTPStatus.CREATED 
    except sqlite3.Error as e:
         return jsonify(
            {
                "data": str(e),
                "status": "Error"
            }
        ),HTTPStatus.BAD_REQUEST